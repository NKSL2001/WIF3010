import sys
from antlr4 import *
from TypeCheckerLexer import TypeCheckerLexer as ExprLexer
from TypeCheckerParser import TypeCheckerParser as ExprParser
from TypeChecker import TypeChecker

def main(argv):
    input_stream = FileStream(argv[1])
    # input_stream = FileStream('sample-code.txt')
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.program()

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