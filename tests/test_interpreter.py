from antlr4 import *
from TACLexer import TACLexer
from TACParser import TACParser
from interpreter import AnalysisPhase, Interpreter

class TestInterpreter:

    def test_simple(self):
        prog = """a = 1
        b = 2
        c = a + b
        result = c
        """
        input_stream = InputStream(prog)
        lexer = TACLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = TACParser(token_stream)
        tree = parser.tacFile()
        walker = ParseTreeWalker()
        analysis = AnalysisPhase()
        walker.walk(analysis, tree)
        interpreter = Interpreter(analysis.instructions)
        interpreter.eval()
        result = interpreter.env["result"]
        assert result == 3
