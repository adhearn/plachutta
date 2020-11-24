import sys
from antlr4 import *
from TACLexer import TACLexer
from TACParser import TACParser
from interpreter import AnalysisPhase


def main(argv):
    input_stream = FileStream(argv[1])

    lexer = TACLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = TACParser(token_stream)
    tree = parser.tacFile()
    walker = ParseTreeWalker()
    analysis = AnalysisPhase()
    walker.walk(analysis, tree)
    print(analysis.labels)
    print(analysis.variables)
    print(analysis.errors)
    # interpreter = EvalPhase(analysis.instructions)
    # walker.walk(interpreter, tree)


if __name__ == "__main__":
    main(sys.argv)
