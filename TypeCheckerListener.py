# Generated from TypeChecker.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TypeCheckerParser import TypeCheckerParser
else:
    from TypeCheckerParser import TypeCheckerParser

# This class defines a complete listener for a parse tree produced by TypeCheckerParser.
class TypeCheckerListener(ParseTreeListener):

    # Enter a parse tree produced by TypeCheckerParser#program.
    def enterProgram(self, ctx:TypeCheckerParser.ProgramContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#program.
    def exitProgram(self, ctx:TypeCheckerParser.ProgramContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#statement.
    def enterStatement(self, ctx:TypeCheckerParser.StatementContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#statement.
    def exitStatement(self, ctx:TypeCheckerParser.StatementContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#showStatement.
    def enterShowStatement(self, ctx:TypeCheckerParser.ShowStatementContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#showStatement.
    def exitShowStatement(self, ctx:TypeCheckerParser.ShowStatementContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#returnStatement.
    def enterReturnStatement(self, ctx:TypeCheckerParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#returnStatement.
    def exitReturnStatement(self, ctx:TypeCheckerParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#createClassStatement.
    def enterCreateClassStatement(self, ctx:TypeCheckerParser.CreateClassStatementContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#createClassStatement.
    def exitCreateClassStatement(self, ctx:TypeCheckerParser.CreateClassStatementContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#variableSignature.
    def enterVariableSignature(self, ctx:TypeCheckerParser.VariableSignatureContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#variableSignature.
    def exitVariableSignature(self, ctx:TypeCheckerParser.VariableSignatureContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:TypeCheckerParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:TypeCheckerParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#assignment.
    def enterAssignment(self, ctx:TypeCheckerParser.AssignmentContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#assignment.
    def exitAssignment(self, ctx:TypeCheckerParser.AssignmentContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#parametersInit.
    def enterParametersInit(self, ctx:TypeCheckerParser.ParametersInitContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#parametersInit.
    def exitParametersInit(self, ctx:TypeCheckerParser.ParametersInitContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#methodSignature.
    def enterMethodSignature(self, ctx:TypeCheckerParser.MethodSignatureContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#methodSignature.
    def exitMethodSignature(self, ctx:TypeCheckerParser.MethodSignatureContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:TypeCheckerParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:TypeCheckerParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#methodBlock.
    def enterMethodBlock(self, ctx:TypeCheckerParser.MethodBlockContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#methodBlock.
    def exitMethodBlock(self, ctx:TypeCheckerParser.MethodBlockContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#classDeclaration.
    def enterClassDeclaration(self, ctx:TypeCheckerParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#classDeclaration.
    def exitClassDeclaration(self, ctx:TypeCheckerParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#templateDeclaration.
    def enterTemplateDeclaration(self, ctx:TypeCheckerParser.TemplateDeclarationContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#templateDeclaration.
    def exitTemplateDeclaration(self, ctx:TypeCheckerParser.TemplateDeclarationContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#parametersCall.
    def enterParametersCall(self, ctx:TypeCheckerParser.ParametersCallContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#parametersCall.
    def exitParametersCall(self, ctx:TypeCheckerParser.ParametersCallContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#classVariableAccess.
    def enterClassVariableAccess(self, ctx:TypeCheckerParser.ClassVariableAccessContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#classVariableAccess.
    def exitClassVariableAccess(self, ctx:TypeCheckerParser.ClassVariableAccessContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#classMethodAccess.
    def enterClassMethodAccess(self, ctx:TypeCheckerParser.ClassMethodAccessContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#classMethodAccess.
    def exitClassMethodAccess(self, ctx:TypeCheckerParser.ClassMethodAccessContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#accessedVariableName.
    def enterAccessedVariableName(self, ctx:TypeCheckerParser.AccessedVariableNameContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#accessedVariableName.
    def exitAccessedVariableName(self, ctx:TypeCheckerParser.AccessedVariableNameContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#expression.
    def enterExpression(self, ctx:TypeCheckerParser.ExpressionContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#expression.
    def exitExpression(self, ctx:TypeCheckerParser.ExpressionContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:TypeCheckerParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:TypeCheckerParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:TypeCheckerParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:TypeCheckerParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#term.
    def enterTerm(self, ctx:TypeCheckerParser.TermContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#term.
    def exitTerm(self, ctx:TypeCheckerParser.TermContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#type.
    def enterType(self, ctx:TypeCheckerParser.TypeContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#type.
    def exitType(self, ctx:TypeCheckerParser.TypeContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#variableName.
    def enterVariableName(self, ctx:TypeCheckerParser.VariableNameContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#variableName.
    def exitVariableName(self, ctx:TypeCheckerParser.VariableNameContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#className.
    def enterClassName(self, ctx:TypeCheckerParser.ClassNameContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#className.
    def exitClassName(self, ctx:TypeCheckerParser.ClassNameContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#methodName.
    def enterMethodName(self, ctx:TypeCheckerParser.MethodNameContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#methodName.
    def exitMethodName(self, ctx:TypeCheckerParser.MethodNameContext):
        pass


    # Enter a parse tree produced by TypeCheckerParser#literal.
    def enterLiteral(self, ctx:TypeCheckerParser.LiteralContext):
        pass

    # Exit a parse tree produced by TypeCheckerParser#literal.
    def exitLiteral(self, ctx:TypeCheckerParser.LiteralContext):
        pass



del TypeCheckerParser