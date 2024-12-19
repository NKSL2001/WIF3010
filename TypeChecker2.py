from antlr4 import ParseTreeVisitor
import re

class TypeChecker(ParseTreeVisitor):
    '''Perform static analysis test & error handling test.'''

    def __init__(self):
        print("init passed")

        self.symbol_table = {}  # Tracks variable names and their types
        self.used_variables = set()  # Tracks variables that are used
        self.valid_variable_pattern = re.compile(r"^[a-zA-Z_][a-zA-Z0-9_]*$")  # Regex for valid names

    def check(self, tree):
        print("check passed")

        # Start type checking from the program's root node
        self.visit(tree)
        # Check for unused variables
        for var in self.symbol_table:
            if var not in self.used_variables:
                print(f"Warning: Variable '{var}' is declared but never used.")

    def visitProgram(self, ctx):
        # Visit all statements in the program
        for statement in ctx.statement():
            self.visit(statement)

    def visitVariableDeclaration(self, ctx):
        print("variable passed")

        # Example: type int x := 5;
        var_name = ctx.variableName().getText()
        var_type = ctx.type().getText()
        # Check for invalid variable names
        if not self.valid_variable_pattern.match(var_name):
            raise Exception(f"Invalid variable name: '{var_name}'. Variable names must start with a letter or underscore and contain only alphanumeric characters.")
        # Check for redeclaration
        if var_name in self.symbol_table:
            raise Exception(f"Variable '{var_name}' already declared.")
        # Add to symbol table
        self.symbol_table[var_name] = var_type

        # Check the initializer expression or class creation
        initializer = ctx.expression() or ctx.createClassStatement()
        if initializer:
            init_type = self.visit(initializer)
            if init_type != var_type:
                raise Exception(f"Type mismatch: Cannot assign {init_type} to {var_type}.")

    def visitAssignment(self, ctx):
        print("assignment passed")

        # Example: x := 5;
        var_name = ctx.variableName().getText()
        if var_name not in self.symbol_table:
            raise Exception(f"Variable '{var_name}' not declared.")
        self.used_variables.add(var_name)  # Mark variable as used
        expr_type = self.visit(ctx.expression())
        if self.symbol_table[var_name] != expr_type:
            raise Exception(f"Type mismatch: Cannot assign {expr_type} to {self.symbol_table[var_name]}.")

    def visitExpression(self, ctx):
        print("expression passed")

        # Check if this is a binary operation like x + y
        if ctx.additiveExpression():
            left_type = self.visit(ctx.left)
            right_type = self.visit(ctx.right)
            if left_type != right_type:
                raise Exception("Type mismatch in binary expression.")
            return left_type  # Assume the operation preserves type

        # Handle single IDENTIFIER or literal
        if ctx.variableName():
            var_name = ctx.variableName().getText()
            if var_name not in self.symbol_table:
                raise Exception(f"Variable '{var_name}' not declared.")
            self.used_variables.add(var_name)  # Mark the variable as used
            return self.symbol_table[var_name]  # Return the variable's type

        elif ctx.literal():
            return self.visit(ctx.literal())

        # Handle classVariableAccess
        elif ctx.classVariableAccess():
            return self.visit(ctx.classVariableAccess())

        # Handle classMethodAccess
        elif ctx.classMethodAccess():
            return self.visit(ctx.classMethodAccess())

        # Default case (e.g., unsupported expressions)
        raise Exception(f"Unsupported expression: {ctx.getText()}")

    def visitClassDeclaration(self, ctx):
        print("class passed")

        # Example: class MyClass { ... }
        class_name = ctx.className().getText()
        if class_name in self.class_definitions:
            raise Exception(f"Class '{class_name}' already declared.")

        self.class_definitions[class_name] = {
            'variables': {},
            'methods': {}
        }

        # Process class variables
        for var in ctx.variableSignature():
            var_name = var.variableName().getText()
            var_type = var.type().getText()
            self.class_definitions[class_name]['variables'][var_name] = var_type

        # Process methods
        for method in ctx.methodDeclaration():
            method_name = method.methodName().getText()
            if method_name in self.class_definitions[class_name]['methods']:
                raise Exception(f"Method '{method_name}' already declared in class '{class_name}'.")
            self.class_definitions[class_name]['methods'][method_name] = method

    def visitClassVariableAccess(self, ctx):
        print("class variable passed")

        # Example: myClass.myVar
        class_or_var = ctx.className() or ctx.variableName()
        class_name = class_or_var.getText()
        if class_name not in self.class_definitions:
            raise Exception(f"Class '{class_name}' not declared.")
        var_name = ctx.variableName().getText()
        if var_name not in self.class_definitions[class_name]['variables']:
            raise Exception(f"Variable '{var_name}' not found in class '{class_name}'.")
        return self.class_definitions[class_name]['variables'][var_name]

    def visitClassMethodAccess(self, ctx):
        print("class method passed")

        # Example: myClass.myMethod(param1, param2)
        class_or_var = ctx.className() or ctx.variableName()
        class_name = class_or_var.getText()
        if class_name not in self.class_definitions:
            raise Exception(f"Class '{class_name}' not declared.")
        method_name = ctx.methodName().getText()
        if method_name not in self.class_definitions[class_name]['methods']:
            raise Exception(f"Method '{method_name}' not found in class '{class_name}'.")
        # Further validation for method parameters can be added here
        return self.class_definitions[class_name]['methods'][method_name].type()
    
    def visitLiteral(self, ctx):
        # Handle literals and return their type
        if ctx.chunkLiteral():
            return "chunk"
        elif ctx.fractionLiteral():
            return "fraction"
        elif ctx.stringLiteral():
            return "string"
        raise Exception(f"Unknown literal type: {ctx.getText()}")

    def visitCreateClassStatement(self, ctx):
        # Example: new MyClass($x, $y)
        class_name = ctx.className().getText()
        if class_name not in self.class_definitions:
            raise Exception(f"Class '{class_name}' not declared.")
        return class_name

    def visitShowStatement(self, ctx):
        # Example: show $x!
        expr_type = self.visit(ctx.expression())
        print(f"Show: {ctx.expression().getText()} (type: {expr_type})")

    def visitChildren(self, node):
        print("visit child fallback")

        # Default implementation: Visit all children
        for child in node.getChildren():
            self.visit(child)
