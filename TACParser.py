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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\30")
        buf.write("g\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\6\2\36\n\2\r\2\16\2\37\3\3\3\3\3\3\3\4\3\4\3\4")
        buf.write("\7\4(\n\4\f\4\16\4+\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\5\59\n\5\3\6\3\6\3\6\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\5\bF\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\tW\n\t\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\5\16e\n\16")
        buf.write("\3\16\2\2\17\2\4\6\b\n\f\16\20\22\24\26\30\32\2\4\3\2")
        buf.write("\f\16\3\2\17\24\2d\2\35\3\2\2\2\4!\3\2\2\2\6)\3\2\2\2")
        buf.write("\b8\3\2\2\2\n:\3\2\2\2\f=\3\2\2\2\16E\3\2\2\2\20V\3\2")
        buf.write("\2\2\22X\3\2\2\2\24\\\3\2\2\2\26^\3\2\2\2\30`\3\2\2\2")
        buf.write("\32d\3\2\2\2\34\36\5\4\3\2\35\34\3\2\2\2\36\37\3\2\2\2")
        buf.write("\37\35\3\2\2\2\37 \3\2\2\2 \3\3\2\2\2!\"\5\6\4\2\"#\7")
        buf.write("\3\2\2#\5\3\2\2\2$%\5\f\7\2%&\7\4\2\2&(\3\2\2\2\'$\3\2")
        buf.write("\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*,\3\2\2\2+)\3\2\2")
        buf.write("\2,-\5\b\5\2-\7\3\2\2\2.9\7\5\2\2/\60\5\16\b\2\60\61\7")
        buf.write("\6\2\2\61\62\5\20\t\2\629\3\2\2\2\63\64\7\7\2\2\64\65")
        buf.write("\5\22\n\2\65\66\5\n\6\2\669\3\2\2\2\679\5\n\6\28.\3\2")
        buf.write("\2\28/\3\2\2\28\63\3\2\2\28\67\3\2\2\29\t\3\2\2\2:;\7")
        buf.write("\b\2\2;<\5\f\7\2<\13\3\2\2\2=>\7\26\2\2>\r\3\2\2\2?F\5")
        buf.write("\32\16\2@A\5\32\16\2AB\7\t\2\2BC\5\32\16\2CD\7\n\2\2D")
        buf.write("F\3\2\2\2E?\3\2\2\2E@\3\2\2\2F\17\3\2\2\2GW\5\32\16\2")
        buf.write("HI\5\32\16\2IJ\5\24\13\2JK\5\32\16\2KW\3\2\2\2LM\5\30")
        buf.write("\r\2MN\5\32\16\2NW\3\2\2\2OP\5\32\16\2PQ\7\t\2\2QR\5\32")
        buf.write("\16\2RS\7\n\2\2SW\3\2\2\2TU\7\13\2\2UW\7\26\2\2VG\3\2")
        buf.write("\2\2VH\3\2\2\2VL\3\2\2\2VO\3\2\2\2VT\3\2\2\2W\21\3\2\2")
        buf.write("\2XY\5\32\16\2YZ\5\26\f\2Z[\5\32\16\2[\23\3\2\2\2\\]\t")
        buf.write("\2\2\2]\25\3\2\2\2^_\t\3\2\2_\27\3\2\2\2`a\7\25\2\2a\31")
        buf.write("\3\2\2\2be\7\26\2\2ce\7\27\2\2db\3\2\2\2dc\3\2\2\2e\33")
        buf.write("\3\2\2\2\b\37)8EVd")
        return buf.getvalue()


class TACParser ( Parser ):

    grammarFileName = "TAC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\n'", "':'", "'<NO OP>'", "'='", "'if'", 
                     "'jump'", "'['", "']'", "'&'", "'*'", "'+'", "'-'", 
                     "'=='", "'!='", "'>'", "'>='", "'<='", "'<'", "'memrequest'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "INT", "WS" ]

    RULE_tacFile = 0
    RULE_tacLine = 1
    RULE_labeledInstruction = 2
    RULE_instruction = 3
    RULE_jump = 4
    RULE_label = 5
    RULE_lhs = 6
    RULE_rhs = 7
    RULE_relop = 8
    RULE_binoperator = 9
    RULE_reloperator = 10
    RULE_unoperator = 11
    RULE_address = 12

    ruleNames =  [ "tacFile", "tacLine", "labeledInstruction", "instruction", 
                   "jump", "label", "lhs", "rhs", "relop", "binoperator", 
                   "reloperator", "unoperator", "address" ]

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
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    ID=20
    INT=21
    WS=22

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
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.tacLine()
                self.state = 29 
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
            self.state = 31
            self.labeledInstruction()
            self.state = 32
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


        def label(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TACParser.LabelContext)
            else:
                return self.getTypedRuleContext(TACParser.LabelContext,i)


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
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 34
                    self.label()
                    self.state = 35
                    self.match(TACParser.T__1) 
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 42
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

        def relop(self):
            return self.getTypedRuleContext(TACParser.RelopContext,0)

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
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TACParser.T__2]:
                localctx = TACParser.NoOpContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.match(TACParser.T__2)
                pass
            elif token in [TACParser.ID, TACParser.INT]:
                localctx = TACParser.AssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.lhs()
                self.state = 46
                self.match(TACParser.T__3)
                self.state = 47
                self.rhs()
                pass
            elif token in [TACParser.T__4]:
                localctx = TACParser.ConditionalJumpContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.match(TACParser.T__4)
                self.state = 50
                self.relop()
                self.state = 51
                self.jump()
                pass
            elif token in [TACParser.T__5]:
                localctx = TACParser.UnconditionalJumpContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 53
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

        def label(self):
            return self.getTypedRuleContext(TACParser.LabelContext,0)


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
            self.state = 56
            self.match(TACParser.T__5)
            self.state = 57
            self.label()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TACParser.ID, 0)

        def getRuleIndex(self):
            return TACParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = TACParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(TACParser.ID)
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


        def getRuleIndex(self):
            return TACParser.RULE_lhs

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class LhsIndexedContext(LhsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.LhsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def address(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TACParser.AddressContext)
            else:
                return self.getTypedRuleContext(TACParser.AddressContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLhsIndexed" ):
                listener.enterLhsIndexed(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLhsIndexed" ):
                listener.exitLhsIndexed(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhsIndexed" ):
                return visitor.visitLhsIndexed(self)
            else:
                return visitor.visitChildren(self)


    class LhsSimpleContext(LhsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.LhsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def address(self):
            return self.getTypedRuleContext(TACParser.AddressContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLhsSimple" ):
                listener.enterLhsSimple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLhsSimple" ):
                listener.exitLhsSimple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhsSimple" ):
                return visitor.visitLhsSimple(self)
            else:
                return visitor.visitChildren(self)



    def lhs(self):

        localctx = TACParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_lhs)
        try:
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = TACParser.LhsSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.address()
                pass

            elif la_ == 2:
                localctx = TACParser.LhsIndexedContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.address()
                self.state = 63
                self.match(TACParser.T__6)
                self.state = 64
                self.address()
                self.state = 65
                self.match(TACParser.T__7)
                pass


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


    class RhsIndexedContext(RhsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.RhsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def address(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TACParser.AddressContext)
            else:
                return self.getTypedRuleContext(TACParser.AddressContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRhsIndexed" ):
                listener.enterRhsIndexed(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRhsIndexed" ):
                listener.exitRhsIndexed(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRhsIndexed" ):
                return visitor.visitRhsIndexed(self)
            else:
                return visitor.visitChildren(self)


    class RhsUnopContext(RhsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.RhsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unoperator(self):
            return self.getTypedRuleContext(TACParser.UnoperatorContext,0)

        def address(self):
            return self.getTypedRuleContext(TACParser.AddressContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRhsUnop" ):
                listener.enterRhsUnop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRhsUnop" ):
                listener.exitRhsUnop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRhsUnop" ):
                return visitor.visitRhsUnop(self)
            else:
                return visitor.visitChildren(self)


    class RhsAddressContext(RhsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.RhsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def address(self):
            return self.getTypedRuleContext(TACParser.AddressContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRhsAddress" ):
                listener.enterRhsAddress(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRhsAddress" ):
                listener.exitRhsAddress(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRhsAddress" ):
                return visitor.visitRhsAddress(self)
            else:
                return visitor.visitChildren(self)


    class RhsAddressOfContext(RhsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.RhsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(TACParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRhsAddressOf" ):
                listener.enterRhsAddressOf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRhsAddressOf" ):
                listener.exitRhsAddressOf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRhsAddressOf" ):
                return visitor.visitRhsAddressOf(self)
            else:
                return visitor.visitChildren(self)



    def rhs(self):

        localctx = TACParser.RhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_rhs)
        try:
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = TACParser.RhsAddressContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.address()
                pass

            elif la_ == 2:
                localctx = TACParser.RhsBinopContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.address()
                self.state = 71
                self.binoperator()
                self.state = 72
                self.address()
                pass

            elif la_ == 3:
                localctx = TACParser.RhsUnopContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.unoperator()
                self.state = 75
                self.address()
                pass

            elif la_ == 4:
                localctx = TACParser.RhsIndexedContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 77
                self.address()
                self.state = 78
                self.match(TACParser.T__6)
                self.state = 79
                self.address()
                self.state = 80
                self.match(TACParser.T__7)
                pass

            elif la_ == 5:
                localctx = TACParser.RhsAddressOfContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 82
                self.match(TACParser.T__8)
                self.state = 83
                self.match(TACParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def address(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TACParser.AddressContext)
            else:
                return self.getTypedRuleContext(TACParser.AddressContext,i)


        def reloperator(self):
            return self.getTypedRuleContext(TACParser.ReloperatorContext,0)


        def getRuleIndex(self):
            return TACParser.RULE_relop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelop" ):
                listener.enterRelop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelop" ):
                listener.exitRelop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelop" ):
                return visitor.visitRelop(self)
            else:
                return visitor.visitChildren(self)




    def relop(self):

        localctx = TACParser.RelopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_relop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.address()
            self.state = 87
            self.reloperator()
            self.state = 88
            self.address()
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
        self.enterRule(localctx, 18, self.RULE_binoperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TACParser.T__9) | (1 << TACParser.T__10) | (1 << TACParser.T__11))) != 0)):
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
        self.enterRule(localctx, 20, self.RULE_reloperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TACParser.T__12) | (1 << TACParser.T__13) | (1 << TACParser.T__14) | (1 << TACParser.T__15) | (1 << TACParser.T__16) | (1 << TACParser.T__17))) != 0)):
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


    class UnoperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TACParser.RULE_unoperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnoperator" ):
                listener.enterUnoperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnoperator" ):
                listener.exitUnoperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnoperator" ):
                return visitor.visitUnoperator(self)
            else:
                return visitor.visitChildren(self)




    def unoperator(self):

        localctx = TACParser.UnoperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_unoperator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(TACParser.T__18)
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
        self.enterRule(localctx, 24, self.RULE_address)
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TACParser.ID]:
                localctx = TACParser.IdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.match(TACParser.ID)
                pass
            elif token in [TACParser.INT]:
                localctx = TACParser.IntegerContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 97
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





