import sys
from antlr4 import *
from TypeCheckerLexer import TypeCheckerLexer as ExprLexer
from TypeCheckerParser import TypeCheckerParser as ExprParser

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))
    print()
    print(tree.children)
    

if __name__ == '__main__':
    main(sys.argv)