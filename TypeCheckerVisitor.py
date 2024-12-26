# Generated from TypeChecker.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TypeCheckerParser import TypeCheckerParser
else:
    from TypeCheckerParser import TypeCheckerParser

# This class defines a complete generic visitor for a parse tree produced by TypeCheckerParser.

class TypeCheckerVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TypeCheckerParser#program.
    def visitProgram(self, ctx:TypeCheckerParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#statement.
    def visitStatement(self, ctx:TypeCheckerParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#showStatement.
    def visitShowStatement(self, ctx:TypeCheckerParser.ShowStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#returnStatement.
    def visitReturnStatement(self, ctx:TypeCheckerParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#createClassStatement.
    def visitCreateClassStatement(self, ctx:TypeCheckerParser.CreateClassStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#variableSignature.
    def visitVariableSignature(self, ctx:TypeCheckerParser.VariableSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:TypeCheckerParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#assignment.
    def visitAssignment(self, ctx:TypeCheckerParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#parametersInit.
    def visitParametersInit(self, ctx:TypeCheckerParser.ParametersInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#methodSignature.
    def visitMethodSignature(self, ctx:TypeCheckerParser.MethodSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#methodDeclaration.
    def visitMethodDeclaration(self, ctx:TypeCheckerParser.MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#methodBlock.
    def visitMethodBlock(self, ctx:TypeCheckerParser.MethodBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#classDeclaration.
    def visitClassDeclaration(self, ctx:TypeCheckerParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#templateDeclaration.
    def visitTemplateDeclaration(self, ctx:TypeCheckerParser.TemplateDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#parametersCall.
    def visitParametersCall(self, ctx:TypeCheckerParser.ParametersCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#classVariableAccess.
    def visitClassVariableAccess(self, ctx:TypeCheckerParser.ClassVariableAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#classMethodAccess.
    def visitClassMethodAccess(self, ctx:TypeCheckerParser.ClassMethodAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#expression.
    def visitExpression(self, ctx:TypeCheckerParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:TypeCheckerParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:TypeCheckerParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#term.
    def visitTerm(self, ctx:TypeCheckerParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#type.
    def visitType(self, ctx:TypeCheckerParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#variableName.
    def visitVariableName(self, ctx:TypeCheckerParser.VariableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#className.
    def visitClassName(self, ctx:TypeCheckerParser.ClassNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#methodName.
    def visitMethodName(self, ctx:TypeCheckerParser.MethodNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeCheckerParser#literal.
    def visitLiteral(self, ctx:TypeCheckerParser.LiteralContext):
        return self.visitChildren(ctx)



del TypeCheckerParser