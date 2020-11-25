import os
from antlr4 import *
from TACLexer import TACLexer
from TACParser import TACParser
from interpreter import AnalysisPhase


class TestAnalysis:
    NO_ERROR_SAMPLES = ["fact5.tac", "jump1.tac", "one_plus_one.tac", "return1.tac", "sum_ten.tac",
                        "three_times_four.tac"]

    def test_no_errors(self):
        for filename in self.NO_ERROR_SAMPLES:
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
            assert not analysis.errors

    def test_jump_to_invalid_label(self):
        prog = """l1: t1 = 4
        t2 = t1 + 3
        jump l2
        """
        input_stream = InputStream(prog)
        lexer = TACLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = TACParser(token_stream)
        tree = parser.tacFile()
        walker = ParseTreeWalker()
        analysis = AnalysisPhase()
        walker.walk(analysis, tree)
        print(analysis.errors)
        assert len(analysis.errors) == 1

    def test_unused_label_warning(self):
        prog = """l1: t1 = 4
        t2 = t1 + 3
        """
        input_stream = InputStream(prog)
        lexer = TACLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = TACParser(token_stream)
        tree = parser.tacFile()
        walker = ParseTreeWalker()
        analysis = AnalysisPhase()
        walker.walk(analysis, tree)
        assert len(analysis.warnings) == 1
        assert len(analysis.errors) == 0

