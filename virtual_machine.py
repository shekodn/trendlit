from semantic_cube.semantic_cube_helper import token_to_code
from runtime_memory.runtime_memory import RuntimeMemory
from stack.stack import Stack


ARTITHMETIC = [
    token_to_code.get("+"),
    token_to_code.get("-"),
    token_to_code.get("*"),
    token_to_code.get("/"),
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
global_memory = {}
# curr_memory = {}

memory_context_stack = Stack()
memory_context_stack.push(999)




def run_code(queue_quad, const_mem):
    global const_memory, memory_context_stack
    const_memory = const_mem
    # TODO: Memory ?
    instruction_pointer = 0
    # print("HELLO", const_memory)
    while quad_cont < len(queue_quad):
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
        value = memory.get_value(quad.operand1)

        # Assign by storing value in memory
        memory.set_value(value, quad.operand3)


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
