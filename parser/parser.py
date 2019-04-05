#!/usr/bin/python3

from lexer.lexer import lexer, tokens
from quadruple.quadruple_helper import *
from quadruple.quadruple import *
from semantic_cube.semantic_cube import Cube
from semantic_cube.semantic_cube_helper import (
    code_to_type,
    token_to_code,
    type_to_init_value,
)
from error.error_helper import ErrorHelper

procedure_directory = {}  # [name] = {type, var_table}

curr_scope = ""  # The current scope inside the program
curr_type = ""  # The current type used (module or var)

quad_helper = QuadrupleHelper()
error_helper = ErrorHelper()
semantic_cube = Cube()


def p_program(p):
    """program : PROGRAM ID program1"""


def p_program1(p):
    """program1 : script program2
        | program2"""


def p_program2(p):
    """program2 : htmltag program2
        | empty"""


def p_script(p):
    """script : SCRIPT snp_script_start block"""


def p_block(p):
    """block : OBRACE declareBlock block1 CBRACE"""


def p_block1(p):
    """block1 : statement block1
        | module block1
        | empty"""


def p_simpleBlock(p):
    """simpleBlock : OBRACE simpleBlock1 CBRACE"""


def p_simpleBlock1(p):
    """simpleBlock1 : statement simpleBlock1
        | empty"""


def p_voidModuleBlock(p):
    """voidModuleBlock : snp_save_void_type OBRACE declareBlock voidModuleBlock1 CBRACE"""


def p_voidModuleBlock1(p):
    """voidModuleBlock1 : statement voidModuleBlock1
        | empty"""


def p_returnModuleBlock(p):
    """returnModuleBlock : COLON type OBRACE declareBlock returnModuleBlock1 CBRACE"""


def p_returnModuleBlock1(p):
    """returnModuleBlock1 : statement returnModuleBlock1
        | SPIT expression"""


def p_declareBlock(p):
    """declareBlock : declare declareBlock
        | empty"""


def p_declare(p):
    """declare : type ID snp_add_var snp_push_solitary_operand
        | type ID snp_add_var initializeSlices
        | initialize"""


def p_initialize(p):
    """initialize : type initialize1 snp_add_assignation_quad initialize2"""


def p_initialize1(p):
    """initialize1 : ID snp_add_var snp_push_pending_operand EQ snp_push_pending_token value
        | ID snp_add_var initializeSlices EQ constSlices"""


def p_initialize2(p):
    """initialize2 : COMMA initialize1 initialize2
        | empty"""


def p_initializeSlices(p):
    """initializeSlices : initializeSlices1D
        | initializeSlices2D"""


def p_initializeSlices1D(p):
    """initializeSlices1D : OBRACK CTEI CBRACK"""


def p_initializeSlices2D(p):
    """initializeSlices2D : OBRACK CTEI CBRACK OBRACK CTEI CBRACK"""


def p_constSlices(p):
    """constSlices : constSlice1D
        | constSlice2D"""


def p_constSlice1D(p):
    """constSlice1D : OBRACK value constSlice1D1 CBRACK"""


def p_constSlice1D1(p):
    """constSlice1D1 : COMMA value constSlice1D1
        | empty"""


# TODO: FIX 2D SLICE
def p_constSlice2D(p):
    """constSlice2D : OBRACK constSlice1D COMMA CBRACK
        | OBRACK constSlice1D CBRACK"""


def p_type(p):
    """type : STR snp_save_type
        | INT snp_save_type
        | DOUBLE snp_save_type
        | BOOL snp_save_type"""


def p_statement(p):
    """statement : assignment
        | condition
        | cycle
        | call
        | writing"""


def p_assignment(p):
    """assignment : ID snp_push_pending_operand assignmentSlice EQ snp_push_pending_token expression snp_add_assignation_quad"""


def p_assignmentSlice(p):
    """assignmentSlice : assignmentSlice1D
        | assignmentSlice2D
        | empty"""


def p_assignmentSlice1D(p):
    """assignmentSlice1D : OBRACK expression CBRACK"""


def p_assignmentSlice2D(p):
    """assignmentSlice2D : OBRACK expression CBRACK OBRACK expression CBRACK"""


def p_expression(p):
    """expression : exp expression1 snp_check_precedence_and_create_quadruple_for_rel"""


# ASSOCIATIVE => "or|and"
def p_expression1(p):
    """expression1 : REL snp_push_pending_token exp
        | ASSOCIATIVE snp_push_pending_token exp
        | empty"""
    # TODO add single expression. Do we allow if(True) ???


# Reference: Mathematical Expressions
# snp_check_precedence_and_create_quadruple => STEP 4
def p_exp(p):
    """exp : term snp_check_precedence_and_create_quadruple_for_sign exp1"""


# Reference: Mathematical Expressions
# snp_push_pending_token => STEP 2
def p_exp1(p):
    """exp1 : SIGN snp_push_pending_token exp exp1
        | empty"""


def p_term(p):
    """term : factor snp_check_precedence_and_create_quadruple_for_op term1"""


# Reference: Mathematical Expressions
# snp_push_pending_token => STEP 3
def p_term1(p):
    """term1 : OP snp_push_pending_token term term1
        | empty"""


def p_factor(p):
    """factor : OPAREN snp_push_pending_token expression CPAREN snp_clean_stack_until_false_bottom
        | factor1"""


def p_factor1(p):
    """factor1 : value
        | SIGN value"""


def p_value(p):
    """value : ID snp_push_pending_operand
        | valueSlice
        | call
        | CTEI snp_save_type_int snp_push_pending_operand
        | CTED snp_save_type_double snp_push_pending_operand
        | CTESTR snp_save_type_str snp_push_pending_operand
        | FALSE snp_save_type_bool snp_push_pending_operand
        | TRUE snp_save_type_bool snp_push_pending_operand"""


def p_valueSlice(p):
    """valueSlice : valueSlice1D
        | valueSlice2D"""


def p_valueSlice1D(p):
    """valueSlice1D : ID OBRACK expression CBRACK"""


def p_valueSlice2D(p):
    """valueSlice2D : ID OBRACK expression CBRACK OBRACK expression CBRACK"""


def p_condition(p):
    """condition : IF OPAREN expression CPAREN snp_conditional_statement_1 simpleBlock condition1 snp_conditional_statement_2"""


def p_condition1(p):
    """condition1 : ELSE snp_conditional_statement_3 simpleBlock
        | empty"""


def p_cycle(p):
    """cycle : LOOP snp_while_1 OPAREN expression CPAREN snp_conditional_statement_1 simpleBlock snp_while_3"""


def p_module(p):
    """module : DEF ID snp_add_module OPAREN arguments CPAREN module1 snp_end_module"""


def p_module1(p):
    """module1 : voidModuleBlock
        | returnModuleBlock"""


def p_call(p):
    """call : ID call1
        | predef"""


def p_call1(p):
    """call1 : OPAREN params CPAREN"""


def p_params(p):
    """params : expression params1"""


def p_params1(p):
    """params1 : COMMA params
        | empty"""


def p_predef(p):
    """predef : predef_avg
        | predef_find_max
        | predef_find_min
        | predef_median
        | predef_mode
        | predef_find_mult_slice
        | predef_pow
        | predef_randoms
        | predef_sort_slice
        | predef_suck_csv
        | predef_zeros"""


def p_predef_avg(p):
    """predef_avg : AVG OPAREN ID CPAREN"""


def p_predef_find_max(p):
    """predef_find_max : FIND_MAX OPAREN ID COMMA predef_find_max_args CPAREN"""


def p_predef_find_max_args(p):
    """predef_find_max_args : ID
        | CTEI"""


def p_predef_find_min(p):
    """predef_find_min : FIND_MIN OPAREN ID COMMA predef_find_min_args CPAREN"""


def p_predef_find_min_args(p):
    """predef_find_min_args : ID
        | CTEI"""


def p_predef_find_mult_slice(p):
    """predef_find_mult_slice : MULTIPLY_1DSLICE OPAREN ID COMMA predef_find_mult_slice_args CPAREN"""


def p_predef_find_mult_slice_args(p):
    """predef_find_mult_slice_args : ID
        | CTEI"""


def p_predef_median(p):
    """predef_median : MEDIAN OPAREN ID CPAREN"""


def p_predef_mode(p):
    """predef_mode : MODE OPAREN ID CPAREN"""


def p_predef_pow(p):
    """predef_pow : POW OPAREN predef_pow_args COMMA predef_pow_args CPAREN"""


def p_predef_pow_args(p):
    """predef_pow_args : ID
        | CTEI"""


def p_predef_randoms(p):
    """predef_randoms : RANDOMS OPAREN predef_randoms_args CPAREN"""


def p_predef_randoms_args(p):
    """predef_randoms_args : ID
        | CTEI"""


def p_predef_zeros(p):
    """predef_zeros : ZEROS OPAREN predef_zeros_args CPAREN"""


def p_predef_zeros_args(p):
    """predef_zeros_args : ID
        | CTEI"""


def p_predef_sort_slice(p):
    """predef_sort_slice : SORT_SLICE OPAREN ID COMMA predef_sort_slice_option CPAREN"""


def p_predef_sort_slice_option(p):
    """predef_sort_slice_option : MAX
        | MIN"""


def p_predef_suck_csv(p):
    """predef_suck_csv : SUCK_CSV OPAREN predef_suck_csv_args CPAREN"""


def p_predef_suck_csv_args(p):
    """predef_suck_csv_args : ID
        | CTESTR"""


def p_writing(p):
    """writing : EVAL OPAREN expression CPAREN"""


def p_arguments(p):
    """arguments : type ID arguments1
        | empty"""


def p_arguments1(p):
    """arguments1 : COMMA type ID arguments1
        | empty"""


def p_htmltag(p):
    """htmltag : tag OBRACE class htmltag1 CBRACE"""


def p_htmltag1(p):
    """htmltag1 : CTESTR htmltag1
        | htmlscript htmltag1
        | htmltag htmltag1
        | empty"""


def p_tag(p):
    """tag : H1
        | H2
        | DIV
        | P
        | TABLE
        | TR
        | TH"""


def p_class(p):
    """class : CLASS COLON CTESTR
        | empty"""


def p_htmlscript(p):
    """htmlscript : OEVALSCRIPT expression CEVALSCRIPT
        | embedscript"""


# TODO : FIX THIS!!!
def p_embedscript(p):
    """embedscript : EMBED ID block"""
    # """embedscript : EMBED ID OBRACE eblock CBRACE"""


def p_empty(p):
    """empty :"""


def p_error(p):
    print("Syntax error at '%s'" % p)
    exit(1)


# --- SEMANTIC NEURAL POINTS ---

# --- PROCEDURE/MODULE SEMANTIC ACTIONS---

# Start of script global scope (adds global scope to directory)
def p_snp_script_start(p):
    """snp_script_start : empty"""
    global procedure_directory, curr_scope, curr_type
    # Set current values for global script
    curr_scope = "global_script"
    curr_type = "void"
    # Add global script to the directory
    procedure_directory[curr_scope] = {
        "type": curr_type,
        "var_table": {},
    }  # TODO : add more info later on


# Start of the module (add module to directory)
def p_snp_add_module(p):
    """snp_add_module : empty"""
    global procedure_directory, curr_scope
    module_name = p[-1]  # get the last symbol read (left from this neural point)
    # Check if module already exists and add it to the directory
    if module_name in procedure_directory:
        error_message = f"Module {module_name} has already been declared"
        error_helper.add_error(0, error_message)
    else:
        procedure_directory[module_name] = {
            "type": curr_type,
            "var_table": {},
        }  # TODO : add more info later on
        curr_scope = module_name


# Save the last type defined
def p_snp_save_type(p):
    """snp_save_type : empty"""
    global curr_type
    curr_type = p[-1]


# Save the last type as void (for modules)
def p_snp_save_void_type(p):
    """snp_save_void_type : empty"""
    global curr_type
    curr_type = "void"


# End of the module deltes the var table
def p_snp_end_module(p):
    """snp_end_module : empty"""
    global procedure_directory, curr_scope
    # Delete var table for the module that ended
    procedure_directory[curr_scope]["var_table"].clear()
    curr_scope = "global_script"


# --- VARIABLE SEMANTIC ACTIONS ---

# Adds a variable defined to the current scope variable table
def p_snp_add_var(p):
    """snp_add_var : empty"""
    global procedure_directory
    var_name = p[-1]  # get the last symbol read (left from this neural point)
    # For debbuging
    # print(f"var_name {var_name}, current_scope, {curr_scope}")
    # print(procedure_directory[curr_scope], "\n")
    # Check if var already exists and add it to the table in currect scope
    if is_var_in_current_scope(var_name):
        error_message = f"Variable {var_name} has already been declared"
        error_helper.add_error(0, error_message)
    else:
        procedure_directory[curr_scope]["var_table"][var_name] = {
            "type": curr_type
        }  # TODO : add more info later on


# --- MATHEMATICAL EXPRESSIONS (INTERMEDIATE REPRESENTATION) ---
def p_snp_push_pending_operand(p):
    """snp_push_pending_operand : empty"""

    # TODO question for Ana Karen
    # FIXME
    # Separate this function to avoid confusion
    # print("-2 ",p[-2], "-1 ", p[-1])
    if p[-2] != None:
        operand_id = p[-2]
        operand_id_2 = p[-1]
        quad_helper.push_operand(operand_id)
        quad_helper.push_operand(operand_id_2)
        # debbuging
        # print("if operand_id: ", operand_id)
        # print("if operand_id_2: ", operand_id_2)
        # print("p-2", p[-2], "p-1", p[-1])
    else:
        operand_id = p[-1]
        quad_helper.push_operand(operand_id)
        # debbuging
        # print("else operand_id: ", operand_id)

    if is_var_in_current_scope(operand_id):
        type = procedure_directory[curr_scope]["var_table"][operand_id]["type"]
        quad_helper.push_type(type)
    else:
        quad_helper.push_type(curr_type)
    # For debbuging
    # print("OPERAND", quad_helper.top_operand())
    # print("TYPE", quad_helper.top_type())


# def p_snp_push_pending_operand_1(p):
#     """snp_push_pending_operand_1 : empty"""
#     print("snp_push_pending_operand_1")
#     # TODO question for Ana Karen
#     # FIXME
#     # Separate this function to avoid confusion
#     if p[-2] != None:
#         operand_id = p[-2]
#         # debbuging
#         print("if operand_id: ", operand_id)
#
#     else:
#         operand_id = p[-1]
#         print("else operand_id: ", operand_id)
#     quad_helper.push_operand(operand_id)
#         # debbuging
#         # print("else operand_id: ", operand_id)
#
#     if is_var_in_current_scope(operand_id):
#         type = procedure_directory[curr_scope]["var_table"][operand_id]["type"]
#         quad_helper.push_type(type)
#     else:
#         quad_helper.push_type(curr_type)
#     # For debbuging
#     # print("OPERAND", quad_helper.top_operand())
#     # print("TYPE", quad_helper.top_type())


def p_snp_save_type_int(p):
    """snp_save_type_int : empty"""
    global curr_type
    curr_type = "int"


def p_snp_save_type_double(p):
    """snp_save_type_double : empty"""
    global curr_type
    curr_type = "double"


def p_snp_save_type_str(p):
    """snp_save_type_str : empty"""
    global curr_type
    curr_type = "str"


def p_snp_save_type_bool(p):
    """snp_save_type_bool : empty"""
    global curr_type
    curr_type = "bool"


def p_snp_push_pending_token(p):
    """snp_push_pending_token : empty"""
    token = p[-1]
    # debbuging
    # print("pushed token", token)
    quad_helper.push_token(token)


def p_snp_push_solitary_operand(p):
    """snp_push_solitary_operand : empty"""

    """
    Variables declared without a corresponding initialization are zero-valued.
    For example, the zero value for an int is 0
    """
    operand_id = p[-2]
    type = procedure_directory[curr_scope]["var_table"][operand_id]["type"]
    default_initial_value = type_to_init_value.get(type)
    operator = token_to_code.get("=")

    quad_helper.add_quad(operator, default_initial_value, -1, operand_id)


def p_snp_add_assignation_quad(p):
    """snp_add_assignation_quad : empty"""
    # TODO = add logic for precedence here?
    add_quadruple_assignation()


def add_quadruple_assignation():
    right_operand = quad_helper.pop_operand()  # TODO: type int
    right_operand_type = quad_helper.pop_type()
    left_operand = quad_helper.pop_operand()  # TODO: type str
    left_operand_type = quad_helper.pop_type()
    token = quad_helper.pop_token()

    if left_operand is None:
        # print("LEFT IS NONE", left_operand)
        left_operand = quad_helper.pop_operand()
        # print("LEFT NOT NONE", left_operand)
    if right_operand is None:
        # print("RIGHT IS NONE", right_operand)
        right_operand = quad_helper.pop_operand()
        # print("RIGHT NOT NONE", right_operand)
        # print("add_quadruple_assignation pop:  ", left_operand_type)

    if semantic_cube.is_in_cube(right_operand_type, left_operand_type, token):  # baila?
        quad_helper.add_quad(token, right_operand, -1, left_operand)  # assignation
    else:
        error_helper.add_error(301)


# sign => "+|-"
def p_snp_check_precedence_and_create_quadruple_for_sign(p):
    """snp_check_precedence_and_create_quadruple_for_sign : empty"""
    top = quad_helper.top_token()
    add = token_to_code.get("+")
    sub = token_to_code.get("-")
    is_sign = (top is add) or (top is sub)
    if is_sign:
        add_quadruple_expression()


# op => "*|/"
def p_snp_check_precedence_and_create_quadruple_for_op(p):
    """snp_check_precedence_and_create_quadruple_for_op : empty"""

    top = quad_helper.top_token()
    division = token_to_code.get("/")
    product = token_to_code.get("*")
    is_op = (top is division) or (top is product)

    if is_op:
        add_quadruple_expression()


# rel => "is|not|>=|<=|>|<"
def p_snp_check_precedence_and_create_quadruple_for_rel(p):
    """snp_check_precedence_and_create_quadruple_for_rel : empty"""

    top = quad_helper.top_token()
    eq = token_to_code.get("is")
    noteq = token_to_code.get("not")
    get = token_to_code.get(">=")
    let = token_to_code.get("<=")
    gt = token_to_code.get(">")
    lt = token_to_code.get("<")

    is_rel = (
        (top is eq)
        or (top is noteq)
        or (top is get)
        or (top is let)
        or (top is gt)
        or (top is lt)
    )

    if is_rel:
        add_quadruple_expression()


def p_snp_clean_stack_until_false_bottom(p):
    """snp_clean_stack_until_false_bottom : empty"""
    # CPAREN ", "stack should pop until finding ')' or '(' ")
    quad_helper.pop_token()


def add_quadruple_expression():
    right_operand = quad_helper.pop_operand()  # TODO: type int
    right_operand_type = quad_helper.pop_type()
    # TODO: TESTTTT
    left_operand = quad_helper.pop_operand()  # TODO: type str
    left_operand_type = quad_helper.pop_type()
    false_bottom = token_to_code.get("(")
    # debbuging
    # print("quad_helper.top_token()", quad_helper.top_token())
    if quad_helper.top_token() is false_bottom:
        print("false bottom:", quad_helper.top_token())
        quad_helper.pop_token()
        token = quad_helper.pop_token()
    else:
        token = quad_helper.pop_token()
    # token = quad_helper.pop_token()

    # debbuging HERE
    # print(right_operand, left_operand, token)
    if semantic_cube.is_in_cube(right_operand_type, left_operand_type, token):  # baila?
        quad_helper.add_quad(token, left_operand, right_operand, quad_helper.temp_cont)
        # expression
        quad_helper.push_operand(quad_helper.temp_cont)
        # add the result (temp var) to the operand stack
        result_type = semantic_cube.cube[right_operand_type, left_operand_type, token]
        # add the result type (temp var) to the type stack
        quad_helper.push_type(code_to_type.get(result_type))
        # increase counter for temp/result vars
        quad_helper.temp_cont = quad_helper.temp_cont + 1
    else:
        error_helper.add_error(301)


# --- NON-LINEAR STATEMENTS (INTERMEDIATE REPRESENTATION) ---

# --- CONDITIONALS ---

# Actions to produce intermediate representation for non-linear statements using quadruples
# snp for single IF
def p_snp_conditional_statement_1(p):
    """snp_conditional_statement_1 : empty"""
    top_type_code = quad_helper.pop_type()

    # Check if top_oper's type is type bool(1)
    if code_to_type.get(top_type_code) is "bool":
        result = quad_helper.pop_operand()
        # debbuging
        # print("result", result)
        quad_helper.add_quad(token_to_code.get("GOTOF"), result, -1, "pending")
        quad_helper.push_jump(quad_helper.quad_cont - 1)
        # debbuging
        # print("Jump", quad_helper.quad_cont)
    else:
        error_helper.add_error(
            0, "Type Missmatch: Expression is not a bool"
        )  # TODO define code and custom error message


def p_snp_conditional_statement_2(p):
    """snp_conditional_statement_2 : empty"""
    end = quad_helper.pop_jump()
    cont = quad_helper.quad_cont
    quad_helper.fill(end, cont)


def p_snp_conditional_statement_3(p):
    """snp_conditional_statement_3 : empty"""
    quad_helper.add_quad(token_to_code.get("GOTO"), -1, -1, "pending")
    false = quad_helper.pop_jump()
    count = quad_helper.quad_cont
    quad_helper.push_jump(count - 1)
    # debbuging
    # print(count-1, false)
    # print(quad_helper.top_jump())
    quad_helper.fill(false, count)
# LOOPS

def p_snp_while_1(p):
    """snp_while_1 : empty"""
    count = quad_helper.quad_cont
    quad_helper.push_jump(count)


def p_snp_while_3(p):
    """snp_while_3 : empty"""
    end  = quad_helper.pop_jump()
    ret = quad_helper.pop_jump()
    quad_helper.add_quad(token_to_code.get("GOTO"), -1, -1, ret)
    count = quad_helper.quad_cont
    quad_helper.fill(end, count)

def is_var_in_current_scope(var_name):
    return var_name in procedure_directory[curr_scope]["var_table"]


import ply.yacc as yacc

parser = yacc.yacc()
