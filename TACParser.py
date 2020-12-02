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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\33")
        buf.write("s\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\3\2\6\2 \n\2\r\2\16\2!\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\7\4*\n\4\f\4\16\4-\13\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5@\n\5")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\5\tP\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\5\nc\n\n\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\5\17q\n\17\3\17\2")
        buf.write("\2\20\2\4\6\b\n\f\16\20\22\24\26\30\32\34\2\5\3\2\17\21")
        buf.write("\3\2\22\27\4\2\t\t\30\30\2r\2\37\3\2\2\2\4#\3\2\2\2\6")
        buf.write("+\3\2\2\2\b?\3\2\2\2\nA\3\2\2\2\fD\3\2\2\2\16G\3\2\2\2")
        buf.write("\20O\3\2\2\2\22b\3\2\2\2\24d\3\2\2\2\26h\3\2\2\2\30j\3")
        buf.write("\2\2\2\32l\3\2\2\2\34p\3\2\2\2\36 \5\4\3\2\37\36\3\2\2")
        buf.write("\2 !\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"\3\3\2\2\2#$\5\6")
        buf.write("\4\2$%\7\3\2\2%\5\3\2\2\2&\'\5\16\b\2\'(\7\4\2\2(*\3\2")
        buf.write("\2\2)&\3\2\2\2*-\3\2\2\2+)\3\2\2\2+,\3\2\2\2,.\3\2\2\2")
        buf.write("-+\3\2\2\2./\5\b\5\2/\7\3\2\2\2\60@\7\5\2\2\61\62\5\20")
        buf.write("\t\2\62\63\7\6\2\2\63\64\5\22\n\2\64@\3\2\2\2\65\66\7")
        buf.write("\7\2\2\66\67\5\24\13\2\678\5\f\7\28@\3\2\2\29:\7\b\2\2")
        buf.write(":@\5\34\17\2;<\7\t\2\2<@\5\34\17\2=@\5\f\7\2>@\5\n\6\2")
        buf.write("?\60\3\2\2\2?\61\3\2\2\2?\65\3\2\2\2?9\3\2\2\2?;\3\2\2")
        buf.write("\2?=\3\2\2\2?>\3\2\2\2@\t\3\2\2\2AB\7\n\2\2BC\7\31\2\2")
        buf.write("C\13\3\2\2\2DE\7\13\2\2EF\5\16\b\2F\r\3\2\2\2GH\7\31\2")
        buf.write("\2H\17\3\2\2\2IP\5\34\17\2JK\5\34\17\2KL\7\f\2\2LM\5\34")
        buf.write("\17\2MN\7\r\2\2NP\3\2\2\2OI\3\2\2\2OJ\3\2\2\2P\21\3\2")
        buf.write("\2\2QR\7\16\2\2RS\5\16\b\2ST\5\34\17\2Tc\3\2\2\2Uc\5\34")
        buf.write("\17\2VW\5\34\17\2WX\5\26\f\2XY\5\34\17\2Yc\3\2\2\2Z[\5")
        buf.write("\32\16\2[\\\5\34\17\2\\c\3\2\2\2]^\5\34\17\2^_\7\f\2\2")
        buf.write("_`\5\34\17\2`a\7\r\2\2ac\3\2\2\2bQ\3\2\2\2bU\3\2\2\2b")
        buf.write("V\3\2\2\2bZ\3\2\2\2b]\3\2\2\2c\23\3\2\2\2de\5\34\17\2")
        buf.write("ef\5\30\r\2fg\5\34\17\2g\25\3\2\2\2hi\t\2\2\2i\27\3\2")
        buf.write("\2\2jk\t\3\2\2k\31\3\2\2\2lm\t\4\2\2m\33\3\2\2\2nq\7\31")
        buf.write("\2\2oq\7\32\2\2pn\3\2\2\2po\3\2\2\2q\35\3\2\2\2\b!+?O")
        buf.write("bp")
        return buf.getvalue()


class TACParser ( Parser ):

    grammarFileName = "TAC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\n'", "':'", "'<NO OP>'", "'='", "'if'", 
                     "'return'", "'param'", "'global'", "'jump'", "'['", 
                     "']'", "'call'", "'*'", "'+'", "'-'", "'=='", "'!='", 
                     "'>'", "'>='", "'<='", "'<'", "'memrequest'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "INT", 
                      "WS" ]

    RULE_tacFile = 0
    RULE_tacLine = 1
    RULE_labeledInstruction = 2
    RULE_instruction = 3
    RULE_globalDeclaration = 4
    RULE_jump = 5
    RULE_label = 6
    RULE_lhs = 7
    RULE_rhs = 8
    RULE_relop = 9
    RULE_binoperator = 10
    RULE_reloperator = 11
    RULE_unoperator = 12
    RULE_address = 13

    ruleNames =  [ "tacFile", "tacLine", "labeledInstruction", "instruction", 
                   "globalDeclaration", "jump", "label", "lhs", "rhs", "relop", 
                   "binoperator", "reloperator", "unoperator", "address" ]

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
    T__19=20
    T__20=21
    T__21=22
    ID=23
    INT=24
    WS=25

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
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.tacLine()
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TACParser.T__2) | (1 << TACParser.T__4) | (1 << TACParser.T__5) | (1 << TACParser.T__6) | (1 << TACParser.T__7) | (1 << TACParser.T__8) | (1 << TACParser.ID) | (1 << TACParser.INT))) != 0)):
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
            self.state = 33
            self.labeledInstruction()
            self.state = 34
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
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 36
                    self.label()
                    self.state = 37
                    self.match(TACParser.T__1) 
                self.state = 43
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 44
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


    class GlobalInstructionContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def globalDeclaration(self):
            return self.getTypedRuleContext(TACParser.GlobalDeclarationContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobalInstruction" ):
                listener.enterGlobalInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobalInstruction" ):
                listener.exitGlobalInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobalInstruction" ):
                return visitor.visitGlobalInstruction(self)
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


    class InstructionReturnContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def address(self):
            return self.getTypedRuleContext(TACParser.AddressContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstructionReturn" ):
                listener.enterInstructionReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstructionReturn" ):
                listener.exitInstructionReturn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstructionReturn" ):
                return visitor.visitInstructionReturn(self)
            else:
                return visitor.visitChildren(self)


    class InstructionParamContext(InstructionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.InstructionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def address(self):
            return self.getTypedRuleContext(TACParser.AddressContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstructionParam" ):
                listener.enterInstructionParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstructionParam" ):
                listener.exitInstructionParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstructionParam" ):
                return visitor.visitInstructionParam(self)
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
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TACParser.T__2]:
                localctx = TACParser.NoOpContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.match(TACParser.T__2)
                pass
            elif token in [TACParser.ID, TACParser.INT]:
                localctx = TACParser.AssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.lhs()
                self.state = 48
                self.match(TACParser.T__3)
                self.state = 49
                self.rhs()
                pass
            elif token in [TACParser.T__4]:
                localctx = TACParser.ConditionalJumpContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.match(TACParser.T__4)
                self.state = 52
                self.relop()
                self.state = 53
                self.jump()
                pass
            elif token in [TACParser.T__5]:
                localctx = TACParser.InstructionReturnContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 55
                self.match(TACParser.T__5)
                self.state = 56
                self.address()
                pass
            elif token in [TACParser.T__6]:
                localctx = TACParser.InstructionParamContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 57
                self.match(TACParser.T__6)
                self.state = 58
                self.address()
                pass
            elif token in [TACParser.T__8]:
                localctx = TACParser.UnconditionalJumpContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 59
                self.jump()
                pass
            elif token in [TACParser.T__7]:
                localctx = TACParser.GlobalInstructionContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 60
                self.globalDeclaration()
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


    class GlobalDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TACParser.ID, 0)

        def getRuleIndex(self):
            return TACParser.RULE_globalDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobalDeclaration" ):
                listener.enterGlobalDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobalDeclaration" ):
                listener.exitGlobalDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGlobalDeclaration" ):
                return visitor.visitGlobalDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def globalDeclaration(self):

        localctx = TACParser.GlobalDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_globalDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(TACParser.T__7)
            self.state = 64
            self.match(TACParser.ID)
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
        self.enterRule(localctx, 10, self.RULE_jump)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(TACParser.T__8)
            self.state = 67
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
        self.enterRule(localctx, 12, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
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
        self.enterRule(localctx, 14, self.RULE_lhs)
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = TACParser.LhsSimpleContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 71
                self.address()
                pass

            elif la_ == 2:
                localctx = TACParser.LhsIndexedContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 72
                self.address()
                self.state = 73
                self.match(TACParser.T__9)
                self.state = 74
                self.address()
                self.state = 75
                self.match(TACParser.T__10)
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



    class RhsCallContext(RhsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.RhsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def label(self):
            return self.getTypedRuleContext(TACParser.LabelContext,0)

        def address(self):
            return self.getTypedRuleContext(TACParser.AddressContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRhsCall" ):
                listener.enterRhsCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRhsCall" ):
                listener.exitRhsCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRhsCall" ):
                return visitor.visitRhsCall(self)
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



    def rhs(self):

        localctx = TACParser.RhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_rhs)
        try:
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = TACParser.RhsCallContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.match(TACParser.T__11)
                self.state = 80
                self.label()
                self.state = 81
                self.address()
                pass

            elif la_ == 2:
                localctx = TACParser.RhsAddressContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.address()
                pass

            elif la_ == 3:
                localctx = TACParser.RhsBinopContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 84
                self.address()
                self.state = 85
                self.binoperator()
                self.state = 86
                self.address()
                pass

            elif la_ == 4:
                localctx = TACParser.RhsUnopContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 88
                self.unoperator()
                self.state = 89
                self.address()
                pass

            elif la_ == 5:
                localctx = TACParser.RhsIndexedContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 91
                self.address()
                self.state = 92
                self.match(TACParser.T__9)
                self.state = 93
                self.address()
                self.state = 94
                self.match(TACParser.T__10)
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
        self.enterRule(localctx, 18, self.RULE_relop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.address()
            self.state = 99
            self.reloperator()
            self.state = 100
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
        self.enterRule(localctx, 20, self.RULE_binoperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TACParser.T__12) | (1 << TACParser.T__13) | (1 << TACParser.T__14))) != 0)):
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
        self.enterRule(localctx, 22, self.RULE_reloperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TACParser.T__15) | (1 << TACParser.T__16) | (1 << TACParser.T__17) | (1 << TACParser.T__18) | (1 << TACParser.T__19) | (1 << TACParser.T__20))) != 0)):
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
        self.enterRule(localctx, 24, self.RULE_unoperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            _la = self._input.LA(1)
            if not(_la==TACParser.T__6 or _la==TACParser.T__21):
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



    class AddressIdentifierContext(AddressContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.AddressContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(TACParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddressIdentifier" ):
                listener.enterAddressIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddressIdentifier" ):
                listener.exitAddressIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddressIdentifier" ):
                return visitor.visitAddressIdentifier(self)
            else:
                return visitor.visitChildren(self)


    class AddressIntegerContext(AddressContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.AddressContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(TACParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddressInteger" ):
                listener.enterAddressInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddressInteger" ):
                listener.exitAddressInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddressInteger" ):
                return visitor.visitAddressInteger(self)
            else:
                return visitor.visitChildren(self)



    def address(self):

        localctx = TACParser.AddressContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_address)
        try:
            self.state = 110
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TACParser.ID]:
                localctx = TACParser.AddressIdentifierContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.match(TACParser.ID)
                pass
            elif token in [TACParser.INT]:
                localctx = TACParser.AddressIntegerContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 109
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





