# Generated from TypeChecker.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,37,255,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,5,0,52,8,0,10,0,
        12,0,55,9,0,1,1,1,1,1,1,1,1,1,1,3,1,62,8,1,1,2,1,2,1,2,1,2,1,3,1,
        3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,83,8,6,
        1,6,1,6,1,7,1,7,1,7,1,7,3,7,91,8,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,5,8,102,8,8,10,8,12,8,105,9,8,1,8,3,8,108,8,8,1,8,1,8,1,9,
        1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,5,11,122,8,11,10,11,12,
        11,125,9,11,1,11,1,11,3,11,129,8,11,1,11,1,11,1,12,1,12,1,12,1,12,
        1,12,3,12,138,8,12,1,12,1,12,1,12,1,12,5,12,144,8,12,10,12,12,12,
        147,9,12,1,12,5,12,150,8,12,10,12,12,12,153,9,12,1,12,5,12,156,8,
        12,10,12,12,12,159,9,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,
        5,13,169,8,13,10,13,12,13,172,9,13,1,13,1,13,1,13,5,13,177,8,13,
        10,13,12,13,180,9,13,1,13,1,13,1,14,1,14,1,14,1,14,5,14,188,8,14,
        10,14,12,14,191,9,14,1,14,3,14,194,8,14,1,14,1,14,1,15,1,15,3,15,
        200,8,15,1,15,1,15,1,15,1,16,1,16,3,16,207,8,16,1,16,1,16,1,16,1,
        16,1,17,1,17,1,18,1,18,1,18,5,18,218,8,18,10,18,12,18,221,9,18,1,
        19,1,19,1,19,5,19,226,8,19,10,19,12,19,229,9,19,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,3,20,239,8,20,1,21,1,21,1,21,1,21,1,21,3,
        21,246,8,21,1,22,1,22,1,22,1,23,1,23,1,24,1,24,1,24,0,0,25,0,2,4,
        6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        0,2,1,0,16,17,1,0,18,19,260,0,53,1,0,0,0,2,61,1,0,0,0,4,63,1,0,0,
        0,6,67,1,0,0,0,8,71,1,0,0,0,10,75,1,0,0,0,12,78,1,0,0,0,14,86,1,
        0,0,0,16,94,1,0,0,0,18,111,1,0,0,0,20,116,1,0,0,0,22,119,1,0,0,0,
        24,132,1,0,0,0,26,162,1,0,0,0,28,183,1,0,0,0,30,199,1,0,0,0,32,206,
        1,0,0,0,34,212,1,0,0,0,36,214,1,0,0,0,38,222,1,0,0,0,40,238,1,0,
        0,0,42,245,1,0,0,0,44,247,1,0,0,0,46,250,1,0,0,0,48,252,1,0,0,0,
        50,52,3,2,1,0,51,50,1,0,0,0,52,55,1,0,0,0,53,51,1,0,0,0,53,54,1,
        0,0,0,54,1,1,0,0,0,55,53,1,0,0,0,56,62,3,12,6,0,57,62,3,14,7,0,58,
        62,3,4,2,0,59,62,3,24,12,0,60,62,3,26,13,0,61,56,1,0,0,0,61,57,1,
        0,0,0,61,58,1,0,0,0,61,59,1,0,0,0,61,60,1,0,0,0,62,3,1,0,0,0,63,
        64,5,1,0,0,64,65,3,34,17,0,65,66,5,2,0,0,66,5,1,0,0,0,67,68,5,3,
        0,0,68,69,3,34,17,0,69,70,5,2,0,0,70,7,1,0,0,0,71,72,5,4,0,0,72,
        73,3,46,23,0,73,74,3,16,8,0,74,9,1,0,0,0,75,76,3,42,21,0,76,77,3,
        44,22,0,77,11,1,0,0,0,78,79,3,10,5,0,79,82,5,5,0,0,80,83,3,34,17,
        0,81,83,3,8,4,0,82,80,1,0,0,0,82,81,1,0,0,0,83,84,1,0,0,0,84,85,
        5,2,0,0,85,13,1,0,0,0,86,87,3,44,22,0,87,90,5,5,0,0,88,91,3,34,17,
        0,89,91,3,8,4,0,90,88,1,0,0,0,90,89,1,0,0,0,91,92,1,0,0,0,92,93,
        5,2,0,0,93,15,1,0,0,0,94,107,5,6,0,0,95,96,3,42,21,0,96,103,3,44,
        22,0,97,98,5,7,0,0,98,99,3,42,21,0,99,100,3,44,22,0,100,102,1,0,
        0,0,101,97,1,0,0,0,102,105,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,
        0,104,108,1,0,0,0,105,103,1,0,0,0,106,108,1,0,0,0,107,95,1,0,0,0,
        107,106,1,0,0,0,108,109,1,0,0,0,109,110,5,8,0,0,110,17,1,0,0,0,111,
        112,5,9,0,0,112,113,3,42,21,0,113,114,3,48,24,0,114,115,3,16,8,0,
        115,19,1,0,0,0,116,117,3,18,9,0,117,118,3,22,11,0,118,21,1,0,0,0,
        119,123,5,10,0,0,120,122,3,2,1,0,121,120,1,0,0,0,122,125,1,0,0,0,
        123,121,1,0,0,0,123,124,1,0,0,0,124,128,1,0,0,0,125,123,1,0,0,0,
        126,129,3,6,3,0,127,129,1,0,0,0,128,126,1,0,0,0,128,127,1,0,0,0,
        129,130,1,0,0,0,130,131,5,11,0,0,131,23,1,0,0,0,132,133,5,12,0,0,
        133,137,3,46,23,0,134,135,5,13,0,0,135,138,3,46,23,0,136,138,1,0,
        0,0,137,134,1,0,0,0,137,136,1,0,0,0,138,139,1,0,0,0,139,145,5,10,
        0,0,140,141,3,10,5,0,141,142,5,2,0,0,142,144,1,0,0,0,143,140,1,0,
        0,0,144,147,1,0,0,0,145,143,1,0,0,0,145,146,1,0,0,0,146,151,1,0,
        0,0,147,145,1,0,0,0,148,150,3,12,6,0,149,148,1,0,0,0,150,153,1,0,
        0,0,151,149,1,0,0,0,151,152,1,0,0,0,152,157,1,0,0,0,153,151,1,0,
        0,0,154,156,3,20,10,0,155,154,1,0,0,0,156,159,1,0,0,0,157,155,1,
        0,0,0,157,158,1,0,0,0,158,160,1,0,0,0,159,157,1,0,0,0,160,161,5,
        11,0,0,161,25,1,0,0,0,162,163,5,14,0,0,163,164,3,46,23,0,164,170,
        5,10,0,0,165,166,3,10,5,0,166,167,5,2,0,0,167,169,1,0,0,0,168,165,
        1,0,0,0,169,172,1,0,0,0,170,168,1,0,0,0,170,171,1,0,0,0,171,178,
        1,0,0,0,172,170,1,0,0,0,173,174,3,18,9,0,174,175,5,2,0,0,175,177,
        1,0,0,0,176,173,1,0,0,0,177,180,1,0,0,0,178,176,1,0,0,0,178,179,
        1,0,0,0,179,181,1,0,0,0,180,178,1,0,0,0,181,182,5,11,0,0,182,27,
        1,0,0,0,183,193,5,6,0,0,184,189,3,34,17,0,185,186,5,7,0,0,186,188,
        3,34,17,0,187,185,1,0,0,0,188,191,1,0,0,0,189,187,1,0,0,0,189,190,
        1,0,0,0,190,194,1,0,0,0,191,189,1,0,0,0,192,194,1,0,0,0,193,184,
        1,0,0,0,193,192,1,0,0,0,194,195,1,0,0,0,195,196,5,8,0,0,196,29,1,
        0,0,0,197,200,3,46,23,0,198,200,3,44,22,0,199,197,1,0,0,0,199,198,
        1,0,0,0,200,201,1,0,0,0,201,202,5,15,0,0,202,203,3,44,22,0,203,31,
        1,0,0,0,204,207,3,46,23,0,205,207,3,44,22,0,206,204,1,0,0,0,206,
        205,1,0,0,0,207,208,1,0,0,0,208,209,5,15,0,0,209,210,3,48,24,0,210,
        211,3,28,14,0,211,33,1,0,0,0,212,213,3,36,18,0,213,35,1,0,0,0,214,
        219,3,38,19,0,215,216,7,0,0,0,216,218,3,38,19,0,217,215,1,0,0,0,
        218,221,1,0,0,0,219,217,1,0,0,0,219,220,1,0,0,0,220,37,1,0,0,0,221,
        219,1,0,0,0,222,227,3,40,20,0,223,224,7,1,0,0,224,226,3,40,20,0,
        225,223,1,0,0,0,226,229,1,0,0,0,227,225,1,0,0,0,227,228,1,0,0,0,
        228,39,1,0,0,0,229,227,1,0,0,0,230,239,3,44,22,0,231,239,5,27,0,
        0,232,239,3,30,15,0,233,239,3,32,16,0,234,235,5,6,0,0,235,236,3,
        34,17,0,236,237,5,8,0,0,237,239,1,0,0,0,238,230,1,0,0,0,238,231,
        1,0,0,0,238,232,1,0,0,0,238,233,1,0,0,0,238,234,1,0,0,0,239,41,1,
        0,0,0,240,246,5,20,0,0,241,246,5,21,0,0,242,246,5,22,0,0,243,246,
        5,23,0,0,244,246,3,46,23,0,245,240,1,0,0,0,245,241,1,0,0,0,245,242,
        1,0,0,0,245,243,1,0,0,0,245,244,1,0,0,0,246,43,1,0,0,0,247,248,5,
        24,0,0,248,249,5,26,0,0,249,45,1,0,0,0,250,251,5,26,0,0,251,47,1,
        0,0,0,252,253,5,26,0,0,253,49,1,0,0,0,22,53,61,82,90,103,107,123,
        128,137,145,151,157,170,178,189,193,199,206,219,227,238,245
    ]

class TypeCheckerParser ( Parser ):

    grammarFileName = "TypeChecker.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'show'", "'!'", "'return'", "'new'", 
                     "':='", "'('", "','", "')'", "'method'", "'{'", "'}'", 
                     "'class'", "'inherit'", "'template'", "'.'", "'+'", 
                     "'-'", "'*'", "'/'", "'chunk'", "'fraction'", "'string'", 
                     "'none'", "'$'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "Whitespace", "Identifier", "Literal", 
                      "ChunkLiteral", "FractionLiteral", "StringLiteral", 
                      "Letter", "NonZeroDigit", "Digit", "CharacterExceptQuote", 
                      "Character", "BlockComment", "LineComment" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_showStatement = 2
    RULE_returnStatement = 3
    RULE_createClassStatement = 4
    RULE_variableSignature = 5
    RULE_variableDeclaration = 6
    RULE_assignment = 7
    RULE_parametersInit = 8
    RULE_methodSignature = 9
    RULE_methodDeclaration = 10
    RULE_methodBlock = 11
    RULE_classDeclaration = 12
    RULE_templateDeclaration = 13
    RULE_parametersCall = 14
    RULE_classVariableAccess = 15
    RULE_classMethodAccess = 16
    RULE_expression = 17
    RULE_additiveExpression = 18
    RULE_multiplicativeExpression = 19
    RULE_term = 20
    RULE_type = 21
    RULE_variableName = 22
    RULE_className = 23
    RULE_methodName = 24

    ruleNames =  [ "program", "statement", "showStatement", "returnStatement", 
                   "createClassStatement", "variableSignature", "variableDeclaration", 
                   "assignment", "parametersInit", "methodSignature", "methodDeclaration", 
                   "methodBlock", "classDeclaration", "templateDeclaration", 
                   "parametersCall", "classVariableAccess", "classMethodAccess", 
                   "expression", "additiveExpression", "multiplicativeExpression", 
                   "term", "type", "variableName", "className", "methodName" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    Whitespace=25
    Identifier=26
    Literal=27
    ChunkLiteral=28
    FractionLiteral=29
    StringLiteral=30
    Letter=31
    NonZeroDigit=32
    Digit=33
    CharacterExceptQuote=34
    Character=35
    BlockComment=36
    LineComment=37

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TypeCheckerParser.StatementContext)
            else:
                return self.getTypedRuleContext(TypeCheckerParser.StatementContext,i)


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = TypeCheckerParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 99635202) != 0):
                self.state = 50
                self.statement()
                self.state = 55
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaration(self):
            return self.getTypedRuleContext(TypeCheckerParser.VariableDeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(TypeCheckerParser.AssignmentContext,0)


        def showStatement(self):
            return self.getTypedRuleContext(TypeCheckerParser.ShowStatementContext,0)


        def classDeclaration(self):
            return self.getTypedRuleContext(TypeCheckerParser.ClassDeclarationContext,0)


        def templateDeclaration(self):
            return self.getTypedRuleContext(TypeCheckerParser.TemplateDeclarationContext,0)


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = TypeCheckerParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 22, 23, 26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.variableDeclaration()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.assignment()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.showStatement()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 59
                self.classDeclaration()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 5)
                self.state = 60
                self.templateDeclaration()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShowStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(TypeCheckerParser.ExpressionContext,0)


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_showStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShowStatement" ):
                listener.enterShowStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShowStatement" ):
                listener.exitShowStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShowStatement" ):
                return visitor.visitShowStatement(self)
            else:
                return visitor.visitChildren(self)




    def showStatement(self):

        localctx = TypeCheckerParser.ShowStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_showStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(TypeCheckerParser.T__0)
            self.state = 64
            self.expression()
            self.state = 65
            self.match(TypeCheckerParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(TypeCheckerParser.ExpressionContext,0)


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = TypeCheckerParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(TypeCheckerParser.T__2)
            self.state = 68
            self.expression()
            self.state = 69
            self.match(TypeCheckerParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateClassStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def className(self):
            return self.getTypedRuleContext(TypeCheckerParser.ClassNameContext,0)


        def parametersInit(self):
            return self.getTypedRuleContext(TypeCheckerParser.ParametersInitContext,0)


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_createClassStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateClassStatement" ):
                listener.enterCreateClassStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateClassStatement" ):
                listener.exitCreateClassStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateClassStatement" ):
                return visitor.visitCreateClassStatement(self)
            else:
                return visitor.visitChildren(self)




    def createClassStatement(self):

        localctx = TypeCheckerParser.CreateClassStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_createClassStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(TypeCheckerParser.T__3)
            self.state = 72
            self.className()
            self.state = 73
            self.parametersInit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableSignatureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TypeCheckerParser.TypeContext,0)


        def variableName(self):
            return self.getTypedRuleContext(TypeCheckerParser.VariableNameContext,0)


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_variableSignature

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableSignature" ):
                listener.enterVariableSignature(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableSignature" ):
                listener.exitVariableSignature(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableSignature" ):
                return visitor.visitVariableSignature(self)
            else:
                return visitor.visitChildren(self)




    def variableSignature(self):

        localctx = TypeCheckerParser.VariableSignatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variableSignature)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.type_()
            self.state = 76
            self.variableName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableSignature(self):
            return self.getTypedRuleContext(TypeCheckerParser.VariableSignatureContext,0)


        def expression(self):
            return self.getTypedRuleContext(TypeCheckerParser.ExpressionContext,0)


        def createClassStatement(self):
            return self.getTypedRuleContext(TypeCheckerParser.CreateClassStatementContext,0)


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration" ):
                return visitor.visitVariableDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def variableDeclaration(self):

        localctx = TypeCheckerParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.variableSignature()
            self.state = 79
            self.match(TypeCheckerParser.T__4)
            self.state = 82
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 24, 26, 27]:
                self.state = 80
                self.expression()
                pass
            elif token in [4]:
                self.state = 81
                self.createClassStatement()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 84
            self.match(TypeCheckerParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableName(self):
            return self.getTypedRuleContext(TypeCheckerParser.VariableNameContext,0)


        def expression(self):
            return self.getTypedRuleContext(TypeCheckerParser.ExpressionContext,0)


        def createClassStatement(self):
            return self.getTypedRuleContext(TypeCheckerParser.CreateClassStatementContext,0)


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = TypeCheckerParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.variableName()
            self.state = 87
            self.match(TypeCheckerParser.T__4)
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 24, 26, 27]:
                self.state = 88
                self.expression()
                pass
            elif token in [4]:
                self.state = 89
                self.createClassStatement()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 92
            self.match(TypeCheckerParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TypeCheckerParser.TypeContext)
            else:
                return self.getTypedRuleContext(TypeCheckerParser.TypeContext,i)


        def variableName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TypeCheckerParser.VariableNameContext)
            else:
                return self.getTypedRuleContext(TypeCheckerParser.VariableNameContext,i)


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_parametersInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametersInit" ):
                listener.enterParametersInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametersInit" ):
                listener.exitParametersInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametersInit" ):
                return visitor.visitParametersInit(self)
            else:
                return visitor.visitChildren(self)




    def parametersInit(self):

        localctx = TypeCheckerParser.ParametersInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parametersInit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(TypeCheckerParser.T__5)
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 22, 23, 26]:
                self.state = 95
                self.type_()
                self.state = 96
                self.variableName()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 97
                    self.match(TypeCheckerParser.T__6)
                    self.state = 98
                    self.type_()
                    self.state = 99
                    self.variableName()
                    self.state = 105
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [8]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 109
            self.match(TypeCheckerParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodSignatureContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(TypeCheckerParser.TypeContext,0)


        def methodName(self):
            return self.getTypedRuleContext(TypeCheckerParser.MethodNameContext,0)


        def parametersInit(self):
            return self.getTypedRuleContext(TypeCheckerParser.ParametersInitContext,0)


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_methodSignature

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodSignature" ):
                listener.enterMethodSignature(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodSignature" ):
                listener.exitMethodSignature(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodSignature" ):
                return visitor.visitMethodSignature(self)
            else:
                return visitor.visitChildren(self)




    def methodSignature(self):

        localctx = TypeCheckerParser.MethodSignatureContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_methodSignature)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(TypeCheckerParser.T__8)
            self.state = 112
            self.type_()
            self.state = 113
            self.methodName()
            self.state = 114
            self.parametersInit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodSignature(self):
            return self.getTypedRuleContext(TypeCheckerParser.MethodSignatureContext,0)


        def methodBlock(self):
            return self.getTypedRuleContext(TypeCheckerParser.MethodBlockContext,0)


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_methodDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDeclaration" ):
                listener.enterMethodDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDeclaration" ):
                listener.exitMethodDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDeclaration" ):
                return visitor.visitMethodDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def methodDeclaration(self):

        localctx = TypeCheckerParser.MethodDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_methodDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.methodSignature()
            self.state = 117
            self.methodBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def returnStatement(self):
            return self.getTypedRuleContext(TypeCheckerParser.ReturnStatementContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TypeCheckerParser.StatementContext)
            else:
                return self.getTypedRuleContext(TypeCheckerParser.StatementContext,i)


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_methodBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodBlock" ):
                listener.enterMethodBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodBlock" ):
                listener.exitMethodBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodBlock" ):
                return visitor.visitMethodBlock(self)
            else:
                return visitor.visitChildren(self)




    def methodBlock(self):

        localctx = TypeCheckerParser.MethodBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_methodBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(TypeCheckerParser.T__9)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 99635202) != 0):
                self.state = 120
                self.statement()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 126
                self.returnStatement()
                pass
            elif token in [11]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 130
            self.match(TypeCheckerParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def className(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TypeCheckerParser.ClassNameContext)
            else:
                return self.getTypedRuleContext(TypeCheckerParser.ClassNameContext,i)


        def variableSignature(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TypeCheckerParser.VariableSignatureContext)
            else:
                return self.getTypedRuleContext(TypeCheckerParser.VariableSignatureContext,i)


        def variableDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TypeCheckerParser.VariableDeclarationContext)
            else:
                return self.getTypedRuleContext(TypeCheckerParser.VariableDeclarationContext,i)


        def methodDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TypeCheckerParser.MethodDeclarationContext)
            else:
                return self.getTypedRuleContext(TypeCheckerParser.MethodDeclarationContext,i)


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_classDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDeclaration" ):
                listener.enterClassDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDeclaration" ):
                listener.exitClassDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDeclaration" ):
                return visitor.visitClassDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def classDeclaration(self):

        localctx = TypeCheckerParser.ClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_classDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(TypeCheckerParser.T__11)
            self.state = 133
            self.className()
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.state = 134
                self.match(TypeCheckerParser.T__12)
                self.state = 135
                self.className()
                pass
            elif token in [10]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 139
            self.match(TypeCheckerParser.T__9)
            self.state = 145
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 140
                    self.variableSignature()
                    self.state = 141
                    self.match(TypeCheckerParser.T__1) 
                self.state = 147
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 82837504) != 0):
                self.state = 148
                self.variableDeclaration()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 154
                self.methodDeclaration()
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 160
            self.match(TypeCheckerParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TemplateDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def className(self):
            return self.getTypedRuleContext(TypeCheckerParser.ClassNameContext,0)


        def variableSignature(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TypeCheckerParser.VariableSignatureContext)
            else:
                return self.getTypedRuleContext(TypeCheckerParser.VariableSignatureContext,i)


        def methodSignature(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TypeCheckerParser.MethodSignatureContext)
            else:
                return self.getTypedRuleContext(TypeCheckerParser.MethodSignatureContext,i)


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_templateDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplateDeclaration" ):
                listener.enterTemplateDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplateDeclaration" ):
                listener.exitTemplateDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTemplateDeclaration" ):
                return visitor.visitTemplateDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def templateDeclaration(self):

        localctx = TypeCheckerParser.TemplateDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_templateDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(TypeCheckerParser.T__13)
            self.state = 163
            self.className()
            self.state = 164
            self.match(TypeCheckerParser.T__9)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 82837504) != 0):
                self.state = 165
                self.variableSignature()
                self.state = 166
                self.match(TypeCheckerParser.T__1)
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 173
                self.methodSignature()
                self.state = 174
                self.match(TypeCheckerParser.T__1)
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 181
            self.match(TypeCheckerParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TypeCheckerParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(TypeCheckerParser.ExpressionContext,i)


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_parametersCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametersCall" ):
                listener.enterParametersCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametersCall" ):
                listener.exitParametersCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametersCall" ):
                return visitor.visitParametersCall(self)
            else:
                return visitor.visitChildren(self)




    def parametersCall(self):

        localctx = TypeCheckerParser.ParametersCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_parametersCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(TypeCheckerParser.T__5)
            self.state = 193
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 24, 26, 27]:
                self.state = 184
                self.expression()
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 185
                    self.match(TypeCheckerParser.T__6)
                    self.state = 186
                    self.expression()
                    self.state = 191
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [8]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 195
            self.match(TypeCheckerParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassVariableAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TypeCheckerParser.VariableNameContext)
            else:
                return self.getTypedRuleContext(TypeCheckerParser.VariableNameContext,i)


        def className(self):
            return self.getTypedRuleContext(TypeCheckerParser.ClassNameContext,0)


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_classVariableAccess

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassVariableAccess" ):
                listener.enterClassVariableAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassVariableAccess" ):
                listener.exitClassVariableAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassVariableAccess" ):
                return visitor.visitClassVariableAccess(self)
            else:
                return visitor.visitChildren(self)




    def classVariableAccess(self):

        localctx = TypeCheckerParser.ClassVariableAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_classVariableAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.state = 197
                self.className()
                pass
            elif token in [24]:
                self.state = 198
                self.variableName()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 201
            self.match(TypeCheckerParser.T__14)
            self.state = 202
            self.variableName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassMethodAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def methodName(self):
            return self.getTypedRuleContext(TypeCheckerParser.MethodNameContext,0)


        def parametersCall(self):
            return self.getTypedRuleContext(TypeCheckerParser.ParametersCallContext,0)


        def className(self):
            return self.getTypedRuleContext(TypeCheckerParser.ClassNameContext,0)


        def variableName(self):
            return self.getTypedRuleContext(TypeCheckerParser.VariableNameContext,0)


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_classMethodAccess

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassMethodAccess" ):
                listener.enterClassMethodAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassMethodAccess" ):
                listener.exitClassMethodAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassMethodAccess" ):
                return visitor.visitClassMethodAccess(self)
            else:
                return visitor.visitChildren(self)




    def classMethodAccess(self):

        localctx = TypeCheckerParser.ClassMethodAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_classMethodAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.state = 204
                self.className()
                pass
            elif token in [24]:
                self.state = 205
                self.variableName()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 208
            self.match(TypeCheckerParser.T__14)
            self.state = 209
            self.methodName()
            self.state = 210
            self.parametersCall()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self):
            return self.getTypedRuleContext(TypeCheckerParser.AdditiveExpressionContext,0)


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = TypeCheckerParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.additiveExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TypeCheckerParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(TypeCheckerParser.MultiplicativeExpressionContext,i)


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpression(self):

        localctx = TypeCheckerParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.multiplicativeExpression()
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16 or _la==17:
                self.state = 215
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 216
                self.multiplicativeExpression()
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TypeCheckerParser.TermContext)
            else:
                return self.getTypedRuleContext(TypeCheckerParser.TermContext,i)


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpression(self):

        localctx = TypeCheckerParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.term()
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==19:
                self.state = 223
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 224
                self.term()
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableName(self):
            return self.getTypedRuleContext(TypeCheckerParser.VariableNameContext,0)


        def Literal(self):
            return self.getToken(TypeCheckerParser.Literal, 0)

        def classVariableAccess(self):
            return self.getTypedRuleContext(TypeCheckerParser.ClassVariableAccessContext,0)


        def classMethodAccess(self):
            return self.getTypedRuleContext(TypeCheckerParser.ClassMethodAccessContext,0)


        def expression(self):
            return self.getTypedRuleContext(TypeCheckerParser.ExpressionContext,0)


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = TypeCheckerParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_term)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.variableName()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.match(TypeCheckerParser.Literal)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 232
                self.classVariableAccess()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 233
                self.classMethodAccess()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 234
                self.match(TypeCheckerParser.T__5)
                self.state = 235
                self.expression()
                self.state = 236
                self.match(TypeCheckerParser.T__7)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def className(self):
            return self.getTypedRuleContext(TypeCheckerParser.ClassNameContext,0)


        def getRuleIndex(self):
            return TypeCheckerParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = TypeCheckerParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_type)
        try:
            self.state = 245
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.match(TypeCheckerParser.T__19)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.match(TypeCheckerParser.T__20)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 242
                self.match(TypeCheckerParser.T__21)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 243
                self.match(TypeCheckerParser.T__22)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 5)
                self.state = 244
                self.className()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(TypeCheckerParser.Identifier, 0)

        def getRuleIndex(self):
            return TypeCheckerParser.RULE_variableName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableName" ):
                listener.enterVariableName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableName" ):
                listener.exitVariableName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableName" ):
                return visitor.visitVariableName(self)
            else:
                return visitor.visitChildren(self)




    def variableName(self):

        localctx = TypeCheckerParser.VariableNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_variableName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(TypeCheckerParser.T__23)
            self.state = 248
            self.match(TypeCheckerParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(TypeCheckerParser.Identifier, 0)

        def getRuleIndex(self):
            return TypeCheckerParser.RULE_className

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassName" ):
                listener.enterClassName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassName" ):
                listener.exitClassName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassName" ):
                return visitor.visitClassName(self)
            else:
                return visitor.visitChildren(self)




    def className(self):

        localctx = TypeCheckerParser.ClassNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_className)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(TypeCheckerParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(TypeCheckerParser.Identifier, 0)

        def getRuleIndex(self):
            return TypeCheckerParser.RULE_methodName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodName" ):
                listener.enterMethodName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodName" ):
                listener.exitMethodName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodName" ):
                return visitor.visitMethodName(self)
            else:
                return visitor.visitChildren(self)




    def methodName(self):

        localctx = TypeCheckerParser.MethodNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_methodName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(TypeCheckerParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





