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
        4,1,34,301,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,5,0,62,8,0,10,0,12,0,65,9,0,1,
        1,1,1,1,1,1,1,1,1,3,1,72,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,
        1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,93,8,6,1,6,1,6,1,7,1,
        7,1,7,1,7,3,7,101,8,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,112,
        8,8,10,8,12,8,115,9,8,1,8,3,8,118,8,8,1,8,1,8,1,9,1,9,1,9,1,9,1,
        9,1,10,1,10,1,10,1,11,1,11,5,11,132,8,11,10,11,12,11,135,9,11,1,
        11,1,11,3,11,139,8,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,3,12,148,
        8,12,1,12,1,12,1,12,1,12,5,12,154,8,12,10,12,12,12,157,9,12,1,12,
        5,12,160,8,12,10,12,12,12,163,9,12,1,12,5,12,166,8,12,10,12,12,12,
        169,9,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,5,13,179,8,13,10,
        13,12,13,182,9,13,1,13,1,13,1,13,5,13,187,8,13,10,13,12,13,190,9,
        13,1,13,1,13,1,14,1,14,1,14,1,14,5,14,198,8,14,10,14,12,14,201,9,
        14,1,14,3,14,204,8,14,1,14,1,14,1,15,1,15,3,15,210,8,15,1,15,1,15,
        1,15,1,16,1,16,3,16,217,8,16,1,16,1,16,1,16,1,16,1,17,1,17,1,18,
        1,18,1,18,5,18,228,8,18,10,18,12,18,231,9,18,1,19,1,19,1,19,5,19,
        236,8,19,10,19,12,19,239,9,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,3,20,249,8,20,1,21,1,21,1,21,1,21,1,21,3,21,256,8,21,1,22,1,
        22,1,22,1,23,1,23,1,24,1,24,1,25,1,25,5,25,267,8,25,10,25,12,25,
        270,9,25,1,26,1,26,1,26,3,26,275,8,26,1,27,1,27,5,27,279,8,27,10,
        27,12,27,282,9,27,1,28,1,28,1,28,5,28,287,8,28,10,28,12,28,290,9,
        28,1,29,1,29,5,29,294,8,29,10,29,12,29,297,9,29,1,29,1,29,1,29,0,
        0,30,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,0,3,1,0,16,17,1,0,18,19,3,0,25,25,28,28,
        30,30,307,0,63,1,0,0,0,2,71,1,0,0,0,4,73,1,0,0,0,6,77,1,0,0,0,8,
        81,1,0,0,0,10,85,1,0,0,0,12,88,1,0,0,0,14,96,1,0,0,0,16,104,1,0,
        0,0,18,121,1,0,0,0,20,126,1,0,0,0,22,129,1,0,0,0,24,142,1,0,0,0,
        26,172,1,0,0,0,28,193,1,0,0,0,30,209,1,0,0,0,32,216,1,0,0,0,34,222,
        1,0,0,0,36,224,1,0,0,0,38,232,1,0,0,0,40,248,1,0,0,0,42,255,1,0,
        0,0,44,257,1,0,0,0,46,260,1,0,0,0,48,262,1,0,0,0,50,264,1,0,0,0,
        52,274,1,0,0,0,54,276,1,0,0,0,56,283,1,0,0,0,58,291,1,0,0,0,60,62,
        3,2,1,0,61,60,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,
        64,1,1,0,0,0,65,63,1,0,0,0,66,72,3,12,6,0,67,72,3,14,7,0,68,72,3,
        4,2,0,69,72,3,24,12,0,70,72,3,26,13,0,71,66,1,0,0,0,71,67,1,0,0,
        0,71,68,1,0,0,0,71,69,1,0,0,0,71,70,1,0,0,0,72,3,1,0,0,0,73,74,5,
        1,0,0,74,75,3,34,17,0,75,76,5,2,0,0,76,5,1,0,0,0,77,78,5,3,0,0,78,
        79,3,34,17,0,79,80,5,2,0,0,80,7,1,0,0,0,81,82,5,4,0,0,82,83,3,46,
        23,0,83,84,3,28,14,0,84,9,1,0,0,0,85,86,3,42,21,0,86,87,3,44,22,
        0,87,11,1,0,0,0,88,89,3,10,5,0,89,92,5,5,0,0,90,93,3,34,17,0,91,
        93,3,8,4,0,92,90,1,0,0,0,92,91,1,0,0,0,93,94,1,0,0,0,94,95,5,2,0,
        0,95,13,1,0,0,0,96,97,3,44,22,0,97,100,5,5,0,0,98,101,3,34,17,0,
        99,101,3,8,4,0,100,98,1,0,0,0,100,99,1,0,0,0,101,102,1,0,0,0,102,
        103,5,2,0,0,103,15,1,0,0,0,104,117,5,6,0,0,105,106,3,42,21,0,106,
        113,3,44,22,0,107,108,5,7,0,0,108,109,3,42,21,0,109,110,3,44,22,
        0,110,112,1,0,0,0,111,107,1,0,0,0,112,115,1,0,0,0,113,111,1,0,0,
        0,113,114,1,0,0,0,114,118,1,0,0,0,115,113,1,0,0,0,116,118,1,0,0,
        0,117,105,1,0,0,0,117,116,1,0,0,0,118,119,1,0,0,0,119,120,5,8,0,
        0,120,17,1,0,0,0,121,122,5,9,0,0,122,123,3,42,21,0,123,124,3,48,
        24,0,124,125,3,16,8,0,125,19,1,0,0,0,126,127,3,18,9,0,127,128,3,
        22,11,0,128,21,1,0,0,0,129,133,5,10,0,0,130,132,3,2,1,0,131,130,
        1,0,0,0,132,135,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,138,
        1,0,0,0,135,133,1,0,0,0,136,139,3,6,3,0,137,139,1,0,0,0,138,136,
        1,0,0,0,138,137,1,0,0,0,139,140,1,0,0,0,140,141,5,11,0,0,141,23,
        1,0,0,0,142,143,5,12,0,0,143,147,3,46,23,0,144,145,5,13,0,0,145,
        148,3,46,23,0,146,148,1,0,0,0,147,144,1,0,0,0,147,146,1,0,0,0,148,
        149,1,0,0,0,149,155,5,10,0,0,150,151,3,10,5,0,151,152,5,2,0,0,152,
        154,1,0,0,0,153,150,1,0,0,0,154,157,1,0,0,0,155,153,1,0,0,0,155,
        156,1,0,0,0,156,161,1,0,0,0,157,155,1,0,0,0,158,160,3,12,6,0,159,
        158,1,0,0,0,160,163,1,0,0,0,161,159,1,0,0,0,161,162,1,0,0,0,162,
        167,1,0,0,0,163,161,1,0,0,0,164,166,3,20,10,0,165,164,1,0,0,0,166,
        169,1,0,0,0,167,165,1,0,0,0,167,168,1,0,0,0,168,170,1,0,0,0,169,
        167,1,0,0,0,170,171,5,11,0,0,171,25,1,0,0,0,172,173,5,14,0,0,173,
        174,3,46,23,0,174,180,5,10,0,0,175,176,3,10,5,0,176,177,5,2,0,0,
        177,179,1,0,0,0,178,175,1,0,0,0,179,182,1,0,0,0,180,178,1,0,0,0,
        180,181,1,0,0,0,181,188,1,0,0,0,182,180,1,0,0,0,183,184,3,18,9,0,
        184,185,5,2,0,0,185,187,1,0,0,0,186,183,1,0,0,0,187,190,1,0,0,0,
        188,186,1,0,0,0,188,189,1,0,0,0,189,191,1,0,0,0,190,188,1,0,0,0,
        191,192,5,11,0,0,192,27,1,0,0,0,193,203,5,6,0,0,194,199,3,34,17,
        0,195,196,5,7,0,0,196,198,3,34,17,0,197,195,1,0,0,0,198,201,1,0,
        0,0,199,197,1,0,0,0,199,200,1,0,0,0,200,204,1,0,0,0,201,199,1,0,
        0,0,202,204,1,0,0,0,203,194,1,0,0,0,203,202,1,0,0,0,204,205,1,0,
        0,0,205,206,5,8,0,0,206,29,1,0,0,0,207,210,3,46,23,0,208,210,3,44,
        22,0,209,207,1,0,0,0,209,208,1,0,0,0,210,211,1,0,0,0,211,212,5,15,
        0,0,212,213,3,44,22,0,213,31,1,0,0,0,214,217,3,46,23,0,215,217,3,
        44,22,0,216,214,1,0,0,0,216,215,1,0,0,0,217,218,1,0,0,0,218,219,
        5,15,0,0,219,220,3,48,24,0,220,221,3,28,14,0,221,33,1,0,0,0,222,
        223,3,36,18,0,223,35,1,0,0,0,224,229,3,38,19,0,225,226,7,0,0,0,226,
        228,3,38,19,0,227,225,1,0,0,0,228,231,1,0,0,0,229,227,1,0,0,0,229,
        230,1,0,0,0,230,37,1,0,0,0,231,229,1,0,0,0,232,237,3,40,20,0,233,
        234,7,1,0,0,234,236,3,40,20,0,235,233,1,0,0,0,236,239,1,0,0,0,237,
        235,1,0,0,0,237,238,1,0,0,0,238,39,1,0,0,0,239,237,1,0,0,0,240,249,
        3,44,22,0,241,249,3,52,26,0,242,249,3,30,15,0,243,249,3,32,16,0,
        244,245,5,6,0,0,245,246,3,34,17,0,246,247,5,8,0,0,247,249,1,0,0,
        0,248,240,1,0,0,0,248,241,1,0,0,0,248,242,1,0,0,0,248,243,1,0,0,
        0,248,244,1,0,0,0,249,41,1,0,0,0,250,256,5,20,0,0,251,256,5,21,0,
        0,252,256,5,22,0,0,253,256,5,23,0,0,254,256,3,46,23,0,255,250,1,
        0,0,0,255,251,1,0,0,0,255,252,1,0,0,0,255,253,1,0,0,0,255,254,1,
        0,0,0,256,43,1,0,0,0,257,258,5,24,0,0,258,259,3,50,25,0,259,45,1,
        0,0,0,260,261,3,50,25,0,261,47,1,0,0,0,262,263,3,50,25,0,263,49,
        1,0,0,0,264,268,5,28,0,0,265,267,7,2,0,0,266,265,1,0,0,0,267,270,
        1,0,0,0,268,266,1,0,0,0,268,269,1,0,0,0,269,51,1,0,0,0,270,268,1,
        0,0,0,271,275,3,54,27,0,272,275,3,56,28,0,273,275,3,58,29,0,274,
        271,1,0,0,0,274,272,1,0,0,0,274,273,1,0,0,0,275,53,1,0,0,0,276,280,
        5,29,0,0,277,279,5,30,0,0,278,277,1,0,0,0,279,282,1,0,0,0,280,278,
        1,0,0,0,280,281,1,0,0,0,281,55,1,0,0,0,282,280,1,0,0,0,283,284,3,
        54,27,0,284,288,5,15,0,0,285,287,5,30,0,0,286,285,1,0,0,0,287,290,
        1,0,0,0,288,286,1,0,0,0,288,289,1,0,0,0,289,57,1,0,0,0,290,288,1,
        0,0,0,291,295,5,26,0,0,292,294,5,31,0,0,293,292,1,0,0,0,294,297,
        1,0,0,0,295,293,1,0,0,0,295,296,1,0,0,0,296,298,1,0,0,0,297,295,
        1,0,0,0,298,299,5,26,0,0,299,59,1,0,0,0,27,63,71,92,100,113,117,
        133,138,147,155,161,167,180,188,199,203,209,216,229,237,248,255,
        268,274,280,288,295
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
                     "'none'", "'$'", "'_'", "'\"'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "Whitespace", 
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
    RULE_identifier = 25
    RULE_literal = 26
    RULE_chunkLiteral = 27
    RULE_fractionLiteral = 28
    RULE_stringLiteral = 29

    ruleNames =  [ "program", "statement", "showStatement", "returnStatement", 
                   "createClassStatement", "variableSignature", "variableDeclaration", 
                   "assignment", "parametersInit", "methodSignature", "methodDeclaration", 
                   "methodBlock", "classDeclaration", "templateDeclaration", 
                   "parametersCall", "classVariableAccess", "classMethodAccess", 
                   "expression", "additiveExpression", "multiplicativeExpression", 
                   "term", "type", "variableName", "className", "methodName", 
                   "identifier", "literal", "chunkLiteral", "fractionLiteral", 
                   "stringLiteral" ]

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
    T__24=25
    T__25=26
    Whitespace=27
    Letter=28
    NonZeroDigit=29
    Digit=30
    CharacterExceptQuote=31
    Character=32
    BlockComment=33
    LineComment=34

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
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 300961794) != 0):
                self.state = 60
                self.statement()
                self.state = 65
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
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 22, 23, 28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.variableDeclaration()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.assignment()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.showStatement()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 69
                self.classDeclaration()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 5)
                self.state = 70
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
            self.state = 73
            self.match(TypeCheckerParser.T__0)
            self.state = 74
            self.expression()
            self.state = 75
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
            self.state = 77
            self.match(TypeCheckerParser.T__2)
            self.state = 78
            self.expression()
            self.state = 79
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


        def parametersCall(self):
            return self.getTypedRuleContext(TypeCheckerParser.ParametersCallContext,0)


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
            self.state = 81
            self.match(TypeCheckerParser.T__3)
            self.state = 82
            self.className()
            self.state = 83
            self.parametersCall()
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
            self.state = 85
            self.type_()
            self.state = 86
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
            self.state = 88
            self.variableSignature()
            self.state = 89
            self.match(TypeCheckerParser.T__4)
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 24, 26, 28, 29]:
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
            self.state = 96
            self.variableName()
            self.state = 97
            self.match(TypeCheckerParser.T__4)
            self.state = 100
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 24, 26, 28, 29]:
                self.state = 98
                self.expression()
                pass
            elif token in [4]:
                self.state = 99
                self.createClassStatement()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 102
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
            self.state = 104
            self.match(TypeCheckerParser.T__5)
            self.state = 117
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 22, 23, 28]:
                self.state = 105
                self.type_()
                self.state = 106
                self.variableName()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 107
                    self.match(TypeCheckerParser.T__6)
                    self.state = 108
                    self.type_()
                    self.state = 109
                    self.variableName()
                    self.state = 115
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [8]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 119
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
            self.state = 121
            self.match(TypeCheckerParser.T__8)
            self.state = 122
            self.type_()
            self.state = 123
            self.methodName()
            self.state = 124
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
            self.state = 126
            self.methodSignature()
            self.state = 127
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
            self.state = 129
            self.match(TypeCheckerParser.T__9)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 300961794) != 0):
                self.state = 130
                self.statement()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 138
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 136
                self.returnStatement()
                pass
            elif token in [11]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 140
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
            self.state = 142
            self.match(TypeCheckerParser.T__11)
            self.state = 143
            self.className()
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.state = 144
                self.match(TypeCheckerParser.T__12)
                self.state = 145
                self.className()
                pass
            elif token in [10]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 149
            self.match(TypeCheckerParser.T__9)
            self.state = 155
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 150
                    self.variableSignature()
                    self.state = 151
                    self.match(TypeCheckerParser.T__1) 
                self.state = 157
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 284164096) != 0):
                self.state = 158
                self.variableDeclaration()
                self.state = 163
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 164
                self.methodDeclaration()
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 170
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
            self.state = 172
            self.match(TypeCheckerParser.T__13)
            self.state = 173
            self.className()
            self.state = 174
            self.match(TypeCheckerParser.T__9)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 284164096) != 0):
                self.state = 175
                self.variableSignature()
                self.state = 176
                self.match(TypeCheckerParser.T__1)
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 183
                self.methodSignature()
                self.state = 184
                self.match(TypeCheckerParser.T__1)
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 191
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
            self.state = 193
            self.match(TypeCheckerParser.T__5)
            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 24, 26, 28, 29]:
                self.state = 194
                self.expression()
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 195
                    self.match(TypeCheckerParser.T__6)
                    self.state = 196
                    self.expression()
                    self.state = 201
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [8]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 205
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
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.state = 207
                self.className()
                pass
            elif token in [24]:
                self.state = 208
                self.variableName()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 211
            self.match(TypeCheckerParser.T__14)
            self.state = 212
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
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.state = 214
                self.className()
                pass
            elif token in [24]:
                self.state = 215
                self.variableName()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 218
            self.match(TypeCheckerParser.T__14)
            self.state = 219
            self.methodName()
            self.state = 220
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
            self.state = 222
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
            self.state = 224
            self.multiplicativeExpression()
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16 or _la==17:
                self.state = 225
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 226
                self.multiplicativeExpression()
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
            self.state = 232
            self.term()
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18 or _la==19:
                self.state = 233
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 234
                self.term()
                self.state = 239
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
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.variableName()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 242
                self.classVariableAccess()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 243
                self.classMethodAccess()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 244
                self.match(TypeCheckerParser.T__5)
                self.state = 245
                self.expression()
                self.state = 246
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
            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.match(TypeCheckerParser.T__19)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.match(TypeCheckerParser.T__20)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 252
                self.match(TypeCheckerParser.T__21)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 253
                self.match(TypeCheckerParser.T__22)
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 5)
                self.state = 254
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

        def identifier(self):
            return self.getTypedRuleContext(TypeCheckerParser.IdentifierContext,0)


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
            self.state = 257
            self.match(TypeCheckerParser.T__23)
            self.state = 258
            self.identifier()
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

        def identifier(self):
            return self.getTypedRuleContext(TypeCheckerParser.IdentifierContext,0)


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
            self.state = 260
            self.identifier()
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

        def identifier(self):
            return self.getTypedRuleContext(TypeCheckerParser.IdentifierContext,0)


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
            self.state = 262
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Letter(self, i:int=None):
            if i is None:
                return self.getTokens(TypeCheckerParser.Letter)
            else:
                return self.getToken(TypeCheckerParser.Letter, i)

        def Digit(self, i:int=None):
            if i is None:
                return self.getTokens(TypeCheckerParser.Digit)
            else:
                return self.getToken(TypeCheckerParser.Digit, i)

        def getRuleIndex(self):
            return TypeCheckerParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = TypeCheckerParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(TypeCheckerParser.Letter)
            self.state = 268
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 265
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1375731712) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 270
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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

        def chunkLiteral(self):
            return self.getTypedRuleContext(TypeCheckerParser.ChunkLiteralContext,0)


        def fractionLiteral(self):
            return self.getTypedRuleContext(TypeCheckerParser.FractionLiteralContext,0)


        def stringLiteral(self):
            return self.getTypedRuleContext(TypeCheckerParser.StringLiteralContext,0)


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
        self.enterRule(localctx, 52, self.RULE_literal)
        try:
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.chunkLiteral()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 272
                self.fractionLiteral()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 273
                self.stringLiteral()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChunkLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NonZeroDigit(self):
            return self.getToken(TypeCheckerParser.NonZeroDigit, 0)

        def Digit(self, i:int=None):
            if i is None:
                return self.getTokens(TypeCheckerParser.Digit)
            else:
                return self.getToken(TypeCheckerParser.Digit, i)

        def getRuleIndex(self):
            return TypeCheckerParser.RULE_chunkLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChunkLiteral" ):
                listener.enterChunkLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChunkLiteral" ):
                listener.exitChunkLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChunkLiteral" ):
                return visitor.visitChunkLiteral(self)
            else:
                return visitor.visitChildren(self)




    def chunkLiteral(self):

        localctx = TypeCheckerParser.ChunkLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_chunkLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.match(TypeCheckerParser.NonZeroDigit)
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 277
                self.match(TypeCheckerParser.Digit)
                self.state = 282
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FractionLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def chunkLiteral(self):
            return self.getTypedRuleContext(TypeCheckerParser.ChunkLiteralContext,0)


        def Digit(self, i:int=None):
            if i is None:
                return self.getTokens(TypeCheckerParser.Digit)
            else:
                return self.getToken(TypeCheckerParser.Digit, i)

        def getRuleIndex(self):
            return TypeCheckerParser.RULE_fractionLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFractionLiteral" ):
                listener.enterFractionLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFractionLiteral" ):
                listener.exitFractionLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFractionLiteral" ):
                return visitor.visitFractionLiteral(self)
            else:
                return visitor.visitChildren(self)




    def fractionLiteral(self):

        localctx = TypeCheckerParser.FractionLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_fractionLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.chunkLiteral()
            self.state = 284
            self.match(TypeCheckerParser.T__14)
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 285
                self.match(TypeCheckerParser.Digit)
                self.state = 290
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CharacterExceptQuote(self, i:int=None):
            if i is None:
                return self.getTokens(TypeCheckerParser.CharacterExceptQuote)
            else:
                return self.getToken(TypeCheckerParser.CharacterExceptQuote, i)

        def getRuleIndex(self):
            return TypeCheckerParser.RULE_stringLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteral" ):
                listener.enterStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteral" ):
                listener.exitStringLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLiteral" ):
                return visitor.visitStringLiteral(self)
            else:
                return visitor.visitChildren(self)




    def stringLiteral(self):

        localctx = TypeCheckerParser.StringLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_stringLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.match(TypeCheckerParser.T__25)
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 292
                self.match(TypeCheckerParser.CharacterExceptQuote)
                self.state = 297
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 298
            self.match(TypeCheckerParser.T__25)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





