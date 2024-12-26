import sys
from antlr4 import *
from TypeCheckerLexer import TypeCheckerLexer as ExprLexer
from TypeCheckerParser import TypeCheckerParser as ExprParser
from TypeChecker import TypeChecker
class SyntaxError(Exception):
    pass

class ThrowingErrorListener():
    def syntaxError(self, offendingSymbol, line, column, msg, e):
        raise SyntaxError(f"line {line}:{column} {msg}") from e

def main(argv):
    input_stream = FileStream(argv[1])
    # input_stream = FileStream('sample-code.txt')
    lexer = ExprLexer(input_stream)
    lexer.addErrorListener(ThrowingErrorListener)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    parser.addErrorListener(ThrowingErrorListener)
    try:
        tree = parser.program()
    except SyntaxError as e:
        print(f"Syntax error: \n{e}")


    type_checker = TypeChecker()
    try:
        type_checker.visit(tree)
        print("Type checking passed.")
    except Exception as e:
        print(f"Type checking failed: \n{e}")

    print(tree.toStringTree(recog=parser))
    print()
    print(tree.children)

if __name__ == '__main__':
    main(sys.argv)