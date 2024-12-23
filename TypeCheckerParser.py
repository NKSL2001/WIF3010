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
        4,1,36,259,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,5,0,54,
        8,0,10,0,12,0,57,9,0,1,1,1,1,1,1,1,1,1,1,3,1,64,8,1,1,2,1,2,1,2,
        1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,
        3,6,85,8,6,1,6,1,6,1,7,1,7,1,7,1,7,3,7,93,8,7,1,7,1,7,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,5,8,104,8,8,10,8,12,8,107,9,8,1,8,3,8,110,8,8,
        1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,5,11,124,8,
        11,10,11,12,11,127,9,11,1,11,1,11,3,11,131,8,11,1,11,1,11,1,12,1,
        12,1,12,1,12,1,12,3,12,140,8,12,1,12,1,12,1,12,1,12,5,12,146,8,12,
        10,12,12,12,149,9,12,1,12,5,12,152,8,12,10,12,12,12,155,9,12,1,12,
        5,12,158,8,12,10,12,12,12,161,9,12,1,12,1,12,1,13,1,13,1,13,1,13,
        1,13,1,13,5,13,171,8,13,10,13,12,13,174,9,13,1,13,1,13,1,13,5,13,
        179,8,13,10,13,12,13,182,9,13,1,13,1,13,1,14,1,14,1,14,1,14,5,14,
        190,8,14,10,14,12,14,193,9,14,1,14,3,14,196,8,14,1,14,1,14,1,15,
        1,15,3,15,202,8,15,1,15,1,15,1,15,1,16,1,16,3,16,209,8,16,1,16,1,
        16,1,16,1,16,1,17,1,17,1,18,1,18,1,18,5,18,220,8,18,10,18,12,18,
        223,9,18,1,19,1,19,1,19,5,19,228,8,19,10,19,12,19,231,9,19,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,20,241,8,20,1,21,1,21,1,21,
        1,21,1,21,3,21,248,8,21,1,22,1,22,1,22,1,23,1,23,1,24,1,24,1,25,
        1,25,1,25,0,0,26,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,0,3,1,0,16,17,1,0,18,19,1,0,27,29,263,0,
        55,1,0,0,0,2,63,1,0,0,0,4,65,1,0,0,0,6,69,1,0,0,0,8,73,1,0,0,0,10,
        77,1,0,0,0,12,80,1,0,0,0,14,88,1,0,0,0,16,96,1,0,0,0,18,113,1,0,
        0,0,20,118,1,0,0,0,22,121,1,0,0,0,24,134,1,0,0,0,26,164,1,0,0,0,
        28,185,1,0,0,0,30,201,1,0,0,0,32,208,1,0,0,0,34,214,1,0,0,0,36,216,
        1,0,0,0,38,224,1,0,0,0,40,240,1,0,0,0,42,247,1,0,0,0,44,249,1,0,
        0,0,46,252,1,0,0,0,48,254,1,0,0,0,50,256,1,0,0,0,52,54,3,2,1,0,53,
        52,1,0,0,0,54,57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,1,1,0,0,
        0,57,55,1,0,0,0,58,64,3,12,6,0,59,64,3,14,7,0,60,64,3,4,2,0,61,64,
        3,24,12,0,62,64,3,26,13,0,63,58,1,0,0,0,63,59,1,0,0,0,63,60,1,0,
        0,0,63,61,1,0,0,0,63,62,1,0,0,0,64,3,1,0,0,0,65,66,5,1,0,0,66,67,
        3,34,17,0,67,68,5,2,0,0,68,5,1,0,0,0,69,70,5,3,0,0,70,71,3,34,17,
        0,71,72,5,2,0,0,72,7,1,0,0,0,73,74,5,4,0,0,74,75,3,46,23,0,75,76,
        3,16,8,0,76,9,1,0,0,0,77,78,3,42,21,0,78,79,3,44,22,0,79,11,1,0,
        0,0,80,81,3,10,5,0,81,84,5,5,0,0,82,85,3,34,17,0,83,85,3,8,4,0,84,
        82,1,0,0,0,84,83,1,0,0,0,85,86,1,0,0,0,86,87,5,2,0,0,87,13,1,0,0,
        0,88,89,3,44,22,0,89,92,5,5,0,0,90,93,3,34,17,0,91,93,3,8,4,0,92,
        90,1,0,0,0,92,91,1,0,0,0,93,94,1,0,0,0,94,95,5,2,0,0,95,15,1,0,0,
        0,96,109,5,6,0,0,97,98,3,42,21,0,98,105,3,44,22,0,99,100,5,7,0,0,
        100,101,3,42,21,0,101,102,3,44,22,0,102,104,1,0,0,0,103,99,1,0,0,
        0,104,107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,110,1,0,0,
        0,107,105,1,0,0,0,108,110,1,0,0,0,109,97,1,0,0,0,109,108,1,0,0,0,
        110,111,1,0,0,0,111,112,5,8,0,0,112,17,1,0,0,0,113,114,5,9,0,0,114,
        115,3,42,21,0,115,116,3,48,24,0,116,117,3,16,8,0,117,19,1,0,0,0,
        118,119,3,18,9,0,119,120,3,22,11,0,120,21,1,0,0,0,121,125,5,10,0,
        0,122,124,3,2,1,0,123,122,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,
        0,125,126,1,0,0,0,126,130,1,0,0,0,127,125,1,0,0,0,128,131,3,6,3,
        0,129,131,1,0,0,0,130,128,1,0,0,0,130,129,1,0,0,0,131,132,1,0,0,
        0,132,133,5,11,0,0,133,23,1,0,0,0,134,135,5,12,0,0,135,139,3,46,
        23,0,136,137,5,13,0,0,137,140,3,46,23,0,138,140,1,0,0,0,139,136,
        1,0,0,0,139,138,1,0,0,0,140,141,1,0,0,0,141,147,5,10,0,0,142,143,
        3,10,5,0,143,144,5,2,0,0,144,146,1,0,0,0,145,142,1,0,0,0,146,149,
        1,0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,153,1,0,0,0,149,147,
        1,0,0,0,150,152,3,12,6,0,151,150,1,0,0,0,152,155,1,0,0,0,153,151,
        1,0,0,0,153,154,1,0,0,0,154,159,1,0,0,0,155,153,1,0,0,0,156,158,
        3,20,10,0,157,156,1,0,0,0,158,161,1,0,0,0,159,157,1,0,0,0,159,160,
        1,0,0,0,160,162,1,0,0,0,161,159,1,0,0,0,162,163,5,11,0,0,163,25,
        1,0,0,0,164,165,5,14,0,0,165,166,3,46,23,0,166,172,5,10,0,0,167,
        168,3,10,5,0,168,169,5,2,0,0,169,171,1,0,0,0,170,167,1,0,0,0,171,
        174,1,0,0,0,172,170,1,0,0,0,172,173,1,0,0,0,173,180,1,0,0,0,174,
        172,1,0,0,0,175,176,3,18,9,0,176,177,5,2,0,0,177,179,1,0,0,0,178,
        175,1,0,0,0,179,182,1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,
        183,1,0,0,0,182,180,1,0,0,0,183,184,5,11,0,0,184,27,1,0,0,0,185,
        195,5,6,0,0,186,191,3,34,17,0,187,188,5,7,0,0,188,190,3,34,17,0,
        189,187,1,0,0,0,190,193,1,0,0,0,191,189,1,0,0,0,191,192,1,0,0,0,
        192,196,1,0,0,0,193,191,1,0,0,0,194,196,1,0,0,0,195,186,1,0,0,0,
        195,194,1,0,0,0,196,197,1,0,0,0,197,198,5,8,0,0,198,29,1,0,0,0,199,
        202,3,46,23,0,200,202,3,44,22,0,201,199,1,0,0,0,201,200,1,0,0,0,
        202,203,1,0,0,0,203,204,5,15,0,0,204,205,3,44,22,0,205,31,1,0,0,
        0,206,209,3,46,23,0,207,209,3,44,22,0,208,206,1,0,0,0,208,207,1,
        0,0,0,209,210,1,0,0,0,210,211,5,15,0,0,211,212,3,48,24,0,212,213,
        3,28,14,0,213,33,1,0,0,0,214,215,3,36,18,0,215,35,1,0,0,0,216,221,
        3,38,19,0,217,218,7,0,0,0,218,220,3,38,19,0,219,217,1,0,0,0,220,
        223,1,0,0,0,221,219,1,0,0,0,221,222,1,0,0,0,222,37,1,0,0,0,223,221,
        1,0,0,0,224,229,3,40,20,0,225,226,7,1,0,0,226,228,3,40,20,0,227,
        225,1,0,0,0,228,231,1,0,0,0,229,227,1,0,0,0,229,230,1,0,0,0,230,
        39,1,0,0,0,231,229,1,0,0,0,232,241,3,44,22,0,233,241,3,50,25,0,234,
        241,3,30,15,0,235,241,3,32,16,0,236,237,5,6,0,0,237,238,3,34,17,
        0,238,239,5,8,0,0,239,241,1,0,0,0,240,232,1,0,0,0,240,233,1,0,0,
        0,240,234,1,0,0,0,240,235,1,0,0,0,240,236,1,0,0,0,241,41,1,0,0,0,
        242,248,5,20,0,0,243,248,5,21,0,0,244,248,5,22,0,0,245,248,5,23,
        0,0,246,248,3,46,23,0,247,242,1,0,0,0,247,243,1,0,0,0,247,244,1,
        0,0,0,247,245,1,0,0,0,247,246,1,0,0,0,248,43,1,0,0,0,249,250,5,24,
        0,0,250,251,5,26,0,0,251,45,1,0,0,0,252,253,5,26,0,0,253,47,1,0,
        0,0,254,255,5,26,0,0,255,49,1,0,0,0,256,257,7,2,0,0,257,51,1,0,0,
        0,22,55,63,84,92,105,109,125,130,139,147,153,159,172,180,191,195,
        201,208,221,229,240,247
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
                      "<INVALID>", "Whitespace", "Identifier", "ChunkLiteral", 
                      "FractionLiteral", "StringLiteral", "Letter", "NonZeroDigit", 
                      "Digit", "CharacterExceptQuote", "Character", "BlockComment", 
                      "LineComment" ]

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
    RULE_literal = 25

    ruleNames =  [ "program", "statement", "showStatement", "returnStatement", 
                   "createClassStatement", "variableSignature", "variableDeclaration", 
                   "assignment", "parametersInit", "methodSignature", "methodDeclaration", 
                   "methodBlock", "classDeclaration", "templateDeclaration", 
                   "parametersCall", "classVariableAccess", "classMethodAccess", 
                   "expression", "additiveExpression", "multiplicativeExpression", 
                   "term", "type", "variableName", "className", "methodName", 
                   "literal" ]

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
    ChunkLiteral=27
    FractionLiteral=28
    StringLiteral=29
    Letter=30
    NonZeroDigit=31
    Digit=32
    CharacterExceptQuote=33
    Character=34
    BlockComment=35
    LineComment=36

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
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 99635202) != 0):
                self.state = 52
                self.statement()
                self.state = 57
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
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 22, 23, 26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.variableDeclaration()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.assignment()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 60
                self.showStatement()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 61
                self.classDeclaration()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 5)
                self.state = 62
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
            self.state = 65
            self.match(TypeCheckerParser.T__0)
            self.state = 66
            self.expression()
            self.state = 67
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
            self.state = 69
            self.match(TypeCheckerParser.T__2)
            self.state = 70
            self.expression()
            self.state = 71
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
            self.state = 73
            self.match(TypeCheckerParser.T__3)
            self.state = 74
            self.className()
            self.state = 75
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
            self.state = 77
            self.type_()
            self.state = 78
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
            self.state = 80
            self.variableSignature()
            self.state = 81
            self.match(TypeCheckerParser.T__4)
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 24, 26, 27, 28, 29]:
                self.state = 82
                self.expression()
                pass
            elif token in [4]:
                self.state = 83
                self.createClassStatement()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 86
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
            self.state = 88
            self.variableName()
            self.state = 89
            self.match(TypeCheckerParser.T__4)
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 24, 26, 27, 28, 29]:
                self.state = 90
                self.expression()
                pass
            elif token in [4]:
                self.state = 91
                self.createClassStatement()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 94
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
            self.state = 96
            self.match(TypeCheckerParser.T__5)
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 22, 23, 26]:
                self.state = 97
                self.type_()
                self.state = 98
                self.variableName()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 99
                    self.match(TypeCheckerParser.T__6)
                    self.state = 100
                    self.type_()
                    self.state = 101
                    self.variableName()
                    self.state = 107
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [8]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 111
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
            self.state = 113
            self.match(TypeCheckerParser.T__8)
            self.state = 114
            self.type_()
            self.state = 115
            self.methodName()
            self.state = 116
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
            self.state = 118
            self.methodSignature()
            self.state = 119
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
            self.state = 121
            self.match(TypeCheckerParser.T__9)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 99635202) != 0):
                self.state = 122
                self.statement()
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 128
                self.returnStatement()
                pass
            elif token in [11]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 132
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
            self.state = 134
            self.match(TypeCheckerParser.T__11)
            self.state = 135
            self.className()
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.state = 136
                self.match(TypeCheckerParser.T__12)
                self.state = 137
                self.className()
                pass
            elif token in [10]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 141
            self.match(TypeCheckerParser.T__9)
            self.state = 147
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 142
                    self.variableSignature()
                    self.state = 143
                    self.match(TypeCheckerParser.T__1) 
                self.state = 149
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 82837504) != 0):
                self.state = 150
                self.variableDeclaration()
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 156
                self.methodDeclaration()
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 162
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
            self.state = 164
            self.match(TypeCheckerParser.T__13)
            self.state = 165
            self.className()
            self.state = 166
            self.match(TypeCheckerParser.T__9)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 82837504) != 0):
                self.state = 167
                self.variableSignature()
                self.state = 168
                self.match(TypeCheckerParser.T__1)
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 175
                self.methodSignature()
                self.state = 176
                self.match(TypeCheckerParser.T__1)
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 183
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
            self.state = 185
            self.match(TypeCheckerParser.T__5)
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 24, 26, 27, 28, 29]:
                self.state = 186
                self.expression()
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 187
                    self.match(TypeCheckerParser.T__6)
                    self.state = 188
                    self.expression()
                    self.state = 193
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [8]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 197
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
            self.state = 201
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.state = 199
                self.className()
                pass
            elif token in [24]:
                self.state = 200
                self.variableName()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 203
            self.match(TypeCheckerParser.T__14)
            self.state = 204
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
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.state = 206
                self.className()
                pass
            elif token in [24]:
                self.state = 207
                self.variableName()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 210
            self.match(TypeCheckerParser.T__14)
            self.state = 211
            self.methodName()
            self.state = 212
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
            self.state = 214
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
            self.state = 216
            self.multiplicativeExpression()
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16 or _la==17:
                self.state = 217
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 218
                self.multiplicativeExpression()
                self.state = 223
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
            self.state = 224
            self.term()
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==19:
                self.state = 225
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 226
                self.term()
                self.state = 231
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


        def literal(self):
            return self.getTypedRuleContext(TypeCheckerParser.LiteralContext,0)


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
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.variableName()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 234
                self.classVariableAccess()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 235
                self.classMethodAccess()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 236
                self.match(TypeCheckerParser.T__5)
                self.state = 237
                self.expression()
                self.state = 238
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
            self.state = 247
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.match(TypeCheckerParser.T__19)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                self.match(TypeCheckerParser.T__20)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 244
                self.match(TypeCheckerParser.T__21)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 245
                self.match(TypeCheckerParser.T__22)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 5)
                self.state = 246
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
            self.state = 249
            self.match(TypeCheckerParser.T__23)
            self.state = 250
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
            self.state = 252
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
            self.state = 254
            self.match(TypeCheckerParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ChunkLiteral(self):
            return self.getToken(TypeCheckerParser.ChunkLiteral, 0)

        def FractionLiteral(self):
            return self.getToken(TypeCheckerParser.FractionLiteral, 0)

        def StringLiteral(self):
            return self.getToken(TypeCheckerParser.StringLiteral, 0)

        def getRuleIndex(self):
            return TypeCheckerParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = TypeCheckerParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 939524096) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





