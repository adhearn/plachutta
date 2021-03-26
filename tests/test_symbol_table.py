import os
from antlr4 import *
from TACLexer import TACLexer
from TACParser import TACParser
from interpreter import AnalysisPhase, SymbolTable


class TestSymbolTable:

    def test_no_globals(self):
        prog = """@l1: %t1 = 4
        %t2 = %t1 + 3
        """
        input_stream = InputStream(prog)
        lexer = TACLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = TACParser(token_stream)
        tree = parser.tacFile()
        walker = ParseTreeWalker()
        analysis = AnalysisPhase()
        walker.walk(analysis, tree)
        st = analysis.symbol_table
        assert len(st.globals()) == 0
        assert len(st.variables()) == 2

    def test_single_global(self):
        prog = """
        @l1: $t1 = 4
        %t2 = $t1 + 3
        """
        input_stream = InputStream(prog)
        lexer = TACLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = TACParser(token_stream)
        tree = parser.tacFile()
        walker = ParseTreeWalker()
        analysis = AnalysisPhase()
        walker.walk(analysis, tree)
        st = analysis.symbol_table
        assert len(st.globals()) == 1
        assert len(st.variables()) == 2

    def test_multiple_globals(self):
        prog = """@l1: $t1 = 4
        $t2 = $t1 + 3
        """
        input_stream = InputStream(prog)
        lexer = TACLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = TACParser(token_stream)
        tree = parser.tacFile()
        walker = ParseTreeWalker()
        analysis = AnalysisPhase()
        walker.walk(analysis, tree)
        st = analysis.symbol_table
        assert len(st.globals()) == 2
        assert len(st.variables()) == 2
