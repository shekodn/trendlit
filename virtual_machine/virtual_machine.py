import sys
from semantic_cube.semantic_cube_helper import (
    token_to_code,
    scope_to_code,
    code_to_token,
)
from runtime_memory.runtime_memory import RuntimeMemory
from stack.stack import Stack
from virtual_machine.virtual_machine_helper import VMH

vmh = VMH()

ARTITHMETIC = [
    token_to_code.get("+"),
    token_to_code.get("-"),
    token_to_code.get("*"),
    token_to_code.get("/"),
    token_to_code.get("="),
]
RELATIONAL = [
    token_to_code.get("is"),
    token_to_code.get("not"),
    token_to_code.get(">="),
    token_to_code.get("<="),
    token_to_code.get(">"),
    token_to_code.get("<"),
]
LOGICAL = [
    token_to_code.get("and"),
    token_to_code.get("or"),
]
JUMPS = [
    token_to_code.get("GOTO"),
    token_to_code.get("GOTOF"),
    token_to_code.get("GOTOT"),
]

MODULES = [
    token_to_code.get("ERA"),
    token_to_code.get("PARAMETER"),
    token_to_code.get("GOSUB"),
    token_to_code.get("RET"),
    token_to_code.get("ENDPROC"),
]

html_file = None
instruction_pointer = 0

mem_const_start = 13000
mem_const_end = 16999

queue_quad = []

const_memory = {}
g_memory = RuntimeMemory(scope_to_code.get("global"))
memory_context_stack = Stack()
memory_context_stack.push(g_memory)
call_context_stack = Stack()


# MEMORY HELPERS
def get_value_from_address(addr):

    if addr >= g_memory.mem_global_int_start and addr <= g_memory.mem_global_str_end: # global
        return g_memory.get_value(addr)
    elif addr >= 1000000: # ptr
        return get_value_from_address(get_value_from_address(addr - 1000000)) # TODO: change this to return ptr memory from context? (- 1000000 or - 2000000 for local scopes)
    elif addr >= mem_const_start and addr <= mem_const_end: # constant
        return const_memory[addr]
    else: # local or temp
        return memory_context_stack.top().get_value(addr)


def set_value_to_address(value, addr):
    if addr >= g_memory.mem_global_int_start and addr <= g_memory.mem_global_str_end:
        # Set GLOBAL variable address
        g_memory.set_value(value, addr)
    elif addr >= 1000000: # ptr
        # Set PTR variable address
        ptr_value_addr = get_value_from_address(addr - 1000000) # TODO: change this to return ptr memory from context? (- 1000000 or - 2000000 for local scopes)
        memory_context_stack.top().set_value(value, ptr_value_addr)  # TODO: how to know if temp from local vs global
    else: #local or temp
        # Set LOCAL or TEMP variable address (from current context)
        memory_context_stack.top().set_value(value, addr)


def run_code(quads, const_mem):
    # Set the constant memory (retrieved during compilation)
    global const_memory, html_file, instruction_pointer, queue_quad
    const_memory = const_mem
    queue_quad = quads

    # html_file = open(
    #     "trendlit.tl", "w"
    # )  # TODO: change the file name to the program name the user wrote

    instruction_pointer = 0

    while instruction_pointer < len(queue_quad):
        # print("ip: ", instruction_pointer)
        exec_quad(queue_quad[instruction_pointer])
        instruction_pointer = instruction_pointer + 1
    # html_file.close()


def exec_quad(quad):
    if quad.token in ARTITHMETIC:
        arithmetic(quad)
    elif quad.token in RELATIONAL:
        relational(quad)
    elif quad.token in LOGICAL:
        logical(quad)
    elif quad.token == token_to_code.get("eval"):
        eval(quad)
    elif quad.token in JUMPS:
        jumps(quad)
    elif quad.token == token_to_code.get("VER"):
        is_arr_out_of_bounds(quad)
    elif quad.token in MODULES:
        modules(quad)
    else:
        return


def arithmetic(quad):
    if quad.token == token_to_code.get("+"):  # Addition
        # +, left_op, right_op, result
        # Get value from memory
        left_op = get_value_from_address(quad.operand1)
        right_op = get_value_from_address(quad.operand2)
        # Execute addition
        res_val = left_op + right_op
        # print(f"Added: {left_op} + {right_op}")
        # Save result in memory
        set_value_to_address(res_val, quad.operand3)
    elif quad.token == token_to_code.get("-"):  # Substraction
        # -, left_op, right_op, result
        # Get value from memory
        left_op = get_value_from_address(quad.operand1)
        right_op = get_value_from_address(quad.operand2)
        # Execute substraction
        res_val = left_op - right_op
        # Save result in memory
        set_value_to_address(res_val, quad.operand3)
    elif quad.token == token_to_code.get("*"):  # Multiplication
        # *, left_op, right_op, result
        # Get value from memory
        left_op = get_value_from_address(quad.operand1)
        right_op = get_value_from_address(quad.operand2)
        # Execute multiplication
        res_val = left_op * right_op
        # Save result in memory
        set_value_to_address(res_val, quad.operand3)
    elif quad.token == token_to_code.get("/"):  # Division
        # /, left_op, right_op, result
        # Get value from memory
        left_op = get_value_from_address(quad.operand1)
        right_op = get_value_from_address(quad.operand2)
        # Execute multiplication
        if right_op != 0:
            res_val = left_op / right_op
        else:
            print(
                "YOU ARE DIVIDING BY 0"
            )  # TODO : add nice error message (zero_division: 401)
            exit(1)
        # Save result in memory
        set_value_to_address(res_val, quad.operand3)
    else:  # Assignment '='
        # =, value, -1, variable
        # Get value from memory
        value = get_value_from_address(quad.operand1)
        # Assign by storing value in memory
        set_value_to_address(value, quad.operand3)
        # print(f"VALUE!: {value}, VARIABLE: {quad.operand3}")
        # For debbuging
        # print("-------")
        # print("int", g_memory.int_memory)
        # print("double", g_memory.double_memory)
        # print("bool", g_memory.bool_memory)
        # print("str", g_memory.str_memory)
        # print("temp", g_memory.temp_memory)
        # print("const", const_memory)


def relational(quad):
    if quad.token == token_to_code.get("is"):
        # Get value from memory
        left_op = get_value_from_address(quad.operand1)
        right_op = get_value_from_address(quad.operand2)
        # Execute substraction
        res_val = left_op == right_op
        # Save result in memory
        set_value_to_address(res_val, quad.operand3)
    elif quad.token == token_to_code.get("not"):
        # Get value from memory
        left_op = get_value_from_address(quad.operand1)
        right_op = get_value_from_address(quad.operand2)
        # Execute substraction
        res_val = left_op != right_op
        # Save result in memory
        set_value_to_address(res_val, quad.operand3)
    elif quad.token == token_to_code.get(">="):
        # Get value from memory
        left_op = get_value_from_address(quad.operand1)
        right_op = get_value_from_address(quad.operand2)
        # Execute substraction
        res_val = left_op >= right_op
        # Save result in memory
        set_value_to_address(res_val, quad.operand3)
    elif quad.token == token_to_code.get("<="):
        # Get value from memory
        left_op = get_value_from_address(quad.operand1)
        right_op = get_value_from_address(quad.operand2)
        # Execute substraction
        res_val = left_op <= right_op
        # Save result in memory
        set_value_to_address(res_val, quad.operand3)
    elif quad.token == token_to_code.get(">"):
        # Get value from memory
        left_op = get_value_from_address(quad.operand1)
        right_op = get_value_from_address(quad.operand2)
        # Execute substraction
        res_val = left_op > right_op
        # Save result in memory
        set_value_to_address(res_val, quad.operand3)
    elif quad.token == token_to_code.get("<"):# '<'
        # <, left_op, right_op, result
        # Get value from memory
        left_op = get_value_from_address(quad.operand1)
        right_op = get_value_from_address(quad.operand2)
        # For debbuging
        # print(f"left_op {left_op} right_op {right_op}")
        # Execute substraction
        res_val = left_op < right_op
        # Save result in memory
        set_value_to_address(res_val, quad.operand3)

def logical(quad):
    if quad.token == token_to_code.get("and"):
        # Get value from memory
        left_op = get_value_from_address(quad.operand1)
        right_op = get_value_from_address(quad.operand2)
        # Execute substraction
        res_val = left_op and right_op
        # Save result in memory
        set_value_to_address(res_val, quad.operand3)
    elif quad.token == token_to_code.get("or"):
        # Get value from memory
        left_op = get_value_from_address(quad.operand1)
        right_op = get_value_from_address(quad.operand2)
        # Execute substraction
        res_val = left_op or right_op
        # Save result in memory
        set_value_to_address(res_val, quad.operand3)
    else:
        print("Invalid logical operator.")
        sys.exit(1)

def eval(quad):
    # eval, -1, -1, 16000
    if quad.operand3 >= 600 and quad.operand3 <= 699:  # html tag
        value = "<" + code_to_token.get(quad.operand3).lower() + ">"
    else:
        value = get_value_from_address(quad.operand3)
        # print(f"VLUE TO PRINT: {value}, ADDRE: {quad.operand3}")
    vmh.queue_results.append(str(value))


def jumps(quad):
    global instruction_pointer
    if quad.token == token_to_code.get("GOTO"):
        # GOTO, -1, -1, destination
        # Change inst pointer to point to destination quad
        instruction_pointer = quad.operand3 - 1
    elif quad.token == token_to_code.get("GOTOF"):
        # GOTOF, trigger, -1, destination
        # Get trigger (result of condition)
        trigger = get_value_from_address(quad.operand1)
        # print("TRIGGER ", trigger)
        # Change inst = destination quad IF trigger is FALSE
        if not trigger:
            instruction_pointer = quad.operand3 - 1
    elif quad.token == token_to_code.get("GOTOT"):
        # GOTOT, trigger, -1, destination
        # Get trigger (result of condition)
        trigger = get_value_from_address(quad.operand1)
        # print("TRIGGER ", trigger)
        # Change inst = destination quad IF trigger is FALSE
        if trigger:
            instruction_pointer = quad.operand3 - 1

def is_arr_out_of_bounds(quad):
    lower_limit = get_value_from_address(quad.operand1) # Should always be 0
    upper_limit = get_value_from_address(quad.operand2)
    s = get_value_from_address(quad.operand3)
    # For debbuging
    # print(f"is_arr_out_of_bounds: lower: {lower_limit}, upper: {upper_limit}, S: {s}")

    if (s >= lower_limit and s < upper_limit):
        return True
    print(f"Slice error: Value should be between {lower_limit} {upper_limit - 1}")
    sys.exit(1)
    return False

def modules(quad):
    global instruction_pointer
    if quad.token == token_to_code.get("ERA"): # Activation Record
        # Start a Local Memory Context
        curr_l_memory = RuntimeMemory(scope_to_code.get("local"))
        # Push to Call Stack
        call_context_stack.push(curr_l_memory)
    elif quad.token == token_to_code.get("GOSUB"): #Go to subroutine
        # Remove from call stack and push to memory_context_stack
        curr_l_memory = call_context_stack.pop()
        memory_context_stack.push(curr_l_memory)
        # GOSUB, next_quad, -1, destination
        memory_context_stack.top().return_quad = quad.operand1
        # print("return to: ", memory_context_stack.top().return_quad)
        instruction_pointer = quad.operand3-1
    elif quad.token == token_to_code.get("ENDPROC"): #Void module ends
        # The function ends, IP must return to where call was made
        # ENDPROC will only appear in void functions

        # Get the return quad number from the curr context
        instruction_pointer = memory_context_stack.top().return_quad-1
        # Pop the module context from the stack
        memory_context_stack.pop()

    elif quad.token == token_to_code.get("RET"): # Return module ends
        # RET, return_val , -1, -1
        # The function ends, IP must return to where call was made
        # RET will appear only un returning functions

        # Get the return value addr
        return_value = get_value_from_address(quad.operand1)
        # Get the return quad number from the curr context
        instruction_pointer = memory_context_stack.top().return_quad
        # Pop the module context from the stack
        memory_context_stack.pop()
        # Relocate IP and get call assignation quad from the quads
        # instruction_pointer = memory_context_stack.top().return_quad
        quad = queue_quad[instruction_pointer]
        # Assign the resut to the func_var_addr
        # =, func_var_addr, -1, temp
        set_value_to_address(return_value, quad.operand1)
        arithmetic(quad) # Vm will move unto whatever quad comes after the assignment of func call var to a temp
