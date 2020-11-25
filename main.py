import sys
from antlr4 import *
from TACLexer import TACLexer
from TACParser import TACParser
from interpreter import AnalysisPhase, Interpreter


def main(argv):
    input_stream = FileStream(argv[1])

    lexer = TACLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = TACParser(token_stream)
    tree = parser.tacFile()
    walker = ParseTreeWalker()
    analysis = AnalysisPhase()
    walker.walk(analysis, tree)
    interpreter = Interpreter(analysis.instructions, analysis.labels)
    interpreter.eval()


if __name__ == "__main__":
    main(sys.argv)
