# Generated from TAC.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TACParser import TACParser
else:
    from TACParser import TACParser

# This class defines a complete listener for a parse tree produced by TACParser.
class TACListener(ParseTreeListener):

    # Enter a parse tree produced by TACParser#tacFile.
    def enterTacFile(self, ctx:TACParser.TacFileContext):
        pass

    # Exit a parse tree produced by TACParser#tacFile.
    def exitTacFile(self, ctx:TACParser.TacFileContext):
        pass


    # Enter a parse tree produced by TACParser#tacLine.
    def enterTacLine(self, ctx:TACParser.TacLineContext):
        pass

    # Exit a parse tree produced by TACParser#tacLine.
    def exitTacLine(self, ctx:TACParser.TacLineContext):
        pass


    # Enter a parse tree produced by TACParser#labeledInstruction.
    def enterLabeledInstruction(self, ctx:TACParser.LabeledInstructionContext):
        pass

    # Exit a parse tree produced by TACParser#labeledInstruction.
    def exitLabeledInstruction(self, ctx:TACParser.LabeledInstructionContext):
        pass


    # Enter a parse tree produced by TACParser#NoOp.
    def enterNoOp(self, ctx:TACParser.NoOpContext):
        pass

    # Exit a parse tree produced by TACParser#NoOp.
    def exitNoOp(self, ctx:TACParser.NoOpContext):
        pass


    # Enter a parse tree produced by TACParser#Assignment.
    def enterAssignment(self, ctx:TACParser.AssignmentContext):
        pass

    # Exit a parse tree produced by TACParser#Assignment.
    def exitAssignment(self, ctx:TACParser.AssignmentContext):
        pass


    # Enter a parse tree produced by TACParser#ConditionalJump.
    def enterConditionalJump(self, ctx:TACParser.ConditionalJumpContext):
        pass

    # Exit a parse tree produced by TACParser#ConditionalJump.
    def exitConditionalJump(self, ctx:TACParser.ConditionalJumpContext):
        pass


    # Enter a parse tree produced by TACParser#UnconditionalJump.
    def enterUnconditionalJump(self, ctx:TACParser.UnconditionalJumpContext):
        pass

    # Exit a parse tree produced by TACParser#UnconditionalJump.
    def exitUnconditionalJump(self, ctx:TACParser.UnconditionalJumpContext):
        pass


    # Enter a parse tree produced by TACParser#jump.
    def enterJump(self, ctx:TACParser.JumpContext):
        pass

    # Exit a parse tree produced by TACParser#jump.
    def exitJump(self, ctx:TACParser.JumpContext):
        pass


    # Enter a parse tree produced by TACParser#label.
    def enterLabel(self, ctx:TACParser.LabelContext):
        pass

    # Exit a parse tree produced by TACParser#label.
    def exitLabel(self, ctx:TACParser.LabelContext):
        pass


    # Enter a parse tree produced by TACParser#lhs.
    def enterLhs(self, ctx:TACParser.LhsContext):
        pass

    # Exit a parse tree produced by TACParser#lhs.
    def exitLhs(self, ctx:TACParser.LhsContext):
        pass


    # Enter a parse tree produced by TACParser#RhsAddress.
    def enterRhsAddress(self, ctx:TACParser.RhsAddressContext):
        pass

    # Exit a parse tree produced by TACParser#RhsAddress.
    def exitRhsAddress(self, ctx:TACParser.RhsAddressContext):
        pass


    # Enter a parse tree produced by TACParser#RhsBinop.
    def enterRhsBinop(self, ctx:TACParser.RhsBinopContext):
        pass

    # Exit a parse tree produced by TACParser#RhsBinop.
    def exitRhsBinop(self, ctx:TACParser.RhsBinopContext):
        pass


    # Enter a parse tree produced by TACParser#relop.
    def enterRelop(self, ctx:TACParser.RelopContext):
        pass

    # Exit a parse tree produced by TACParser#relop.
    def exitRelop(self, ctx:TACParser.RelopContext):
        pass


    # Enter a parse tree produced by TACParser#binoperator.
    def enterBinoperator(self, ctx:TACParser.BinoperatorContext):
        pass

    # Exit a parse tree produced by TACParser#binoperator.
    def exitBinoperator(self, ctx:TACParser.BinoperatorContext):
        pass


    # Enter a parse tree produced by TACParser#reloperator.
    def enterReloperator(self, ctx:TACParser.ReloperatorContext):
        pass

    # Exit a parse tree produced by TACParser#reloperator.
    def exitReloperator(self, ctx:TACParser.ReloperatorContext):
        pass


    # Enter a parse tree produced by TACParser#Identifier.
    def enterIdentifier(self, ctx:TACParser.IdentifierContext):
        pass

    # Exit a parse tree produced by TACParser#Identifier.
    def exitIdentifier(self, ctx:TACParser.IdentifierContext):
        pass


    # Enter a parse tree produced by TACParser#Integer.
    def enterInteger(self, ctx:TACParser.IntegerContext):
        pass

    # Exit a parse tree produced by TACParser#Integer.
    def exitInteger(self, ctx:TACParser.IntegerContext):
        pass



del TACParser