from semantic_cube.semantic_cube_helper import token_to_code, scope_to_code, code_to_token
from runtime_memory.runtime_memory import RuntimeMemory
from stack.stack import Stack


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

html_file = None

const_memory = {}
g_memory = RuntimeMemory(scope_to_code.get("global"))
# memory_context_stack = Stack() # TODO: how to keep track of local contexts


# MEMORY HELPERS
def get_value_from_address(addr):
    if addr >= g_memory.mem_global_int_start and addr <= g_memory.mem_global_str_end:
        return g_memory.get_value(addr)
    elif addr >= g_memory.mem_local_int_start and addr <= g_memory.mem_local_str_end:
        return l_memory.get_value(addr) # TODO: current memory context?
    elif addr >= g_memory.mem_temp_int_start and addr <= g_memory.mem_temp_str_end:
        return g_memory.get_value(addr) #TODO: how to know if temp from local vs global
    else: # constant
        return const_memory[addr]


def set_value_to_address (value, addr):
    if addr >= g_memory.mem_global_int_start and addr <= g_memory.mem_global_str_end:
        # Set GLOBAL variable address
        g_memory.set_value(value, addr)
    elif addr >= g_memory.mem_local_int_start and addr <= g_memory.mem_local_str_end:
        # Set LOCAL variable address
        l_memory.set_value(value, addr) # TODO: current memory context?
    else: #temp
        # Set TEMP variable address
        g_memory.set_value(value, addr) #TODO: how to know if temp from local vs global




def run_code(queue_quad, const_mem):
    # Set the constant memory (retrieved during compilation)
    global const_memory, html_file
    const_memory = const_mem

    html_file = open("trendlit.html", "w") # TODO: change the file name to the program name the user wrote

    instruction_pointer = 0
    # print("HELLO", const_memory)
    while instruction_pointer < len(queue_quad):
        exec_quad(queue_quad[instruction_pointer])
        instruction_pointer = instruction_pointer + 1


def exec_quad(quad):
    if (quad.token in ARTITHMETIC):
        arithmetic(quad)
    elif (quad.token in RELATIONAL):
        relational(quad)
    elif (quad.token == token_to_code.get('eval')):
        eval(quad)
    else:
        return


def arithmetic(quad):
    if (quad.token == token_to_code.get('+')): # Addition
        # +, left_op, right_op, result
        # Get value from memory
        left_op = get_value_from_address(quad.operand1)
        right_op = get_value_from_address(quad.operand2)
        # Execute addition
        res_val = left_op + right_op
        # Save result in memory
        set_value_to_address(res_val, quad.operand3)
    elif (quad.token == token_to_code.get('-')): # Substraction
        # -, left_op, right_op, result
        # Get value from memory
        left_op = get_value_from_address(quad.operand1)
        right_op = get_value_from_address(quad.operand2)
        # Execute substraction
        res_val = left_op - right_op
        # Save result in memory
        set_value_to_address(res_val, quad.operand3)
    elif (quad.token == token_to_code.get('*')): # Multiplication
        # *, left_op, right_op, result
        # Get value from memory
        left_op = get_value_from_address(quad.operand1)
        right_op = get_value_from_address(quad.operand2)
        # Execute multiplication
        res_val = left_op * right_op
        # Save result in memory
        set_value_to_address(res_val, quad.operand3)
    elif (quad.token == token_to_code.get('/')): # Division
        # /, left_op, right_op, result
        # Get value from memory
        left_op = get_value_from_address(quad.operand1)
        right_op = get_value_from_address(quad.operand2)
        # Execute multiplication
        if right_op != 0:
            res_val = left_op / right_op
        else:
            print("YOU ARE DIVIDING BY 0") # TODO : add nice error message (zero_division: 401)
            exit(1)
        # Save result in memory
        set_value_to_address(res_val, quad.operand3)
    else: # Assignment '='
        # =, value, -1, variable
        # Get value from memory
        value = get_value_from_address(quad.operand1)
        # Assign by storing value in memory
        set_value_to_address(value, quad.operand3)
        print("-------")
        print("int", g_memory.int_memory)
        print("double", g_memory.double_memory)
        print("bool", g_memory.bool_memory)
        print("str", g_memory.str_memory)
        print("temp", g_memory.temp_memory)


def relational(quad):
    if (quad.token == token_to_code.get('is')):
        # Get value from memory
        left_op = get_value_from_address(quad.operand1)
        right_op = get_value_from_address(quad.operand2)
        # Execute substraction
        res_val = left_op == right_op
        # Save result in memory
        set_value_to_address(res_val, quad.operand3)
    elif (quad.token == token_to_code.get('not')):
        # Get value from memory
        left_op = get_value_from_address(quad.operand1)
        right_op = get_value_from_address(quad.operand2)
        # Execute substraction
        res_val = left_op != right_op
        # Save result in memory
        set_value_to_address(res_val, quad.operand3)
    elif (quad.token == token_to_code.get('>=')):
        # Get value from memory
        left_op = get_value_from_address(quad.operand1)
        right_op = get_value_from_address(quad.operand2)
        # Execute substraction
        res_val = left_op >= right_op
        # Save result in memory
        set_value_to_address(res_val, quad.operand3)
    elif (quad.token == token_to_code.get('<=')):
        # Get value from memory
        left_op = get_value_from_address(quad.operand1)
        right_op = get_value_from_address(quad.operand2)
        # Execute substraction
        res_val = left_op <= right_op
        # Save result in memory
        set_value_to_address(res_val, quad.operand3)
    elif (quad.token == token_to_code.get('>')):
        # Get value from memory
        left_op = get_value_from_address(quad.operand1)
        right_op = get_value_from_address(quad.operand2)
        # Execute substraction
        res_val = left_op > right_op
        # Save result in memory
        set_value_to_address(res_val, quad.operand3)
    else: # '<'
        # <, left_op, right_op, result
        # Get value from memory
        left_op = get_value_from_address(quad.operand1)
        right_op = get_value_from_address(quad.operand2)
        # Execute substraction
        res_val = left_op < right_op
        # Save result in memory
        set_value_to_address(res_val, quad.operand3)

def eval(quad):
    # eval, -1, -1, 16000
    if quad.operand3 >= 600 and quad.operand3 <= 699: # html tag
        value = "<" + code_to_token.get(quad.operand3).lower() + ">"
    else:
        value = get_value_from_address(quad.operand3)
    html_file.write(str(value))  # TODO: endl? spaces? make it pretty/understandable
    html_file.write("\n")
