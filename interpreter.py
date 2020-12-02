from TACListener import TACListener
from TACVisitor import TACVisitor
from TACParser import TACParser


class NoSuchVariableException(BaseException):
    pass


class Symbol:
    TYPE = "SYMBOL"

    def __init__(self, *, name):
        self.name = name
        self.reference_locations = set()
        self.symbol_type = self.TYPE
        self.is_global = False


    def add_reference(self, location):
        self.reference_locations.add(location)

    def __str__(self):
        return f"<{self.name} ({self.symbol_type}): {self.declaration_location} ({self.reference_locations})>"


class Label(Symbol):
    TYPE = "LABEL"

    def __init__(self, *args, declaration_location=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.declaration_location = declaration_location
        self.is_global = True


class Variable(Symbol):
    TYPE = "VARIABLE"

    def __init__(self, *args, is_global=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.memory_location = None
        self.is_global = is_global


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

    def globals(self):
        return [v for k, v in self.symbols.items() if v.TYPE == Variable.TYPE and v.is_global]


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


class StackFrame:
    def __init__(self, return_address, parameters):
        self.return_address = return_address
        self.parameters = parameters
        self.memory = Memory()
        self._variable_locations = {}

    def get_local_variable(self, variable_name):
        loc = self._variable_locations.get(variable_name)

        if loc is None:
            print(self._variable_locations)
            raise NoSuchVariableException(f"No local variable found: {variable_name}")

        return self.memory.ref(loc)

    def set_local_variable(self, variable_name, value):
        print(f"Setting local variable {variable_name} = {value}")
        loc = self._variable_locations.get(variable_name)

        if loc is None:
            loc = self.memory.request(1)
            self._variable_locations[variable_name] = loc

        return self.memory.set(loc, value)


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

    def variable_reference(self, name, location, global_declaration=False):
        variable = self.symbol_table.get(name)
        if not variable:
            variable = Variable(name=name)
            variable.add_reference(location)
            self.symbol_table.add(variable)

        if global_declaration:
            variable.is_global = True

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

    def enterGlobalDeclaration(self, ctx: TACParser.GlobalInstructionContext):
        name = ctx.ID().getText()
        location = ctx.start.line - 1
        self.variable_reference(name, location, global_declaration=True)

    def enterAddressIdentifier(self, ctx: TACParser.AddressIdentifierContext):
        name = ctx.ID().getText()
        location = ctx.start.line - 1
        self.variable_reference(name, location)


class Interpreter(TACVisitor):
    MAIN_EXIT_ADDRESS = "MAIN_EXIT"

    def __init__(self, instructions, symbol_table):
        self.instructions = instructions
        self.instruction_pointer = None
        self.symbol_table = symbol_table
        self.memory = Memory()
        self.parameters = []
        self.stack = []
        self.return_value_set = False
        self.return_value = None
        self.initialize_memory()
        self.initialize_stack()

    def initialize_stack(self):
        main_label = self.symbol_table.get("main")
        assert main_label.symbol_type == Label.TYPE
        self.instruction_pointer = main_label.declaration_location
        initial_frame = StackFrame(self.MAIN_EXIT_ADDRESS, [])
        self.stack.append(initial_frame)

    @property
    def current_frame(self):
        return self.stack[len(self.stack) - 1]

    def initialize_memory(self):
        for variable in self.symbol_table.globals():
            variable.memory_location = self.memory.request(1)

    def pop_parameters(self, n):
        params = self.parameters[-n:]
        self.parameters = self.parameters[:-n]
        return params

    def eval(self):
        while self.instruction_pointer < len(self.instructions):
            instr = self.instructions[self.instruction_pointer]
            instruction_pointer = self.visit(instr)
            if instruction_pointer:
                if instruction_pointer == self.MAIN_EXIT_ADDRESS:
                    return self.return_value
                else:
                    self.instruction_pointer = instruction_pointer
            else:
                self.instruction_pointer += 1

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

    # Visit a parse tree produced by TACParser#InstructionReturn.
    def visitInstructionReturn(self, ctx: TACParser.InstructionReturnContext):
        return_value = self.visit(ctx.address())
        return_address = self.current_frame.return_address  # currently unused
        self.stack.pop()
        self.return_value = return_value
        self.return_value_set = True
        return return_address

    # Visit a parse tree produced by TACParser#InstructionParam.
    def visitInstructionParam(self, ctx: TACParser.InstructionParamContext):
        address_value = self.visit(ctx.address())
        self.parameters.append(address_value)

    # Visit a parse tree produced by TACParser#InstructionCall.
    def visitRhsCall(self, ctx: TACParser.RhsCallContext):
        if self.return_value_set:
            return_value = self.return_value
            self.return_value_set = False
            self.return_value = None
            return return_value
        else:
            param_count = self.visit(ctx.address())
            params = self.pop_parameters(param_count)
            stack_frame = StackFrame(self.instruction_pointer, params)
            self.stack.append(stack_frame)
            # TODO: This is a terrible hack
            label_location = self.visit(ctx.label()) - 1
            self.instruction_pointer = label_location

    # Visit a parse tree produced by TACParser#LhsSimple.
    def visitLhsSimple(self, ctx: TACParser.LhsSimpleContext):
        lhs_name = ctx.getText()
        symbol = self.symbol_table.get(lhs_name)
        if symbol.is_global:
            memloc = symbol.memory_location
            def variable(rhs):
                self.memory.set(memloc, rhs)
        else:
            def variable(rhs):
                self.current_frame.set_local_variable(lhs_name, rhs)

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
        op = ctx.unoperator().getText()
        if op == "memrequest":
            return self.memory.request(addr_value)
        elif op == "param":
            return self.current_frame.parameters[addr_value]
        else:
            raise Exception(f"vistRhsUnop: Unexpected operator: {op}")

    # Visit a parse tree produced by TACParser#RhsIndexed.
    def visitRhsIndexed(self, ctx:TACParser.RhsIndexedContext):
        base_index = self.visit(ctx.address(0))
        offset_value = self.visit(ctx.address(1))
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
    def visitAddressIdentifier(self, ctx:TACParser.AddressIdentifierContext):
        name = ctx.getText()
        symbol = self.symbol_table.get(name)
        if symbol.is_global:
            memloc = symbol.memory_location
            return self.memory.ref(memloc)
        else:
            return self.current_frame.get_local_variable(name)

    # Visit a parse tree produced by TACParser#Integer.
    def visitAddressInteger(self, ctx:TACParser.AddressIntegerContext):
        return int(ctx.getText())
