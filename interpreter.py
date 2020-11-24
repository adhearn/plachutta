from TACListener import TACListener
from TACVisitor import TACVisitor
from TACParser import TACParser


class Label:
    def __init__(self, name, declaration_location=None):
        self.name = name
        self.declaration_location = declaration_location
        self.reference_locations = set()

    def set_declaration_location(self, location):
        self.declaration_location = location

    def add_reference(self, location):
        self.reference_locations.add(location)

    def __str__(self):
        return f"<{self.name}: {self.declaration_location} ({self.reference_locations})>"


class AnalysisPhase(TACListener):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instructions = []
        self.labels = {}
        self.variables = set()
        self.errors = []
        self.warnings = []

    def add_label_declaration(self, name, location):
        if name in self.labels:
            label = self.labels[name]
            if label.declaration_location:
                error_msg = f"Duplicate label: {name}"
                self.errors.append(error_msg)
            else:
                label.declaration_location = location
        else:
            label = Label(name, declaration_location=location)
            self.labels[name] = label

    def add_label_reference(self, name, location):
        label = None
        if name in self.labels:
            label = self.labels[name]
        else:
            label = Label(name, declaration_location=None)
            self.labels[name] = label

        label.add_reference(location)

    def generate_unused_label_warnings(self):
        for name, label in self.labels.items():
            if not label.reference_locations:
                warning_str = f"Unused label: {label.name}"
                self.warnings.append(warning_str)

    def generate_undeclared_label_errors(self):
        for name, label in self.labels.items():
            if not label.declaration_location:
                error_str = f"Label used but not defined: {label.name}"
                self.errors.append(error_str)

    def exitTacFile(self, ctx:TACParser.TacFileContext):
        self.generate_undeclared_label_errors()
        self.generate_unused_label_warnings()

    def enterLabeledInstruction(self, ctx:TACParser.LabeledInstructionContext):
        labels = ctx.ID()
        label_location = ctx.start.line
        for label in labels:
            label_name = label.getText()
            self.add_label_declaration(label_name, label_location)

        self.instructions.append(ctx.instruction())

    def enterIdentifier(self, ctx: TACParser.IdentifierContext):
        name = ctx.ID().getText()
        parent_type = ctx.parentCtx.getRuleIndex()
        if parent_type == TACParser.RULE_rhs:
            # Make sure this variable has been defined
            if name not in self.variables:
                # Only a warning, since it might be legal with jumps. However,
                # it's a bit odd, so probably worth warning about.
                warning_str = f"Variable referenced before assignment: {name}"
                self.warning.append(warning_str)
        if parent_type == TACParser.RULE_lhs:
            self.variables.add(name)
        elif parent_type == TACParser.RULE_jump:
            location = ctx.start.line
            self.add_label_reference(name, location)


class Interpreter(TACVisitor):
    def __init__(self, instructions):
        self.instructions = instructions
        self.env = {}
        self.next_instruction = 0

    def eval(self):
        while self.next_instruction < len(self.instructions):
            instr = self.instructions[self.next_instruction]
            next_instruction = self.visit(instr)
            if next_instruction:
                self.next_instruction += next_instruction
            else:
                self.next_instruction += 1

    # Visit a parse tree produced by TACParser#Assignment.
    def visitAssignment(self, ctx:TACParser.AssignmentContext):
        lhs = self.visit(ctx.lhs())
        rhs = self.visit(ctx.rhs())
        self.env[lhs] = rhs

    # Visit a parse tree produced by TACParser#ConditionalJump.
    def visitConditionalJump(self, ctx:TACParser.ConditionalJumpContext):
        relop_value = self.visit(ctx.relop())
        if relop_value:
            dest = self.visit(ctx.jump())
            return dest

    # Visit a parse tree produced by TACParser#UnconditionalJump.
    def visitUnconditionalJump(self, ctx:TACParser.UnconditionalJumpContext):
        return self.visit(ctx.jump())


    # Visit a parse tree produced by TACParser#jump.
    def visitJump(self, ctx:TACParser.JumpContext):
        return self.visit(ctx.label())


    # Visit a parse tree produced by TACParser#lhs.
    def visitLhs(self, ctx:TACParser.LhsContext):
        return ctx.getText()

    # Visit a parse tree produced by TACParser#RhsBinop.
    def visitRhsBinop(self, ctx:TACParser.RhsBinopContext):
        addr1 = self.visit(ctx.address()[0])
        addr2 = self.visit(ctx.address()[1])
        op = self.visit(ctx.binoperator())
        return op(addr1, addr2)

    # Visit a parse tree produced by TACParser#binoperator.
    def visitBinoperator(self, ctx:TACParser.BinoperatorContext):
        text = ctx.getText()
        if text == "+":
            return lambda x, y: x + y
        elif text == "-":
            return lambda x, y: x - y
        elif text == "*":
            return lambda x, y: x * y
        else:
            raise Exception(f"Unexpected binop: {text}")

    # Visit a parse tree produced by TACParser#reloperator.
    def visitReloperator(self, ctx:TACParser.ReloperatorContext):
        text = ctx.getText()
        if text == "==":
            return lambda x, y: x == y
        elif text == "!=":
            return lambda x, y: not (x == y)
        elif text == ">":
            return lambda x, y: x > y
        elif text == ">=":
            return lambda x, y: x >= y
        elif text == "<=":
            return lambda x, y: x <= y
        elif text == "m":
            return lambda x, y: x < y
        else:
            raise Exception(f"Unexpected relop: {text}")

    # Visit a parse tree produced by TACParser#Identifier.
    def visitIdentifier(self, ctx:TACParser.IdentifierContext):
        name = ctx.getText()
        try:
            val = self.env[name]
            return val
        except KeyError:
            raise Exception(f"Variable referenced before set: {name}")

    # Visit a parse tree produced by TACParser#Integer.
    def visitInteger(self, ctx:TACParser.IntegerContext):
        return int(ctx.getText())



