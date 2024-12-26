from TypeCheckerParser import TypeCheckerParser as ExprParser
from TypeCheckerVisitor import TypeCheckerVisitor as ExprVisitor
import re

class TypeChecker(ExprVisitor):
    def __init__(self):
        self.symbol_table = {}  # Tracks variable names and their types
        self.used_variables = set()  # Tracks variables that are used
        self.valid_variable_pattern = re.compile(r"^[a-zA-Z_][a-zA-Z0-9_]*$")  # Regex for valid names
        self.inheritance_map = {}  # Tracks inheritance relationships

    def markVariableAsUsed(self, var_name):
        """Helper function to mark variables as used."""
        self.used_variables.add(var_name)

    def get_line_info(self, ctx):
        """Helper function to get the line number and position from the context."""
        line = ctx.start.line if ctx.start else None  # Get line number
        col = ctx.start.column if ctx.start else None  # Get column number
        return line, col

    def is_type_compatible(self, declared_type, expr_type):
        # If both types are the same, it's compatible
        if declared_type == expr_type:
            return True

        # Check if the declared type is a superclass of the assigned type
        if declared_type in self.inheritance_map:
            current_type = expr_type
            while current_type is not None:
                if current_type == declared_type:
                    return True
                current_type = self.inheritance_map.get(current_type, None)
        
        # If not compatible, return False
        return False

    def visitProgram(self, ctx:ExprParser.ProgramContext):
        # Visit all statements in the program
        for statement in ctx.statement():
            self.visit(statement)

        # Check for unused variables after visiting the whole program
        for var, info in self.symbol_table.items():
            if var not in self.used_variables:
                line = info["line"]
                print(f"Warning: Variable '{var}' declared at line {line} is declared but never used.")
    
    def visitShowStatement(self, ctx:ExprParser.ShowStatementContext):
        # Evaluate the expression
        expr_type = self.visit(ctx.expression())
        
        # Get the line and column for better error messages
        line, col = self.get_line_info(ctx)

        # Validate the type
        if expr_type == 'none':
            raise Exception(f"Cannot show a 'none' value at line {line}, column {col}.")

        # Print the evaluated value (as a placeholder for actual execution)
        print(f"Output: {expr_type}")
    
    def visitVariableDeclaration(self, ctx:ExprParser.VariableDeclarationContext):
        # The variable signature is part of the variable declaration
        var_signature = ctx.variableSignature()

        # Extract the variable name and type from the signature
        var_name = var_signature.variableName().getText()
        var_type = var_signature.type_().getText()  # The declared type of the variable

        # Get line number for better error messages
        line, col = self.get_line_info(ctx)

        # Check that the variable name starts with '$' and validate the rest of the name
        if not var_name.startswith('$'):
            raise Exception(f"Invalid variable name: '{var_name}' at line {line}, column {col}. Variable names must start with '$'.")
        
        # Check if the variable name is valid (you can implement custom logic here)
        if not self.valid_variable_pattern.match(var_name[1:]): # Check what follows '$'
            raise Exception(f"Invalid variable name: '{var_name}' at line {line}, column {col}. Variable names must start with a letter or underscore and contain only alphanumeric characters.")

        # Check for redeclaration of the variable
        if var_name in self.symbol_table:
            raise Exception(f"Variable '{var_name}' already declared.")

        # Add the variable to the symbol table with its declared type and the line number
        self.symbol_table[var_name] = {"type": var_type, "line": line}

        # Check the initializer expression for type mismatch
        initializer = ctx.expression() or ctx.createClassStatement()  # Check if there's an initializer expression

        if initializer:
            init_val = self.visit(initializer)  # Visit the initializer to get its type
            # TODO: Handle class initialization & get variable type
            init_type = init_val if isinstance(init_val, str) else init_val  # Get the type of the initializer
            if init_type != var_type:
                raise Exception(f"Type mismatch: Cannot assign {init_type} to {var_type} for variable '{var_name}' at line {line}, column {col}.")
    
    def visitAssignment(self, ctx:ExprParser.AssignmentContext):
        # Extract the variable name from the assignment
        var_name = ctx.variableName().getText()

        # Get line number for better error messages
        line, col = self.get_line_info(ctx)

        # Check if the variable has been declared
        if var_name not in self.symbol_table:
            raise Exception(f"Variable '{var_name}' not declared at line {line}, column {col}.")

        # Mark the variable as used
        self.used_variables.add(var_name)

        # Get the type of the variable from the symbol table
        declared_type = self.symbol_table[var_name]

        # Visit the assigned expression to determine its type
        expr_type = self.visit(ctx.expression())

        # Check for type compatibility: if declared type is a class type, check inheritance
        if not self.is_type_compatible(declared_type, expr_type):
            raise Exception(f"Type mismatch: Cannot assign {expr_type} to {declared_type} for variable '{var_name}' at line {line}, column {col}.")
        
        # If types are compatible, continue (assignment is valid)

    def visitMethodDeclaration(self, ctx: ExprParser.MethodDeclarationContext):
        # Handle method signature (method_name, type, parameters)
        method_name = ctx.methodSignature().methodName().getText()
        return_type = ctx.methodSignature().type_().getText()
        parameters = ctx.methodSignature().parametersInit()
        
        # # Check if method already exists (to avoid redeclaration)
        # if method_name in self.symbol_table:
        #     line, col = self.get_line_info(ctx)
        #     raise Exception(f"Method '{method_name}' already declared at line {line}, column {col}.")

        param_children = list(parameters.getChildren())
        seen_params = set()
        # Iterate over parameter pairs (type, variableName)
        for i, child in enumerate(param_children):
            if isinstance(child, ExprParser.TypeContext):
                param_type = child.getText()
                param_name = param_children[i + 1].getText() if i + 1 < len(param_children) else None

                if param_name in seen_params:
                    raise Exception(f"Duplicate parameter: {param_type} {param_name} found in method '{method_name}'.")
                
                seen_params.add(param_name)
        
        # Add method to the symbol table, including its return type
        if method_name not in self.symbol_table:
            self.symbol_table[method_name] = {"type": return_type, "line": ctx.start.line}

        # Now handle method block (statements inside method)
        self.visit(ctx.methodBlock())

        # Handle return statement type validation
        return_statement = ctx.methodBlock().returnStatement()
        if return_statement:
            return_expr_type = self.visit(return_statement.expression())
            print(f"Return statement type: {return_expr_type}")
            if return_expr_type != return_type:
                line, col = self.get_line_info(return_statement)
                raise Exception(f"Type mismatch in return statement at line {line}, column {col}: expected {return_type} but got {return_expr_type}.")
    
    def visitClassDeclaration(self, ctx: ExprParser.ClassDeclarationContext):
        # Handle class name and inheritance
        class_name = ctx.className()[0].getText()
        superclass_name = None

        if len(ctx.className()) > 1:
            superclass_name = ctx.className()[1].getText()
        
        # Check if the class already exists in the symbol table
        if class_name in self.symbol_table:
            line, col = self.get_line_info(ctx)
            raise Exception(f"Class '{class_name}' already declared at line {line}, column {col}.")
        
        # Check if the class is a template (abstract class/interface)
        is_template = False
        if isinstance(ctx, ExprParser.TemplateDeclarationContext):
            is_template = True
            # Handle template-specific logic, e.g., abstract methods
            print(f"Template class '{class_name}' detected.")

        if superclass_name:
            self.inheritance_map[class_name] = superclass_name
        else:
            self.inheritance_map[class_name] = None  # No inheritance
        
        # Add class to symbol table, indicating whether it's a template (abstract class/interface)
        self.symbol_table[class_name] = {"type": "class" if not is_template else "template", "line": ctx.start.line, "is_template": is_template}

        # Add class fields (variables)
        for field in ctx.variableSignature():
            # Initialize var_type to None before the try block
            var_type = None
            var_name = None

            try:
                if hasattr(field, 'type'): # Check if we can access the type directly
                    field_type = field.type() # Access type and get text
                    if field_type:
                        var_type = field_type.getText()
                
                if hasattr(field, 'variableName'):  # Check if we can access the variableName directly
                    var_name = field.variableName().getText() # Access variable name and get text

                if var_name is not None:
                    # Handle variable existence in the symbol table
                    if var_name in self.symbol_table:
                        line, col = self.get_line_info(field)
                        raise Exception(f"Variable '{var_name}' already declared at line {line}, column {col}.")
                    self.symbol_table[var_name] = {"type": var_type, "line": ctx.start.line}

            except AttributeError as e:
                print(f"Error accessing attributes: {e}")
        
        # Add methods to symbol table
        for method in ctx.methodDeclaration():
            self.visitMethodDeclaration(method)  # Visit each method declaration

        # Handle abstract methods if this is a template (abstract class/interface)
        if is_template:
            for method in ctx.methodDeclaration():
                method_name = method.methodSignature().methodName().getText()
                # Assuming methods in templates are abstract by default
                self.symbol_table[method_name] = {"type": "abstract method", "line": method.start.line}
                print(f"Abstract method '{method_name}' in template class '{class_name}'.")

        # Visit the children of the class declaration (optional, depending on your needs)
        self.visitChildren(ctx)
    
    def visitExpression(self, ctx: ExprParser.ExpressionContext):
        # Delegate to additiveExpression, as it's the core of the expression
        return self.visit(ctx.additiveExpression())

    def visitAdditiveExpression(self, ctx: ExprParser.AdditiveExpressionContext):
        # If there is only one multiplicative expression, return its value
        if len(ctx.multiplicativeExpression()) == 1:
            return self.visit(ctx.multiplicativeExpression(0))

        # Handle compound expressions (e.g., x + y)
        left_type = self.visit(ctx.multiplicativeExpression(0))
        for i in range(1, len(ctx.multiplicativeExpression())):
            right_type = self.visit(ctx.multiplicativeExpression(i))

            # Allow implicit conversion: if one is 'chunk' and the other is 'fraction', promote 'chunk' to 'fraction'
            if left_type == 'chunk' and right_type == 'fraction':
                left_type = 'fraction'
            elif left_type == 'fraction' and right_type == 'chunk':
                right_type = 'fraction'

            if left_type != right_type:
                line, col = self.get_line_info(ctx)
                raise Exception(f"Type mismatch in additive expression at line {line}, column {col}: {left_type} and {right_type} are not the same.")
        return left_type  # Assume type consistency
    
    def visitMultiplicativeExpression(self, ctx: ExprParser.MultiplicativeExpressionContext):
        # If there is only one term, return its value
        if len(ctx.term()) == 1:
            return self.visit(ctx.term(0))

        # Handle compound expressions (e.g., x * y)
        left_type = self.visit(ctx.term(0))
        for i in range(1, len(ctx.term())):
            right_type = self.visit(ctx.term(i))

            # Allow implicit conversion: if one is 'chunk' and the other is 'fraction', promote 'chunk' to 'fraction'
            if left_type == 'chunk' and right_type == 'fraction':
                left_type = 'fraction'
            elif left_type == 'fraction' and right_type == 'chunk':
                right_type = 'fraction'

            if left_type != right_type:
                line, col = self.get_line_info(ctx)
                raise Exception(f"Type mismatch in multiplicative expression at line {line}, column {col}: {left_type} and {right_type} are not the same.")
        return left_type  # Assume type consistency

    def visitTerm(self, ctx: ExprParser.TermContext):
        # Check if the term is a variableName
        if ctx.variableName():
            var_name = ctx.variableName().getText()
            if var_name not in self.symbol_table:
                line, col = self.get_line_info(ctx)
                raise Exception(f"Variable '{var_name}' not declared at line {line}, column {col}.")
            self.markVariableAsUsed(var_name)
            return self.symbol_table[var_name]["type"]
        
        # Check if the term is a literal
        elif ctx.literal(): 
            return self.visit(ctx.literal())  
        
        # Check if the term is a classVariableAccess
        elif ctx.classVariableAccess():
            return self.visit(ctx.classVariableAccess())
        
        # Check if the term is a classMethodAccess
        elif ctx.classMethodAccess():
            return self.visit(ctx.classMethodAccess())
        
        # Check if the term is a parenthesized expression
        elif ctx.expression():
            return self.visit(ctx.expression())
        
        raise Exception(f"Unsupported term: {ctx.getText()}")

    def visitLiteral(self, ctx:ExprParser.LiteralContext):
        # Check if it's a chunkLiteral, fractionLiteral, or stringLiteral
        if ctx.ChunkLiteral():
            return 'chunk'  # Return the type for chunk literal
        elif ctx.FractionLiteral():
            return 'fraction'  # Return the type for fraction literal
        elif ctx.StringLiteral():
            return 'string'  # Return the type for string literal
        else:
            raise Exception(f"Unsupported literal: {ctx.getText()}")
    
    def visitCreateClassStatement(self, ctx: ExprParser.CreateClassStatementContext):
        try:
            class_name = ctx.className().getText()

            # Check if the class exists
            if class_name not in self.symbol_table:
                print(self.symbol_table)
                raise Exception(f"Class '{class_name}' not declared.")
            
            self.markVariableAsUsed(class_name)
            
            for variable in ctx.parametersCall().expression():
                resolved_variable = self.visit(variable)
            
            return class_name
        except Exception as e:
            raise Exception(f"Error in class creation: {e}")
    
    def visitClassMethodAccess(self, ctx: ExprParser.ClassMethodAccessContext):
        if ctx.variableName():
            var_name = ctx.variableName().getText()
            if var_name not in self.symbol_table:
                line, col = self.get_line_info(ctx)
                raise Exception(f"Variable '{var_name}' not declared at line {line}, column {col}.")
            self.markVariableAsUsed(var_name)
            return self.symbol_table[var_name]["type"]
        elif ctx.className():
            class_name = ctx.className().getText()
            if class_name not in self.symbol_table:
                line, col = self.get_line_info(ctx)
                raise Exception(f"Class '{class_name}' not declared at line {line}, column {col}.")
            return self.symbol_table[class_name][ctx.methodName().getText()]["type"]
    
    def visitClassVariableAccess(self, ctx: ExprParser.ClassVariableAccessContext):
        if ctx.variableName():
            var_name = ctx.variableName().getText()
            if var_name not in self.symbol_table:
                line, col = self.get_line_info(ctx)
                raise Exception(f"Variable '{var_name}' not declared at line {line}, column {col}.")
            self.markVariableAsUsed(var_name)
            return self.symbol_table[var_name]["type"]
        elif ctx.className():
            class_name = ctx.className().getText()
            if class_name not in self.symbol_table:
                line, col = self.get_line_info(ctx)
                raise Exception(f"Class '{class_name}' not declared at line {line}, column {col}.")
