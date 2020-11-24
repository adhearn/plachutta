# Generated from TAC.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TACParser import TACParser
else:
    from TACParser import TACParser

# This class defines a complete generic visitor for a parse tree produced by TACParser.

class TACVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TACParser#tacFile.
    def visitTacFile(self, ctx:TACParser.TacFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#tacLine.
    def visitTacLine(self, ctx:TACParser.TacLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#labeledInstruction.
    def visitLabeledInstruction(self, ctx:TACParser.LabeledInstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#NoOp.
    def visitNoOp(self, ctx:TACParser.NoOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#Assignment.
    def visitAssignment(self, ctx:TACParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#ConditionalJump.
    def visitConditionalJump(self, ctx:TACParser.ConditionalJumpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#UnconditionalJump.
    def visitUnconditionalJump(self, ctx:TACParser.UnconditionalJumpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#jump.
    def visitJump(self, ctx:TACParser.JumpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#lhs.
    def visitLhs(self, ctx:TACParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#RhsAddres.
    def visitRhsAddres(self, ctx:TACParser.RhsAddresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#RhsBinop.
    def visitRhsBinop(self, ctx:TACParser.RhsBinopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#binoperator.
    def visitBinoperator(self, ctx:TACParser.BinoperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#reloperator.
    def visitReloperator(self, ctx:TACParser.ReloperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#Identifier.
    def visitIdentifier(self, ctx:TACParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#Integer.
    def visitInteger(self, ctx:TACParser.IntegerContext):
        return self.visitChildren(ctx)



del TACParser