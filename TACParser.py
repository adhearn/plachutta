# Generated from TAC.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("J\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\6\2\30\n\2\r\2\16\2")
        buf.write("\31\3\3\3\3\3\3\3\4\3\4\7\4!\n\4\f\4\16\4$\13\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5")
        buf.write("\64\n\5\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\5\b@\n")
        buf.write("\b\3\t\3\t\3\n\3\n\3\13\3\13\5\13H\n\13\3\13\2\2\f\2\4")
        buf.write("\6\b\n\f\16\20\22\24\2\4\3\2\t\13\3\2\f\21\2F\2\27\3\2")
        buf.write("\2\2\4\33\3\2\2\2\6\"\3\2\2\2\b\63\3\2\2\2\n\65\3\2\2")
        buf.write("\2\f8\3\2\2\2\16?\3\2\2\2\20A\3\2\2\2\22C\3\2\2\2\24G")
        buf.write("\3\2\2\2\26\30\5\4\3\2\27\26\3\2\2\2\30\31\3\2\2\2\31")
        buf.write("\27\3\2\2\2\31\32\3\2\2\2\32\3\3\2\2\2\33\34\5\6\4\2\34")
        buf.write("\35\7\3\2\2\35\5\3\2\2\2\36\37\7\22\2\2\37!\7\4\2\2 \36")
        buf.write("\3\2\2\2!$\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#%\3\2\2\2$\"")
        buf.write("\3\2\2\2%&\5\b\5\2&\7\3\2\2\2\'\64\7\5\2\2()\5\f\7\2)")
        buf.write("*\7\6\2\2*+\5\16\b\2+\64\3\2\2\2,-\7\7\2\2-.\5\24\13\2")
        buf.write("./\5\22\n\2/\60\5\24\13\2\60\61\5\n\6\2\61\64\3\2\2\2")
        buf.write("\62\64\5\n\6\2\63\'\3\2\2\2\63(\3\2\2\2\63,\3\2\2\2\63")
        buf.write("\62\3\2\2\2\64\t\3\2\2\2\65\66\7\b\2\2\66\67\5\24\13\2")
        buf.write("\67\13\3\2\2\289\5\24\13\29\r\3\2\2\2:@\5\24\13\2;<\5")
        buf.write("\24\13\2<=\5\20\t\2=>\5\24\13\2>@\3\2\2\2?:\3\2\2\2?;")
        buf.write("\3\2\2\2@\17\3\2\2\2AB\t\2\2\2B\21\3\2\2\2CD\t\3\2\2D")
        buf.write("\23\3\2\2\2EH\7\22\2\2FH\7\23\2\2GE\3\2\2\2GF\3\2\2\2")
        buf.write("H\25\3\2\2\2\7\31\"\63?G")
        return buf.getvalue()


class TACParser ( Parser ):

    grammarFileName = "TAC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\n'", "':'", "'<NO OP>'", "'='", "'if'", 
                     "'jump'", "'*'", "'+'", "'-'", "'=='", "'!='", "'>'", 
                     "'>='", "'<='", "'<'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "INT", "WS" ]

    RULE_tacFile = 0
    RULE_tacLine = 1
    RULE_labeledInstruction = 2
    RULE_instruction = 3
    RULE_jump = 4
    RULE_lhs = 5
    RULE_rhs = 6
    RULE_binoperator = 7
    RULE_reloperator = 8
    RULE_address = 9

    ruleNames =  [ "tacFile", "tacLine", "labeledInstruction", "instruction", 
                   "jump", "lhs", "rhs", "binoperator", "reloperator", "address" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    ID=16
    INT=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TacFileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tacLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TACParser.TacLineContext)
            else:
                return self.getTypedRuleContext(TACParser.TacLineContext,i)


        def getRuleIndex(self):
            return TACParser.RULE_tacFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTacFile" ):
                listener.enterTacFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTacFile" ):
                listener.exitTacFile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTacFile" ):
                return visitor.visitTacFile(self)
            else:
                return visitor.visitChildren(self)




    def tacFile(self):

        localctx = TACParser.TacFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_tacFile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.tacLine()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TACParser.T__2) | (1 << TACParser.T__4) | (1 << TACParser.T__5) | (1 << TACParser.ID) | (1 << TACParser.INT))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TacLineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def labeledInstruction(self):
            return self.getTypedRuleContext(TACParser.LabeledInstructionContext,0)


        def getRuleIndex(self):
            return TACParser.RULE_tacLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTacLine" ):
                listener.enterTacLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTacLine" ):
                listener.exitTacLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTacLine" ):
                return visitor.visitTacLine(self)
            else:
                return visitor.visitChildren(self)




    def tacLine(self):

        localctx = TACParser.TacLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_tacLine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.labeledInstruction()
            self.state = 26
            self.match(TACParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabeledInstructionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruction(self):
            return self.getTypedRuleContext(TACParser.InstructionContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(TACParser.ID)
            else:
                return self.getToken(TACParser.ID, i)

        def getRuleIndex(self):
            return TACParser.RULE_labeledInstruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabeledInstruction" ):
                listener.enterLabeledInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabeledInstruction" ):
                listener.exitLabeledInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabeledInstruction" ):
                return visitor.visitLabeledInstruction(self)
            else:
                return visitor.visitChildren(self)




    def labeledInstruction(self):

        localctx = TACParser.LabeledInstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_labeledInstruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 28
                    self.match(TACParser.ID)
                    self.state = 29
                    self.match(TACParser.T__1) 
                self.state = 34
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 35
            self.instruction()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TACParser.RULE_instruction

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignmentContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def lhs(self):
            return self.getTypedRuleContext(TACParser.LhsContext,0)

        def rhs(self):
            return self.getTypedRuleContext(TACParser.RhsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)


    class UnconditionalJumpContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def jump(self):
            return self.getTypedRuleContext(TACParser.JumpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnconditionalJump" ):
                listener.enterUnconditionalJump(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnconditionalJump" ):
                listener.exitUnconditionalJump(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnconditionalJump" ):
                return visitor.visitUnconditionalJump(self)
            else:
                return visitor.visitChildren(self)


    class NoOpContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNoOp" ):
                listener.enterNoOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNoOp" ):
                listener.exitNoOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNoOp" ):
                return visitor.visitNoOp(self)
            else:
                return visitor.visitChildren(self)


    class ConditionalJumpContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def address(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TACParser.AddressContext)
            else:
                return self.getTypedRuleContext(TACParser.AddressContext,i)

        def reloperator(self):
            return self.getTypedRuleContext(TACParser.ReloperatorContext,0)

        def jump(self):
            return self.getTypedRuleContext(TACParser.JumpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalJump" ):
                listener.enterConditionalJump(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalJump" ):
                listener.exitConditionalJump(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionalJump" ):
                return visitor.visitConditionalJump(self)
            else:
                return visitor.visitChildren(self)



    def instruction(self):

        localctx = TACParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_instruction)
        try:
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TACParser.T__2]:
                localctx = TACParser.NoOpContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.match(TACParser.T__2)
                pass
            elif token in [TACParser.ID, TACParser.INT]:
                localctx = TACParser.AssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.lhs()
                self.state = 39
                self.match(TACParser.T__3)
                self.state = 40
                self.rhs()
                pass
            elif token in [TACParser.T__4]:
                localctx = TACParser.ConditionalJumpContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.match(TACParser.T__4)
                self.state = 43
                self.address()
                self.state = 44
                self.reloperator()
                self.state = 45
                self.address()
                self.state = 46
                self.jump()
                pass
            elif token in [TACParser.T__5]:
                localctx = TACParser.UnconditionalJumpContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 48
                self.jump()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JumpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def address(self):
            return self.getTypedRuleContext(TACParser.AddressContext,0)


        def getRuleIndex(self):
            return TACParser.RULE_jump

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJump" ):
                listener.enterJump(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJump" ):
                listener.exitJump(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJump" ):
                return visitor.visitJump(self)
            else:
                return visitor.visitChildren(self)




    def jump(self):

        localctx = TACParser.JumpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_jump)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(TACParser.T__5)
            self.state = 52
            self.address()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def address(self):
            return self.getTypedRuleContext(TACParser.AddressContext,0)


        def getRuleIndex(self):
            return TACParser.RULE_lhs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLhs" ):
                listener.enterLhs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLhs" ):
                listener.exitLhs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = TACParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.address()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RhsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TACParser.RULE_rhs

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RhsAddresContext(RhsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.RhsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def address(self):
            return self.getTypedRuleContext(TACParser.AddressContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRhsAddres" ):
                listener.enterRhsAddres(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRhsAddres" ):
                listener.exitRhsAddres(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRhsAddres" ):
                return visitor.visitRhsAddres(self)
            else:
                return visitor.visitChildren(self)


    class RhsBinopContext(RhsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.RhsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def address(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TACParser.AddressContext)
            else:
                return self.getTypedRuleContext(TACParser.AddressContext,i)

        def binoperator(self):
            return self.getTypedRuleContext(TACParser.BinoperatorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRhsBinop" ):
                listener.enterRhsBinop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRhsBinop" ):
                listener.exitRhsBinop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRhsBinop" ):
                return visitor.visitRhsBinop(self)
            else:
                return visitor.visitChildren(self)



    def rhs(self):

        localctx = TACParser.RhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_rhs)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = TACParser.RhsAddresContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.address()
                pass

            elif la_ == 2:
                localctx = TACParser.RhsBinopContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.address()
                self.state = 58
                self.binoperator()
                self.state = 59
                self.address()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinoperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TACParser.RULE_binoperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinoperator" ):
                listener.enterBinoperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinoperator" ):
                listener.exitBinoperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinoperator" ):
                return visitor.visitBinoperator(self)
            else:
                return visitor.visitChildren(self)




    def binoperator(self):

        localctx = TACParser.BinoperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_binoperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TACParser.T__6) | (1 << TACParser.T__7) | (1 << TACParser.T__8))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReloperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TACParser.RULE_reloperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReloperator" ):
                listener.enterReloperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReloperator" ):
                listener.exitReloperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReloperator" ):
                return visitor.visitReloperator(self)
            else:
                return visitor.visitChildren(self)




    def reloperator(self):

        localctx = TACParser.ReloperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_reloperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TACParser.T__9) | (1 << TACParser.T__10) | (1 << TACParser.T__11) | (1 << TACParser.T__12) | (1 << TACParser.T__13) | (1 << TACParser.T__14))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddressContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TACParser.RULE_address

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IntegerContext(AddressContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.AddressContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(TACParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierContext(AddressContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.AddressContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(TACParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)



    def address(self):

        localctx = TACParser.AddressContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_address)
        try:
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TACParser.ID]:
                localctx = TACParser.IdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.match(TACParser.ID)
                pass
            elif token in [TACParser.INT]:
                localctx = TACParser.IntegerContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.match(TACParser.INT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





