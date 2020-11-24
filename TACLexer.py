# Generated from TAC.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\24")
        buf.write("c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\21\3\21\7\21V\n\21\f\21\16")
        buf.write("\21Y\13\21\3\22\6\22\\\n\22\r\22\16\22]\3\23\3\23\3\23")
        buf.write("\3\23\2\2\24\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\3\2\6\3")
        buf.write("\2c|\5\2\62;C\\c|\3\2\62;\4\2\13\13\"\"\2d\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\3\'")
        buf.write("\3\2\2\2\5)\3\2\2\2\7+\3\2\2\2\t\63\3\2\2\2\13\65\3\2")
        buf.write("\2\2\r8\3\2\2\2\17=\3\2\2\2\21?\3\2\2\2\23A\3\2\2\2\25")
        buf.write("C\3\2\2\2\27F\3\2\2\2\31I\3\2\2\2\33K\3\2\2\2\35N\3\2")
        buf.write("\2\2\37Q\3\2\2\2!S\3\2\2\2#[\3\2\2\2%_\3\2\2\2\'(\7\f")
        buf.write("\2\2(\4\3\2\2\2)*\7<\2\2*\6\3\2\2\2+,\7>\2\2,-\7P\2\2")
        buf.write("-.\7Q\2\2./\7\"\2\2/\60\7Q\2\2\60\61\7R\2\2\61\62\7@\2")
        buf.write("\2\62\b\3\2\2\2\63\64\7?\2\2\64\n\3\2\2\2\65\66\7k\2\2")
        buf.write("\66\67\7h\2\2\67\f\3\2\2\289\7l\2\29:\7w\2\2:;\7o\2\2")
        buf.write(";<\7r\2\2<\16\3\2\2\2=>\7,\2\2>\20\3\2\2\2?@\7-\2\2@\22")
        buf.write("\3\2\2\2AB\7/\2\2B\24\3\2\2\2CD\7?\2\2DE\7?\2\2E\26\3")
        buf.write("\2\2\2FG\7#\2\2GH\7?\2\2H\30\3\2\2\2IJ\7@\2\2J\32\3\2")
        buf.write("\2\2KL\7@\2\2LM\7?\2\2M\34\3\2\2\2NO\7>\2\2OP\7?\2\2P")
        buf.write("\36\3\2\2\2QR\7>\2\2R \3\2\2\2SW\t\2\2\2TV\t\3\2\2UT\3")
        buf.write("\2\2\2VY\3\2\2\2WU\3\2\2\2WX\3\2\2\2X\"\3\2\2\2YW\3\2")
        buf.write("\2\2Z\\\t\4\2\2[Z\3\2\2\2\\]\3\2\2\2][\3\2\2\2]^\3\2\2")
        buf.write("\2^$\3\2\2\2_`\t\5\2\2`a\3\2\2\2ab\b\23\2\2b&\3\2\2\2")
        buf.write("\5\2W]\3\b\2\2")
        return buf.getvalue()


class TACLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    ID = 16
    INT = 17
    WS = 18

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\n'", "':'", "'<NO OP>'", "'='", "'if'", "'jump'", "'*'", 
            "'+'", "'-'", "'=='", "'!='", "'>'", "'>='", "'<='", "'<'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "ID", "INT", "WS" ]

    grammarFileName = "TAC.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


