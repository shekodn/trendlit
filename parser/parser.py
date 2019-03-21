#!/usr/bin/python3

from lexer.lexer import lexer, tokens


procedure_directory = {}  # [name] = {type, var_table}

curr_scope = ""  # The current scope inside the program
curr_type = ""  # The current type used (module or var)


def p_program(p):
    """program : PROGRAM ID program1"""
    print("it compiles !")


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
        | empty"""


def p_simpleBlock(p):
    """simpleBlock : OBRACE simpleBlock1 CBRACE"""


def p_simpleBlock1(p):
    """simpleBlock1 : statement simpleBlock1
        | empty"""


def p_declareBlock(p):
    """declareBlock : declare declareBlock
        | empty"""


def p_declare(p):
    """declare : type ID snp_add_var
        | type ID snp_add_var initializeSlices
        | initialize"""


def p_initialize(p):
    """initialize : type initialize1 initialize2"""


def p_initialize1(p):
    """initialize1 : ID snp_add_var EQ value
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
        | module
        | writing"""


def p_assignment(p):
    """assignment : ID assignmentSlice EQ expression"""


def p_assignmentSlice(p):
    """assignmentSlice : assignmentSlice1D
        | assignmentSlice2D
        | empty"""


def p_assignmentSlice1D(p):
    """assignmentSlice1D : OBRACK expression CBRACK"""


def p_assignmentSlice2D(p):
    """assignmentSlice2D : OBRACK expression CBRACK OBRACK expression CBRACK"""


def p_expression(p):
    """expression : exp expression1"""


def p_expression1(p):
    """expression1 : REL exp
        | ASSOCIATIVE exp
        | empty"""


def p_exp(p):
    """exp : term exp1"""


def p_exp1(p):
    """exp1 : SIGN exp exp1
        | empty"""


def p_term(p):
    """term : factor term1"""


def p_term1(p):
    """term1 : OP term term1
        | empty"""


def p_factor(p):
    """factor : OPAREN expression CPAREN
        | factor1"""


def p_factor1(p):
    """factor1 : value
        | SIGN value"""


def p_value(p):
    """value : ID
        | valueSlice
        | call
        | CTEI
        | CTED
        | CTESTR
        | FALSE
        | TRUE"""


def p_valueSlice(p):
    """valueSlice : valueSlice1D
        | valueSlice2D"""


def p_valueSlice1D(p):
    """valueSlice1D : ID OBRACK expression CBRACK"""


def p_valueSlice2D(p):
    """valueSlice2D : ID OBRACK expression CBRACK OBRACK expression CBRACK"""


def p_condition(p):
    """condition : IF OPAREN expression CPAREN simpleBlock condition1"""


def p_condition1(p):
    """condition1 : ELSE simpleBlock
        | empty"""


def p_cycle(p):
    """cycle : LOOP OPAREN expression CPAREN simpleBlock"""


def p_module(p):
    """module : DEF ID snp_add_module OPAREN arguments CPAREN module1 snp_end_module"""


def p_module1(p):  # TODO: are we allowing func declaration inside a func ?
    """module1 : snp_save_void_type block
        | COLON type OBRACE declareBlock module2 CBRACE"""


def p_module2(p):
    """module2 : statement module2
        | SPIT expression"""


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
    # if procedure_directory.has_key(module_name):
    if module_name in procedure_directory:
        print(
            "Module '%s' has already been declared" % module_name
        )  # TODO : is this the best way to give an error?
        exit(1)
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
    # Check if var already exists and add it to the table in currect scope
    # if procedure_directory[curr_scope]["var_table"].has_key(var_name):
    if var_name in procedure_directory[curr_scope]["var_table"]:
        print(
            "Variable '%s' has already been declared" % var_name
        )  # TODO : is this the best way to give an error?
        exit(1)
    else:
        procedure_directory[curr_scope]["var_table"][var_name] = {
            "type": curr_type
        }  # TODO : add more info later on


import ply.yacc as yacc

parser = yacc.yacc()

# import sys
#
# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         file = sys.argv[1]
#         try:
#             f = open(file, "r")
#             data = f.read()
#             f.close()
#             yacc.parse(data, tracking=True)
#         except EOFError:
#             print("EOFError")
#     else:
#         print("File missing")
