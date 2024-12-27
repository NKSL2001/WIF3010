from TypeCheckerParser import TypeCheckerParser as ExprParser
from TypeCheckerVisitor import TypeCheckerVisitor as ExprVisitor
from collections import defaultdict


class SymbolTable:
    def __init__(self):
        self.global_scope = defaultdict(lambda: defaultdict(lambda: dict))
        self.class_scopes = defaultdict(
            lambda: defaultdict(lambda: defaultdict(lambda: dict))
        )  # Track class scopes
        self.method_scopes = defaultdict(
            lambda: defaultdict(lambda: defaultdict(lambda: dict))
        )  # Track method scopes
        self.scope_stack = []  # Track the current scope stack

    def enter_scope(self, class_name=None, method_name=None):
        """Enter a new scope (class or method)"""

        # Validate if class or method exists
        if method_name and method_name not in self.method_scopes:
            if self.current_scope()[0]:
                if f"{self.current_scope()[0]}.{method_name}" in self.method_scopes:
                    class_name = self.current_scope()[0]
                else:
                    raise Exception(
                        f"Method '{method_name}' not found in symbol table."
                    )
            else:
                raise Exception(f"Method '{method_name}' not found in symbol table.")
        if class_name and class_name not in self.class_scopes:
            raise Exception(f"Class '{class_name}' not found in symbol table.")

        self.scope_stack.append((class_name, method_name))

    def exit_scope(self):
        """Exit the current scope"""
        self.scope_stack.pop()

    def current_scope(self):
        """Get the current scope"""
        return self.scope_stack[-1] if self.scope_stack else (None, None)

    # adding variable to scope
    def add_to_scope(self, var_name, var_type, line):
        """Add variable to the current scope"""
        class_name, method_name = self.current_scope()

        # Check if we're in a method scope
        if method_name:
            if self.current_scope()[0]:
                method_name = f"{self.current_scope()[0]}.{method_name}"
            self.add_to_method_scope(method_name, var_name, var_type, line)
            return

        # Check if we're in a class scope
        if class_name:
            self.add_to_class_scope(class_name, var_name, var_type, line)

        self.add_to_global_scope(var_name, var_type, line)

    def add_to_global_scope(self, var_name, var_type, line):
        """Add variable to global scope"""
        self.global_scope[var_name]["type"] = var_type
        self.global_scope[var_name]["line"] = line

    def add_to_class_scope(self, class_name, var_name, var_type, line):
        """Add variable to a specific class scope"""
        self.class_scopes[class_name][var_name]["type"] = var_type
        self.class_scopes[class_name][var_name]["line"] = line

    def add_to_method_scope(self, method_name, var_name, var_type, line):
        """Add variable to a specific method scope"""
        self.method_scopes[method_name][var_name]["type"] = var_type
        self.method_scopes[method_name][var_name]["line"] = line

    # end adding variable to scope

    # add class and method to symbol table
    def add_class(self, class_name, line, is_template):
        """Add class to the symbol table"""
        self.class_scopes[class_name] = defaultdict(dict)
        self.class_scopes[class_name]["line"] = line
        self.class_scopes[class_name]["is_template"] = is_template

    def add_method(self, method_name, return_type, line, class_name=None):
        """Add method to the symbol table"""
        method_info = defaultdict(dict)
        method_info["return_type"] = return_type
        method_info["line"] = line

        # if provide class name
        if class_name and class_name in self.class_scopes:
            method_name = f"{class_name}.{method_name}"
            method_info["from_class"] = class_name
        # if not provide class name, but current scope is in class
        elif (
            self.current_scope()[0] is not None
            and self.current_scope()[0] in self.class_scopes
        ):
            method_name = f"{self.current_scope()[0]}.{method_name}"
            method_info["from_class"] = self.current_scope()[0]

        self.method_scopes[method_name] = method_info

    def get_current_class(self):
        """Get the current class name"""
        if self.current_scope()[0] is None:
            return None
        return self.get_class(self.current_scope()[0])

    def get_class(self, class_name):
        """Get the class by name"""
        return self.class_scopes[class_name]

    def get_current_method(self):
        """Get the current method name"""
        class_name, method_name = self.current_scope()
        if method_name is None:
            return None
        return self.get_method(class_name, method_name)

    def get_method(self, class_name, method_name):
        """Get the method by name"""
        if class_name is not None:
            return self.method_scopes[f"{class_name}.{method_name}"]
        return self.method_scopes[method_name]

    # end add class and method to symbol table

    def get_var_type(self, var_name):
        """Get the variable type from the current scope stack (method -> class -> global)"""
        class_name, method_name = self.current_scope()

        # Check method scope first
        if method_name:
            # visit class name first
            if class_name and f"{class_name}.{method_name}" in self.method_scopes:
                method_name = f"{class_name}.{method_name}"

            if (
                method_name in self.method_scopes
                and var_name in self.method_scopes[method_name]
            ):
                return self.method_scopes[method_name][var_name]["type"]

        # Check class scope next
        if (
            class_name
            and class_name in self.class_scopes
            and var_name in self.class_scopes[class_name]
        ):
            return self.class_scopes[class_name][var_name]["type"]

        # Fallback to global scope
        if var_name in self.global_scope:
            return self.global_scope[var_name]["type"]

        return None  # Variable not found

    def set_var_used(self, var_name):
        """Mark a variable as used"""
        class_name, method_name = self.current_scope()

        # Check method scope first
        if (
            method_name
            and method_name in self.method_scopes
            and var_name in self.method_scopes[method_name]
        ):
            self.method_scopes[method_name][var_name]["used"] = True
            return

        # Check class scope next
        if (
            class_name
            and class_name in self.class_scopes
            and var_name in self.class_scopes[class_name]
        ):
            self.class_scopes[class_name][var_name]["used"] = True
            return

        # Fallback to global scope
        if var_name in self.global_scope:
            self.global_scope[var_name]["used"] = True

    def __contains__(self, var_name):
        if self.get_var_type(var_name):
            return True
        return False

    def items(self):
        vars = {}
        for var_name, var_info in self.global_scope.items():
            if var_name.startswith("$"):
                vars[var_name] = var_info
        for cls in self.class_scopes.values():
            for var_name, var_info in cls.items():
                if var_name.startswith("$"):
                    vars[var_name] = var_info
        for method in self.method_scopes.values():
            for var_name, var_info in method.items():
                if var_name.startswith("$"):
                    vars[var_name] = var_info
        return vars.items()

    def __str__(self):
        return f"Global scope: {self.global_scope}\nClass scopes: {self.class_scopes}\nMethod scopes: {self.method_scopes}\nCurrent scope: {self.current_scope()}"


class TypeChecker(ExprVisitor):
    def __init__(self):
        self.symbol_table = SymbolTable()  # Tracks variable names and their types
        self.used_variables = set()  # Tracks variables that are used

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
        if declared_type in self.symbol_table.class_scopes:
            current_type = expr_type
            while current_type is not None:
                if current_type == declared_type:
                    return True
                current_type = self.symbol_table.get_class(current_type).get(
                    "superclass", None
                )

        # If not compatible, return False
        return False

    def visitProgram(self, ctx: ExprParser.ProgramContext):
        # Visit all statements in the program
        for statement in ctx.statement():
            self.visit(statement)

        # Check for unused variables after visiting the whole program
        print(self.used_variables)
        for var, info in self.symbol_table.items():
            if var not in self.used_variables:
                line = info["line"]
                print(
                    f"Warning: Variable '{var}' declared at line {line} is declared but never used."
                )

    def visitShowStatement(self, ctx: ExprParser.ShowStatementContext):
        # Evaluate the expression
        expr_type = self.visit(ctx.expression())

        # Get the line and column for better error messages
        line, col = self.get_line_info(ctx)

        # Validate the type
        if expr_type == "none":
            raise Exception(f"Cannot show a 'none' value at line {line}, column {col}.")

        # Print the evaluated value (as a placeholder for actual execution)
        print(f"Output: {expr_type}")

    def visitVariableDeclaration(self, ctx: ExprParser.VariableDeclarationContext):
        # The variable signature is part of the variable declaration
        var_signature = ctx.variableSignature()

        # Extract the variable name and type from the signature
        var_name = var_signature.variableName().getText()
        var_type = var_signature.type_().getText()  # The declared type of the variable

        # Get line number for better error messages
        line, col = self.get_line_info(ctx)

        # Check for redeclaration of the variable
        if var_name in self.symbol_table:
            raise Exception(f"Variable '{var_name}' already declared.")

        # Add the variable to the symbol table with its declared type and the line number
        self.symbol_table.add_to_scope(var_name, var_type, line)

        # Check the initializer expression for type mismatch
        initializer = (
            ctx.expression() or ctx.createClassStatement()
        )  # Check if there's an initializer expression

        if initializer:
            init_type = self.visit(initializer)  # Visit the initializer to get its type
            if init_type != var_type:
                raise Exception(
                    f"Type mismatch: Cannot assign {init_type} to {var_type} for variable '{var_name}' at line {line}, column {col}."
                )

    def visitAssignment(self, ctx: ExprParser.AssignmentContext):
        # Extract the variable name from the assignment
        var_name = ctx.variableName().getText()

        # Get line number for better error messages
        line, col = self.get_line_info(ctx)

        # Check if the variable has been declared
        if var_name not in self.symbol_table:
            raise Exception(
                f"Variable '{var_name}' not declared at line {line}, column {col}."
            )

        # Mark the variable as used
        self.used_variables.add(var_name)

        # Get the type of the variable from the symbol table
        declared_type = self.symbol_table.get_var_type(var_name)

        # Visit the assigned expression to determine its type
        expr_type = self.visit(ctx.expression())

        # Check for type compatibility: if declared type is a class type, check inheritance
        if not self.is_type_compatible(declared_type, expr_type):
            raise Exception(
                f"Type mismatch: Cannot assign {expr_type} to {declared_type} for variable '{var_name}' at line {line}, column {col}."
            )

        # If types are compatible, continue (assignment is valid)

    def visitMethodDeclaration(self, ctx: ExprParser.MethodDeclarationContext):
        # Handle method signature (method_name, type, parameters)
        method_name = ctx.methodSignature().methodName().getText()
        return_type = ctx.methodSignature().type_().getText()
        parameters = ctx.methodSignature().parametersInit()

        # Add method to the symbol table, including its return type
        self.symbol_table.add_method(method_name, return_type, ctx.start.line)

        # Enter method scope to add variables to correct scope
        self.symbol_table.enter_scope(method_name=method_name)

        # Iterate over parameter pairs (type, variableName)
        for param_type, param_name in zip(
            parameters.type_(), parameters.variableName()
        ):
            self.symbol_table.add_to_scope(
                param_name.getText(), param_type.getText(), ctx.start.line
            )

        # Now handle method block (statements inside method)
        self.visit(ctx.methodBlock())

        # Handle return statement type validation
        return_statement = ctx.methodBlock().returnStatement()
        if return_statement:
            return_expr_type = self.visit(return_statement.expression())
            print(f"Return statement type: {return_expr_type}")
            if return_expr_type != return_type:
                line, col = self.get_line_info(return_statement)
                raise Exception(
                    f"Type mismatch in return statement at line {line}, column {col}: expected {return_type} but got {return_expr_type}."
                )

        self.symbol_table.exit_scope()

    def visitClassDeclaration(self, ctx: ExprParser.ClassDeclarationContext):
        # Handle class name and inheritance
        class_name = ctx.className()[0].getText()
        superclass_name = None

        if len(ctx.className()) > 1:
            superclass_name = ctx.className()[1].getText()

        # Check if the class already exists in the symbol table
        if class_name in self.symbol_table.class_scopes:
            line, col = self.get_line_info(ctx)
            raise Exception(
                f"Class '{class_name}' already declared at line {line}, column {col}."
            )

        # Check if the class is a template (abstract class/interface)
        is_template = False
        if isinstance(ctx, ExprParser.TemplateDeclarationContext):
            is_template = True
            # Handle template-specific logic, e.g., abstract methods
            print(f"Template class '{class_name}' detected.")

        # Add class to symbol table, indicating whether it's a template (abstract class/interface)
        self.symbol_table.add_class(class_name, ctx.start.line, is_template)

        self.symbol_table.enter_scope(class_name=class_name)

        self.symbol_table.get_current_class()["superclass"] = superclass_name

        # Add class fields (variables)
        for field in ctx.variableSignature():
            # Initialize var_type to None before the try block
            var_type = field.type_().getText()
            var_name = field.variableName().getText()

            if var_name is not None:
                # Handle variable existence in the symbol table
                if var_name in self.symbol_table:
                    line, col = self.get_line_info(field)
                    raise Exception(
                        f"Variable '{var_name}' already declared at line {line}, column {col}."
                    )
                self.symbol_table.add_to_scope(var_name, var_type, field.start.line)

        # Add methods to symbol table
        for method in ctx.methodDeclaration():
            self.visitMethodDeclaration(method)  # Visit each method declaration

        # Handle abstract methods if this is a template (abstract class/interface)
        if is_template:
            for method in ctx.methodDeclaration():
                method_name = method.methodSignature().methodName().getText()
                # Assuming methods in templates are abstract by default
                method_info = self.symbol_table.get_method(class_name, method_name)
                method_info["type"] = "abstract method"
                print(
                    f"Abstract method '{method_name}' in template class '{class_name}'."
                )

        # Visit the children of the class declaration (optional, depending on your needs)
        # self.visitChildren(ctx)

        self.symbol_table.exit_scope()

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
            if left_type == "chunk" and right_type == "fraction":
                left_type = "fraction"
            elif left_type == "fraction" and right_type == "chunk":
                right_type = "fraction"

            if left_type != right_type:
                line, col = self.get_line_info(ctx)
                raise Exception(
                    f"Type mismatch in additive expression at line {line}, column {col}: {left_type} and {right_type} are not the same."
                )
        return left_type  # Assume type consistency

    def visitMultiplicativeExpression(
        self, ctx: ExprParser.MultiplicativeExpressionContext
    ):
        # If there is only one term, return its value
        if len(ctx.term()) == 1:
            return self.visit(ctx.term(0))

        # Handle compound expressions (e.g., x * y)
        left_type = self.visit(ctx.term(0))
        for i in range(1, len(ctx.term())):
            right_type = self.visit(ctx.term(i))

            # Allow implicit conversion: if one is 'chunk' and the other is 'fraction', promote 'chunk' to 'fraction'
            if left_type == "chunk" and right_type == "fraction":
                left_type = "fraction"
            elif left_type == "fraction" and right_type == "chunk":
                right_type = "fraction"

            if left_type != right_type:
                line, col = self.get_line_info(ctx)
                raise Exception(
                    f"Type mismatch in multiplicative expression at line {line}, column {col}: {left_type} and {right_type} are not the same."
                )
        return left_type  # Assume type consistency

    def visitTerm(self, ctx: ExprParser.TermContext):
        # Check if the term is a variableName
        if ctx.variableName():
            var_name = ctx.variableName().getText()
            if var_name not in self.symbol_table:
                print(self.symbol_table)
                line, col = self.get_line_info(ctx)
                raise Exception(
                    f"Variable '{var_name}' not declared at line {line}, column {col}."
                )
            self.markVariableAsUsed(var_name)
            return self.symbol_table.get_var_type(var_name)

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

    def visitLiteral(self, ctx: ExprParser.LiteralContext):
        # Check if it's a chunkLiteral, fractionLiteral, or stringLiteral
        if ctx.ChunkLiteral():
            return "chunk"  # Return the type for chunk literal
        elif ctx.FractionLiteral():
            return "fraction"  # Return the type for fraction literal
        elif ctx.StringLiteral():
            return "string"  # Return the type for string literal
        else:
            raise Exception(f"Unsupported literal: {ctx.getText()}")

    def visitCreateClassStatement(self, ctx: ExprParser.CreateClassStatementContext):
        try:
            class_name = ctx.className().getText()

            # Check if the class exists
            if class_name not in self.symbol_table.class_scopes:
                print(self.symbol_table)
                raise Exception(f"Class '{class_name}' not declared.")

            for variable in ctx.parametersCall().expression():
                resolved_variable = self.visit(variable)

            return class_name
        except Exception as e:
            raise Exception(f"Error in class creation: {e}")

    def visitClassMethodAccess(self, ctx: ExprParser.ClassMethodAccessContext):
        method_name = ctx.methodName().getText()

        # try to find class
        class_name = None
        if ctx.variableName():
            var_name = ctx.variableName().getText()
            if var_name not in self.symbol_table:
                line, col = self.get_line_info(ctx)
                raise Exception(
                    f"Variable '{var_name}' not declared at line {line}, column {col}."
                )
            self.markVariableAsUsed(var_name)
            class_name = self.symbol_table.get_var_type(var_name)
        elif ctx.className():
            class_name = ctx.className().getText()

        if class_name not in self.symbol_table.class_scopes:
            line, col = self.get_line_info(ctx)
            raise Exception(
                f"Class '{class_name}' not declared at line {line}, column {col}."
            )

        for variable in ctx.parametersCall().expression():
            resolved_variable = self.visit(variable)

        return self.symbol_table.get_method(class_name, method_name)["return_type"]

    def visitClassVariableAccess(self, ctx: ExprParser.ClassVariableAccessContext):
        access_name = ctx.accessedVariableName().getText()

        if ctx.variableName():
            var_name = ctx.variableName().getText()
            if var_name not in self.symbol_table:
                line, col = self.get_line_info(ctx)
                raise Exception(
                    f"Variable '{var_name}' not declared at line {line}, column {col}."
                )
            self.markVariableAsUsed(var_name)
            class_name = self.symbol_table.get_var_type(var_name)
        elif ctx.className():
            class_name = ctx.className().getText()
            if class_name not in self.symbol_table.class_scopes:
                line, col = self.get_line_info(ctx)
                raise Exception(
                    f"Class '{class_name}' not declared at line {line}, column {col}."
                )

        return self.symbol_table.get_class(class_name)[access_name]["type"]
