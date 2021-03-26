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


    # Enter a parse tree produced by TACParser#InstructionReturn.
    def enterInstructionReturn(self, ctx:TACParser.InstructionReturnContext):
        pass

    # Exit a parse tree produced by TACParser#InstructionReturn.
    def exitInstructionReturn(self, ctx:TACParser.InstructionReturnContext):
        pass


    # Enter a parse tree produced by TACParser#InstructionParam.
    def enterInstructionParam(self, ctx:TACParser.InstructionParamContext):
        pass

    # Exit a parse tree produced by TACParser#InstructionParam.
    def exitInstructionParam(self, ctx:TACParser.InstructionParamContext):
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


    # Enter a parse tree produced by TACParser#LhsSimple.
    def enterLhsSimple(self, ctx:TACParser.LhsSimpleContext):
        pass

    # Exit a parse tree produced by TACParser#LhsSimple.
    def exitLhsSimple(self, ctx:TACParser.LhsSimpleContext):
        pass


    # Enter a parse tree produced by TACParser#LhsIndexed.
    def enterLhsIndexed(self, ctx:TACParser.LhsIndexedContext):
        pass

    # Exit a parse tree produced by TACParser#LhsIndexed.
    def exitLhsIndexed(self, ctx:TACParser.LhsIndexedContext):
        pass


    # Enter a parse tree produced by TACParser#RhsCall.
    def enterRhsCall(self, ctx:TACParser.RhsCallContext):
        pass

    # Exit a parse tree produced by TACParser#RhsCall.
    def exitRhsCall(self, ctx:TACParser.RhsCallContext):
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


    # Enter a parse tree produced by TACParser#RhsUnop.
    def enterRhsUnop(self, ctx:TACParser.RhsUnopContext):
        pass

    # Exit a parse tree produced by TACParser#RhsUnop.
    def exitRhsUnop(self, ctx:TACParser.RhsUnopContext):
        pass


    # Enter a parse tree produced by TACParser#RhsIndexed.
    def enterRhsIndexed(self, ctx:TACParser.RhsIndexedContext):
        pass

    # Exit a parse tree produced by TACParser#RhsIndexed.
    def exitRhsIndexed(self, ctx:TACParser.RhsIndexedContext):
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


    # Enter a parse tree produced by TACParser#unoperator.
    def enterUnoperator(self, ctx:TACParser.UnoperatorContext):
        pass

    # Exit a parse tree produced by TACParser#unoperator.
    def exitUnoperator(self, ctx:TACParser.UnoperatorContext):
        pass


    # Enter a parse tree produced by TACParser#AddressGlobal.
    def enterAddressGlobal(self, ctx:TACParser.AddressGlobalContext):
        pass

    # Exit a parse tree produced by TACParser#AddressGlobal.
    def exitAddressGlobal(self, ctx:TACParser.AddressGlobalContext):
        pass


    # Enter a parse tree produced by TACParser#AddressLocal.
    def enterAddressLocal(self, ctx:TACParser.AddressLocalContext):
        pass

    # Exit a parse tree produced by TACParser#AddressLocal.
    def exitAddressLocal(self, ctx:TACParser.AddressLocalContext):
        pass


    # Enter a parse tree produced by TACParser#AddressInteger.
    def enterAddressInteger(self, ctx:TACParser.AddressIntegerContext):
        pass

    # Exit a parse tree produced by TACParser#AddressInteger.
    def exitAddressInteger(self, ctx:TACParser.AddressIntegerContext):
        pass



del TACParser