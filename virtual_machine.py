from semantic_cube.semantic_cube_helper import token_to_code

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


def run_code(queue_quad):
    # TODO: Memory ?
    instruction_pointer = 0
    while quad_cont < len(queue_quad):
        exec_quad(queue_quad[instruction_pointer])
        instruction_pointer = instruction_pointer + 1


def exec_quad(quad):
    if (quad.token in ARTITHMETIC):
        arithmetic(quad)
    elif (quad.token in RELATIONAL):
        relational(quad)
    elif (quad.token == token_to_code.get('eval')):
        eval(quad)


def arithmetic(quad):
    if (quad.token == token_to_code.get('+')):
        # Addition
    elif (quad.token == token_to_code.get('-')):
        # Substraction
    elif (quad.token == token_to_code.get('*')):
        # Multiplication
    elif (quad.token == token_to_code.get('/')):
        # Division
    else: ## Assignment '='

def relational(quad):
    if (quad.token == token_to_code.get('is')):
    elif (quad.token == token_to_code.get('not')):
    elif (quad.token == token_to_code.get('>=')):
    elif (quad.token == token_to_code.get('<=')):
    elif (quad.token == token_to_code.get('>')):
    else: # '<'

def eval(quad):
    # TODO: print html tag, print value, endl?
