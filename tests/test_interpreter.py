import os
from antlr4 import *
from TACLexer import TACLexer
from TACParser import TACParser
from interpreter import AnalysisPhase, Interpreter

class TestInterpreter:
    #
    # def test_simple(self):
    #     prog = """a = 1
    #     b = 2
    #     c = a + b
    #     result = c
    #     """
    #     input_stream = InputStream(prog)
    #     lexer = TACLexer(input_stream)
    #     token_stream = CommonTokenStream(lexer)
    #     parser = TACParser(token_stream)
    #     tree = parser.tacFile()
    #     walker = ParseTreeWalker()
    #     analysis = AnalysisPhase()
    #     walker.walk(analysis, tree)
    #     interpreter = Interpreter(analysis.instructions, analysis.labels)
    #     interpreter.eval()
    #     result = interpreter.env["result"]
    #     assert result == 3

    def _test_sample_file(self, filename, expected, result_var):
        cur_dir = os.path.dirname(__file__)
        test_filepath = os.path.join(cur_dir, "samples", filename)
        input_stream = FileStream(test_filepath)
        lexer = TACLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = TACParser(token_stream)
        tree = parser.tacFile()
        walker = ParseTreeWalker()
        analysis = AnalysisPhase()
        walker.walk(analysis, tree)
        interpreter = Interpreter(analysis.instructions, analysis.labels)
        interpreter.eval()
        result = interpreter.env[result_var]
        assert result == expected

    def test_return1(self):
        self._test_sample_file("return1.tac", 1, "rdi")

    def test_jump1(self):
        self._test_sample_file("jump1.tac", 5, "rdi")

    def test_one_plus_one(self):
        self._test_sample_file("one_plus_one.tac", 2, "rdi")

    def test_three_times_four(self):
        self._test_sample_file("three_times_four.tac", 12, "rdi")

    def test_sum_ten(self):
        self._test_sample_file("sum_ten.tac", 55, "rdi")

    def test_fact5(self):
        self._test_sample_file("fact5.tac", 120, "rdi")
