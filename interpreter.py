from TACListener import TACListener
from TACVisitor import TACVisitor
from TACParser import TACParser


class Symbol:
    TYPE = "SYMBOL"

    def __init__(self, *, name):
        self.name = name
        self.reference_locations = set()
        self.symbol_type = self.TYPE

    def add_reference(self, location):
        self.reference_locations.add(location)

    def __str__(self):
        return f"<{self.name} ({self.symbol_type}): {self.declaration_location} ({self.reference_locations})>"


class Label(Symbol):
    TYPE = "LABEL"

    def __init__(self, *args, declaration_location=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.declaration_location = declaration_location


class Variable(Symbol):
    TYPE = "VARIABLE"

    def __init__(self, *args, memory_location=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.memory_location = memory_location


class SymbolTable:

    def __init__(self):
        self.symbols = {}

    def add(self, symbol):
        self.symbols[symbol.name] = symbol

    def get(self, name):
        return self.symbols.get(name)

    def labels(self):
        return [v for k, v in self.symbols.items() if v.TYPE == Label.TYPE]

    def variables(self):
        return [v for k, v in self.symbols.items() if v.TYPE == Variable.TYPE]


class Memory:
    def __init__(self):
        self._mem = []

    def ref(self, address, offset=0):
        return self._mem[address + offset]

    def set(self, address, value, offset=0):
        self._mem[address + offset] = value

    def request(self, size, initial=None):
        index = len(self._mem)
        new_mem = [initial for _ in range(size)]
        self._mem.extend(new_mem)
        return index


class AnalysisPhase(TACListener):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instructions = []
        self.memory = Memory()
        self.symbol_table = SymbolTable()
        self.errors = []
        self.warnings = []

    def add_label_declaration(self, name, location):
        symbol = self.symbol_table.get(name)
        if symbol:
            if symbol.declaration_location:
                error_msg = f"Duplicate label: {name}"
                self.errors.append(error_msg)
            else:
                symbol.declaration_location = location
        else:
            label = Label(name=name, declaration_location=location)
            self.symbol_table.add(label)

    def add_label_reference(self, name, location):
        label = self.symbol_table.get(name)
        if not label:
            label = Label(name=name, declaration_location=None)
            self.symbol_table.add(label)

        label.add_reference(location)

    def variable_reference(self, name, location):
        variable = self.symbol_table.get(name)
        if not variable:
            variable = Variable(name=name)
            variable.add_reference(location)
            self.symbol_table.add(variable)

    def generate_unused_label_warnings(self):
        for label in self.symbol_table.labels():
            if not label.reference_locations:
                warning_str = f"Unused label: {label.name}"
                self.warnings.append(warning_str)

    def generate_undeclared_label_errors(self):
        for label in self.symbol_table.labels():
            if label.declaration_location is None:
                error_str = f"Label used but not defined: {label.name}"
                self.errors.append(error_str)

    def exitTacFile(self, ctx:TACParser.TacFileContext):
        self.generate_undeclared_label_errors()
        self.generate_unused_label_warnings()

    def enterLabeledInstruction(self, ctx:TACParser.LabeledInstructionContext):
        self.instructions.append(ctx.instruction())

    def enterLabel(self, ctx):
        name = ctx.ID().getText()
        parent_type = ctx.parentCtx.getRuleIndex()
        location = ctx.start.line - 1
        if parent_type == TACParser.RULE_jump:
            self.add_label_reference(name, location)
        elif parent_type == TACParser.RULE_labeledInstruction:
            self.add_label_declaration(name, location)

    def enterIdentifier(self, ctx: TACParser.IdentifierContext):
        name = ctx.ID().getText()
        location = ctx.start.line - 1
        self.variable_reference(name, location)


class Interpreter(TACVisitor):
    def __init__(self, instructions, symbol_table):
        self.instructions = instructions
        self.symbol_table = symbol_table
        self.memory = Memory()
        self.next_instruction = 0
        self.initialize_memory()

    def initialize_memory(self):
        for variable in self.symbol_table.variables():
            variable.memory_location = self.memory.request(1)

    def eval(self):
        while self.next_instruction < len(self.instructions):
            instr = self.instructions[self.next_instruction]
            next_instruction = self.visit(instr)
            if next_instruction:
                self.next_instruction = next_instruction
            else:
                self.next_instruction += 1

    # Visit a parse tree produced by TACParser#Assignment.
    def visitAssignment(self, ctx:TACParser.AssignmentContext):
        lhs = self.visit(ctx.lhs())
        rhs = self.visit(ctx.rhs())
        lhs(rhs)

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

    # Visit a parse tree produced by TACParser#LhsSimple.
    def visitLhsSimple(self, ctx: TACParser.LhsSimpleContext):
        lhs_name = ctx.getText()
        symbol = self.symbol_table.get(lhs_name)
        memloc = symbol.memory_location
        def variable(rhs):
            self.memory.set(memloc, rhs)

        return variable

    def visitLhsIndexed(self, ctx: TACParser.LhsIndexedContext):
        base = self.visit(ctx.address(0))
        offset = self.visit(ctx.address(1))

        def update(value):
            self.memory.set(base, value, offset=offset)

        return update

    # Visit a parse tree produced by TACParser#RhsBinop.
    def visitRhsBinop(self, ctx:TACParser.RhsBinopContext):
        addr1 = self.visit(ctx.address()[0])
        addr2 = self.visit(ctx.address()[1])
        op = self.visit(ctx.binoperator())
        return op(addr1, addr2)

    # Visit a parse tree produced by TACParser#RhsUnop.
    def visitRhsUnop(self, ctx:TACParser.RhsUnopContext):
        addr_value = self.visit(ctx.address())
        assert type(addr_value) == int
        return self.memory.request(addr_value)

    # Visit a parse tree produced by TACParser#RhsIndexed.
    def visitRhsIndexed(self, ctx:TACParser.RhsIndexedContext):
        base_index = self.visit(ctx.address(0))
        offset_value = self.visit(ctx.address(1))
        print(f"offset: {offset_value}")
        print(f"base_index: {base_index}")
        print(f"mem: {self.memory._mem}")
        return self.memory.ref(base_index, offset_value)

    # # Visit a parse tree produced by TACParser#RhsAddressOf.
    # def visitRhsAddressOf(self, ctx:TACParser.RhsAddressOfContext):
    #     identifier_name = self.visit(ctx.ID().getText())
    #     symbol = self.symbol_table.get(identifier_name)
    #     return symbol.memory_location

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

    def visitRelop(self, ctx:TACParser.RelopContext):
        op = self.visit(ctx.reloperator())
        addr1 = self.visit(ctx.address()[0])
        addr2 = self.visit(ctx.address()[1])
        return op(addr1, addr2)

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

    def visitLabel(self, ctx:TACParser.LabelContext):
        name = ctx.getText()
        label_loc = self.symbol_table.get(name).declaration_location
        return label_loc

    # Visit a parse tree produced by TACParser#Identifier.
    def visitIdentifier(self, ctx:TACParser.IdentifierContext):
        name = ctx.getText()
        symbol = self.symbol_table.get(name)
        memloc = symbol.memory_location
        return self.memory.ref(memloc)

    # Visit a parse tree produced by TACParser#Integer.
    def visitInteger(self, ctx:TACParser.IntegerContext):
        return int(ctx.getText())
