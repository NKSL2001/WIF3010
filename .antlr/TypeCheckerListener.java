// Generated from c:/WIF3010-TypeChecker/TypeChecker.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link TypeCheckerParser}.
 */
public interface TypeCheckerListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link TypeCheckerParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(TypeCheckerParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link TypeCheckerParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(TypeCheckerParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link TypeCheckerParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(TypeCheckerParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link TypeCheckerParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(TypeCheckerParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link TypeCheckerParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void enterShowStatement(TypeCheckerParser.ShowStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link TypeCheckerParser#showStatement}.
	 * @param ctx the parse tree
	 */
	void exitShowStatement(TypeCheckerParser.ShowStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link TypeCheckerParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void enterReturnStatement(TypeCheckerParser.ReturnStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link TypeCheckerParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void exitReturnStatement(TypeCheckerParser.ReturnStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link TypeCheckerParser#createClassStatement}.
	 * @param ctx the parse tree
	 */
	void enterCreateClassStatement(TypeCheckerParser.CreateClassStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link TypeCheckerParser#createClassStatement}.
	 * @param ctx the parse tree
	 */
	void exitCreateClassStatement(TypeCheckerParser.CreateClassStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link TypeCheckerParser#variableSignature}.
	 * @param ctx the parse tree
	 */
	void enterVariableSignature(TypeCheckerParser.VariableSignatureContext ctx);
	/**
	 * Exit a parse tree produced by {@link TypeCheckerParser#variableSignature}.
	 * @param ctx the parse tree
	 */
	void exitVariableSignature(TypeCheckerParser.VariableSignatureContext ctx);
	/**
	 * Enter a parse tree produced by {@link TypeCheckerParser#variableDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterVariableDeclaration(TypeCheckerParser.VariableDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link TypeCheckerParser#variableDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitVariableDeclaration(TypeCheckerParser.VariableDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link TypeCheckerParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(TypeCheckerParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link TypeCheckerParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(TypeCheckerParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link TypeCheckerParser#parametersInit}.
	 * @param ctx the parse tree
	 */
	void enterParametersInit(TypeCheckerParser.ParametersInitContext ctx);
	/**
	 * Exit a parse tree produced by {@link TypeCheckerParser#parametersInit}.
	 * @param ctx the parse tree
	 */
	void exitParametersInit(TypeCheckerParser.ParametersInitContext ctx);
	/**
	 * Enter a parse tree produced by {@link TypeCheckerParser#methodSignature}.
	 * @param ctx the parse tree
	 */
	void enterMethodSignature(TypeCheckerParser.MethodSignatureContext ctx);
	/**
	 * Exit a parse tree produced by {@link TypeCheckerParser#methodSignature}.
	 * @param ctx the parse tree
	 */
	void exitMethodSignature(TypeCheckerParser.MethodSignatureContext ctx);
	/**
	 * Enter a parse tree produced by {@link TypeCheckerParser#methodDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterMethodDeclaration(TypeCheckerParser.MethodDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link TypeCheckerParser#methodDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitMethodDeclaration(TypeCheckerParser.MethodDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link TypeCheckerParser#methodBlock}.
	 * @param ctx the parse tree
	 */
	void enterMethodBlock(TypeCheckerParser.MethodBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link TypeCheckerParser#methodBlock}.
	 * @param ctx the parse tree
	 */
	void exitMethodBlock(TypeCheckerParser.MethodBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link TypeCheckerParser#classDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterClassDeclaration(TypeCheckerParser.ClassDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link TypeCheckerParser#classDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitClassDeclaration(TypeCheckerParser.ClassDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link TypeCheckerParser#templateDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterTemplateDeclaration(TypeCheckerParser.TemplateDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link TypeCheckerParser#templateDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitTemplateDeclaration(TypeCheckerParser.TemplateDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link TypeCheckerParser#parametersCall}.
	 * @param ctx the parse tree
	 */
	void enterParametersCall(TypeCheckerParser.ParametersCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link TypeCheckerParser#parametersCall}.
	 * @param ctx the parse tree
	 */
	void exitParametersCall(TypeCheckerParser.ParametersCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link TypeCheckerParser#classVariableAccess}.
	 * @param ctx the parse tree
	 */
	void enterClassVariableAccess(TypeCheckerParser.ClassVariableAccessContext ctx);
	/**
	 * Exit a parse tree produced by {@link TypeCheckerParser#classVariableAccess}.
	 * @param ctx the parse tree
	 */
	void exitClassVariableAccess(TypeCheckerParser.ClassVariableAccessContext ctx);
	/**
	 * Enter a parse tree produced by {@link TypeCheckerParser#classMethodAccess}.
	 * @param ctx the parse tree
	 */
	void enterClassMethodAccess(TypeCheckerParser.ClassMethodAccessContext ctx);
	/**
	 * Exit a parse tree produced by {@link TypeCheckerParser#classMethodAccess}.
	 * @param ctx the parse tree
	 */
	void exitClassMethodAccess(TypeCheckerParser.ClassMethodAccessContext ctx);
	/**
	 * Enter a parse tree produced by {@link TypeCheckerParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(TypeCheckerParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link TypeCheckerParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(TypeCheckerParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link TypeCheckerParser#additiveExpression}.
	 * @param ctx the parse tree
	 */
	void enterAdditiveExpression(TypeCheckerParser.AdditiveExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link TypeCheckerParser#additiveExpression}.
	 * @param ctx the parse tree
	 */
	void exitAdditiveExpression(TypeCheckerParser.AdditiveExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link TypeCheckerParser#multiplicativeExpression}.
	 * @param ctx the parse tree
	 */
	void enterMultiplicativeExpression(TypeCheckerParser.MultiplicativeExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link TypeCheckerParser#multiplicativeExpression}.
	 * @param ctx the parse tree
	 */
	void exitMultiplicativeExpression(TypeCheckerParser.MultiplicativeExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link TypeCheckerParser#term}.
	 * @param ctx the parse tree
	 */
	void enterTerm(TypeCheckerParser.TermContext ctx);
	/**
	 * Exit a parse tree produced by {@link TypeCheckerParser#term}.
	 * @param ctx the parse tree
	 */
	void exitTerm(TypeCheckerParser.TermContext ctx);
	/**
	 * Enter a parse tree produced by {@link TypeCheckerParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(TypeCheckerParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link TypeCheckerParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(TypeCheckerParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link TypeCheckerParser#variableName}.
	 * @param ctx the parse tree
	 */
	void enterVariableName(TypeCheckerParser.VariableNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link TypeCheckerParser#variableName}.
	 * @param ctx the parse tree
	 */
	void exitVariableName(TypeCheckerParser.VariableNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link TypeCheckerParser#className}.
	 * @param ctx the parse tree
	 */
	void enterClassName(TypeCheckerParser.ClassNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link TypeCheckerParser#className}.
	 * @param ctx the parse tree
	 */
	void exitClassName(TypeCheckerParser.ClassNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link TypeCheckerParser#methodName}.
	 * @param ctx the parse tree
	 */
	void enterMethodName(TypeCheckerParser.MethodNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link TypeCheckerParser#methodName}.
	 * @param ctx the parse tree
	 */
	void exitMethodName(TypeCheckerParser.MethodNameContext ctx);
}