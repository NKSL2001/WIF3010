Updated Symbol Table
We will modify the symbol table to handle multiple scopes (class, method, global) without needing to pass the method_name or class_name explicitly.

python
复制代码
class SymbolTable:
    def __init__(self):
        self.global_scope = {}
        self.class_scopes = {}  # Track class scopes
        self.method_scopes = {}  # Track method scopes
        self.scope_stack = []    # Track the current scope stack
    
    def enter_scope(self, class_name=None, method_name=None):
        """Enter a new scope (class or method)"""
        self.scope_stack.append((class_name, method_name))
    
    def exit_scope(self):
        """Exit the current scope"""
        self.scope_stack.pop()
    
    def add_to_global_scope(self, var_name, var_type):
        """Add variable to global scope"""
        self.global_scope[var_name] = var_type
    
    def add_to_class_scope(self, class_name, var_name, var_type):
        """Add variable to a specific class scope"""
        if class_name not in self.class_scopes:
            self.class_scopes[class_name] = {}
        self.class_scopes[class_name][var_name] = var_type
    
    def add_to_method_scope(self, method_name, var_name, var_type):
        """Add variable to a specific method scope"""
        if method_name not in self.method_scopes:
            self.method_scopes[method_name] = {}
        self.method_scopes[method_name][var_name] = var_type
    
    def get_var_type(self, var_name):
        """Get the variable type from the current scope stack (class -> method -> global)"""
        class_name, method_name = self.scope_stack[-1] if self.scope_stack else (None, None)

        # Check class scope first
        if class_name and class_name in self.class_scopes and var_name in self.class_scopes[class_name]:
            return self.class_scopes[class_name][var_name]
        
        # Check method scope next
        if method_name and method_name in self.method_scopes and var_name in self.method_scopes[method_name]:
            return self.method_scopes[method_name][var_name]
        
        # Fallback to global scope
        if var_name in self.global_scope:
            return self.global_scope[var_name]
        
        return None  # Variable not found
Updated Visitor Methods
visitClassDeclaration: When entering a class, push the class context onto the stack.
python
复制代码
def visitClassDeclaration(self, ctx: ExprParser.ClassDeclarationContext):
    class_name = ctx.className().getText()
    
    # Enter class scope
    self.symbol_table.enter_scope(class_name=class_name)
    
    # Add class-level variables
    for var_decl in ctx.variableDeclaration():
        var_name = var_decl.variableName().getText()
        var_type = var_decl.type().getText()
        self.symbol_table.add_to_class_scope(class_name, var_name, var_type)
    
    # Add class methods
    for method_decl in ctx.methodDeclaration():
        self.visitMethodDeclaration(method_decl)
    
    # Exit class scope
    self.symbol_table.exit_scope()
    
    # Continue to the body of the class
    self.visitChildren(ctx)
visitMethodDeclaration: When visiting a method declaration, push the method context onto the stack, including the class name if inside a class.
python
复制代码
def visitMethodDeclaration(self, ctx: ExprParser.MethodDeclarationContext):
    # Get class name (if any) and method name
    class_name = self.symbol_table.scope_stack[-1][0]  # Class name from the current scope
    method_name = ctx.methodSignature().methodName().getText()
    
    # Enter method scope
    self.symbol_table.enter_scope(class_name=class_name, method_name=method_name)
    
    # Add method parameters to the method scope
    for param in ctx.methodSignature().parametersInit().typeVariable():
        param_name = param.variableName().getText()
        param_type = param.type().getText()
        self.symbol_table.add_to_method_scope(method_name, param_name, param_type)
    
    # Visit the method block
    self.visitMethodBlock(ctx.methodBlock())
    
    # Exit method scope
    self.symbol_table.exit_scope()
visitMethodBlock: This method now relies on the context stack and doesn't need to explicitly pass method_name.
python
复制代码
def visitMethodBlock(self, ctx: ExprParser.MethodBlockContext):
    for statement in ctx.statement():
        self.visitStatement(statement)
visitStatement: Propagate the current scope context to the assignment handler.
python
复制代码
def visitStatement(self, ctx: ExprParser.StatementContext):
    if isinstance(ctx, ExprParser.AssignmentContext):
        self.visitAssignment(ctx)
    # Handle other statement types as needed
visitAssignment: Check if the variable exists in the current scope (based on the class, method, or global).
python
复制代码
def visitAssignment(self, ctx: ExprParser.AssignmentContext):
    var_name = ctx.variableName().getText()
    expression_type = self.visit(ctx.expression())
    
    # Check variable type in the current scope
    var_type = self.symbol_table.get_var_type(var_name)
    
    if var_type is None:
        raise Exception(f"Variable '{var_name}' not declared in the current scope.")
    
    # Type checking: ensure the assigned value matches the variable type
    if var_type != expression_type:
        raise Exception(f"Type mismatch: cannot assign {expression_type} to {var_type}")
Summary
Scope Management: You no longer need to pass method_name or class_name explicitly. The SymbolTable class uses the current context stack to manage scopes dynamically.

Entering and Exiting Scopes: The enter_scope and exit_scope methods allow you to track when you enter or leave a class or method scope.

Type Checking: The visitAssignment method uses the current scope context to look up variable types and perform type checking.

This approach makes it easier to manage nested scopes and eliminates the need to manually pass method or class names across your visitor methods. It also provides a more scalable and flexible way to handle scopes for a larger program.



