from semantic_cube.semantic_cube_helper import token_to_code, scope_to_code
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
    global const_memory
    const_memory = const_mem
    # TODO: Memory ?
    instruction_pointer = 0
    # print("HELLO", const_memory)
    while instruction_pointer < len(queue_quad):
        exec_quad(queue_quad[instruction_pointer])
        instruction_pointer = instruction_pointer + 1


def exec_quad(quad):
    if (quad.token in ARTITHMETIC):
        arithmetic(quad)
    # elif (quad.token in RELATIONAL):
    #     relational(quad)
    # elif (quad.token == token_to_code.get('eval')):
    #     eval(quad)
    else:
        return


def arithmetic(quad):
    if (quad.token == token_to_code.get('+')):
        # Addition
        return
    elif (quad.token == token_to_code.get('-')):
        # Substraction
        return
    elif (quad.token == token_to_code.get('*')):
        # Multiplication
        return
    elif (quad.token == token_to_code.get('/')):
        # Division
        return
    else: ## Assignment '='
        # =, value, -1, variable
        # Get value from memory
        value = get_value_from_address(quad.operand1)
        # Assign by storing value in memory
        set_value_to_address(value, quad.operand3)


# def relational(quad):
#     if (quad.token == token_to_code.get('is')):
#     elif (quad.token == token_to_code.get('not')):
#     elif (quad.token == token_to_code.get('>=')):
#     elif (quad.token == token_to_code.get('<=')):
#     elif (quad.token == token_to_code.get('>')):
#     else: # '<'
#
# def eval(quad):
#     # TODO: print html tag, print value, endl?
