#!/usr/bin/python3
from memory.memory import Memory
from lexer.lexer import lexer, tokens
from parser.parser_helper import ParserHelper
from quadruple.quadruple_helper import *
from quadruple.quadruple import *
from semantic_cube.semantic_cube import Cube
from semantic_cube.semantic_cube_helper import (
    code_to_type,
    token_to_code,
    type_to_code,
    type_to_init_value,
    scope_to_code,
    code_to_scope,
)
from error.error_helper import ErrorHelper

parser_helper = ParserHelper()
quad_helper = QuadrupleHelper()
error_helper = ErrorHelper()
semantic_cube = Cube()
memory = Memory()


def p_program(p):
    """program : PROGRAM ID program1"""
    # print("DIR TABLE: ", parser_helper.procedure_directory)


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
        | SPIT snp_return_module voidModuleBlock1
        | SPIT expression snp_return_module returnModuleBlock1
        | empty"""


def p_voidModuleBlock(p):
    """voidModuleBlock : snp_save_void_type snp_save_type_to_module_table OBRACE snp_add_quad_cont_to_table declareBlock voidModuleBlock1 CBRACE"""


def p_voidModuleBlock1(p):
    """voidModuleBlock1 : statement voidModuleBlock1
        | SPIT snp_return_module voidModuleBlock1
        | empty"""


def p_returnModuleBlock(p):
    """returnModuleBlock : COLON type snp_save_type_to_module_table OBRACE snp_add_quad_cont_to_table declareBlock returnModuleBlock1 CBRACE"""


def p_returnModuleBlock1(p):
    """returnModuleBlock1 : statement returnModuleBlock1
        | SPIT expression snp_return_module returnModuleBlock1
        | empty"""


def p_declareBlock(p):
    """declareBlock : declare declareBlock
        | empty"""


def p_declare(p):
    """declare : type ID snp_add_var snp_push_solitary_operand
        | type ID snp_add_var initializeSlices snp_add_dimension EQ constSlices
        | initialize"""


def p_initialize(p):
    """initialize : type initialize1 initialize2"""


def p_initialize1(p):
    """initialize1 : ID snp_add_var snp_push_pending_operand EQ snp_push_pending_token value snp_add_assignation_quad"""


def p_initialize2(p):
    """initialize2 : COMMA initialize1 initialize2
        | empty"""


def p_initializeSlices(p):
    """initializeSlices : initializeSlices1D
        | initializeSlices2D"""


def p_initializeSlices1D(p):
    """initializeSlices1D : OBRACK CTEI CBRACK snp_increase_dimension_count"""
    # """initializeSlices1D : OBRACK CTEI snp_check_ctei CBRACK snp_increase_dimension_count"""


def p_initializeSlices2D(p):
    """initializeSlices2D : OBRACK CTEI CBRACK snp_increase_dimension_count OBRACK CTEI CBRACK snp_increase_dimension_count"""


def p_constSlices(p):
    """constSlices : constSlice1D
        | constSlice2D"""


def p_constSlice1D(p):
    """constSlice1D : OBRACK CBRACK  snp_init_slice_1d"""


def p_constSlice1D1(p):
    """constSlice1D1 : COMMA value constSlice1D1
        | empty"""


# TODO: FIX 2D SLICE
def p_constSlice2D(p):
    """constSlice2D : OBRACK constSlice1D constSlice2D1 CBRACK
        | OBRACK constSlice1D CBRACK"""


def p_constSlice2D1(p):
    """constSlice2D1 : COMMA constSlice1D constSlice2D1
        | empty"""


def p_type(p):
    """type : STR snp_save_type
        | INT snp_save_type
        | DOUBLE snp_save_type
        | BOOL snp_save_type"""


def p_statement(p):
    """statement : assignment
        | condition
        | cycle
        | doCycle
        | call
        | writing"""


def p_assignment(p):
    """assignment : ID snp_push_pending_operand EQ snp_push_pending_token expression snp_add_assignation_quad
    | valueSlice EQ snp_push_pending_token expression snp_add_assignation_quad"""


# LOGICAL => "or|and"
def p_expression(p):
    """expression : rel_expression expression1 snp_check_precedence_and_create_quadruple_for_logic"""


def p_expression1(p):
    """expression1 : ASSOCIATIVE snp_push_pending_token expression
        | empty"""


# REL => is|not|>=|<=|>|<
def p_rel_expression(p):
    """rel_expression : exp rel_expression1 snp_check_precedence_and_create_quadruple_for_rel"""


def p_rel_expression1(p):
    """rel_expression1 : REL snp_push_pending_token exp rel_expression1
    | empty"""


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
    """value : ID snp_checks_for_previous_declaration snp_push_pending_operand
        | valueSlice
        | exp_call
        | CTEI snp_save_type_int snp_push_pending_operand
        | CTED snp_save_type_double snp_push_pending_operand
        | CTESTR snp_save_type_str snp_push_pending_operand
        | FALSE snp_save_type_bool snp_push_pending_operand
        | TRUE snp_save_type_bool snp_push_pending_operand"""


def p_slice_expression(p):
    """slice_expression : slice_exp slice_expression1 snp_check_precedence_and_create_quadruple_for_rel"""


# ASSOCIATIVE => "or|and"
def p_slice_expression1(p):
    """slice_expression1 : REL snp_push_pending_token slice_exp
        | empty"""
    # TODO add single expression. Do we allow if(True) ???


# Reference: Mathematical Expressions
# snp_check_precedence_and_create_quadruple => STEP 4
def p_slice_exp(p):
    """slice_exp : slice_term snp_check_precedence_and_create_quadruple_for_sign slice_exp1"""


# Reference: Mathematical Expressions
# snp_push_pending_token => STEP 2
def p_slice_exp1(p):
    """slice_exp1 : SIGN snp_push_pending_token slice_exp slice_exp1
        | empty"""


def p_slice_term(p):
    """slice_term : slice_factor snp_check_precedence_and_create_quadruple_for_op slice_term1"""


# Reference: Mathematical Expressions
# snp_push_pending_token => STEP 3
def p_slice_term1(p):
    """slice_term1 : OP snp_push_pending_token slice_term slice_term1
        | empty"""


def p_slice_factor(p):
    """slice_factor : OPAREN snp_push_pending_token slice_expression CPAREN snp_clean_stack_until_false_bottom
        | slice_factor1"""


def p_slice_factor1(p):
    """slice_factor1 : slice_value
        | SIGN slice_value"""


def p_slice_value(p):
    """slice_value : ID snp_checks_for_previous_declaration snp_push_pending_operand
        | CTEI snp_save_type_int snp_push_pending_operand"""


def p_valueSlice(p):
    """valueSlice : valueSlice1D """


def p_valueSlice1D(p):
    """valueSlice1D : ID snp_update_curr_slice snp_push_pending_operand OBRACK snp_increase_dim_access_count snp_slice_access_2 snp_push_start_false_bottom slice_expression snp_slice_access_3 CBRACK snp_clean_stack_until_false_bottom snp_reset_dim_access_count"""


def p_condition(p):
    """condition : IF OPAREN expression CPAREN snp_conditional_statement_1 simpleBlock condition1 snp_conditional_statement_2"""


def p_condition1(p):
    """condition1 : ELSE snp_conditional_statement_3 simpleBlock
        | empty"""


def p_cycle(p):
    """cycle : LOOP snp_while_1 OPAREN expression CPAREN snp_conditional_statement_1 simpleBlock snp_while_3"""


def p_doCycle(p):
    """doCycle : DO snp_while_1 simpleBlock LOOP OPAREN expression CPAREN snp_do_while_gotot"""


def p_module(p):
    """module : DEF ID snp_add_module OPAREN arguments CPAREN snp_add_params_count_to_table module1 snp_end_module"""


def p_module1(p):
    """module1 : voidModuleBlock
        | returnModuleBlock"""


def p_call(p):
    """call : ID snp_verify_module_existance call1 snp_add_gosub"""


def p_exp_call(p):
    """exp_call : ID snp_verify_module_existance call1 snp_check_return snp_add_gosub"""


def p_call1(p):
    """call1 : OPAREN snp_add_era_size_quad params CPAREN"""


def p_params(p):
    """params : expression snp_check_param params1
        | empty"""


def p_params1(p):
    """params1 : COMMA params
        | empty"""


def p_writing(p):
    """writing : EVAL OPAREN writing1 CPAREN"""


def p_writing1(p):
    """writing1 : snp_push_pending_eval_token expression snp_add_eval_quad writing2"""


def p_writing2(p):
    """writing2 : COMMA writing1
        | empty"""


# snp_add_var is the equivalent of snp #2 and #3 from Intermediate code actions
# for module definitions
def p_arguments(p):
    """arguments : type ID snp_add_var snp_counts_params arguments1
        | empty"""


# snp_add_var is the equivalent of snp #2 and #3 from Intermediate code actions
# for module definitions
def p_arguments1(p):
    """arguments1 : COMMA type ID snp_add_var snp_counts_params arguments1
        | empty"""


def p_tag(p):
    """tag : H1 html_class snp_open_html_tag
        | H2 html_class snp_open_html_tag
        | H3 html_class snp_open_html_tag
        | H4 html_class snp_open_html_tag
        | H5 html_class snp_open_html_tag
        | H6 html_class snp_open_html_tag
        | DIV html_class snp_open_html_tag
        | P html_class snp_open_html_tag
        | TABLE html_class snp_open_html_tag
        | TH html_class snp_open_html_tag
        | TR html_class snp_open_html_tag
        | THEAD html_class snp_open_html_tag
        | TD html_class snp_open_html_tag
        | TBODY html_class snp_open_html_tag
        | OL html_class snp_open_html_tag
        | UL html_class snp_open_html_tag
        | LI html_class snp_open_html_tag
        | SPAN html_class snp_open_html_tag
        | LINK html_href snp_open_html_tag
        | IMG html_img snp_open_html_tag
        | HEAD html_class snp_open_html_tag
        """


def p_html_class(p):
    """html_class : CLASS COLON CTESTR snp_class_quad
        | empty"""


def p_html_href(p):
    """html_href : HREF COLON CTESTR snp_href_quad
        | empty"""


def p_html_img(p):
    """html_img : SRC COLON CTESTR snp_img_quad
        | empty"""


# def p_html_head_class():
#     """html_head_class : CLASS COLON CTESTR snp_head_quad
#         | empty"""

# gorritos <^ ^>
def p_htmlscript(p):
    """htmlscript : OEVALSCRIPT snp_push_eval_pending_token expression CEVALSCRIPT snp_add_eval_quad"""


def p_empty(p):
    """empty :"""


# TODO : Add a nice error to the error queue here
# Cannot use error_helper since program needs to exit.
# Othwerwise it doesn't know where to go next (aka se cicla)
# Reference: https://github.com/dabeaz/ply/blob/dca6c606d63d4729a395f30953456b0f00d4f443/ply/lex.py#L66
def p_error(p):
    # For debbuging
    # print("Type: ", p.type)
    # print("Value: ", p.value)
    # print("Line #", p.lineno)
    # print("lexpos? #", p.lexpos)
    print("Syntax error at '%s'" % p)
    exit(1)


# --- HTML ---


def p_htmltag(p):
    """htmltag : tag OBRACE html_block CBRACE snp_close_html_tag
    | BR snp_br_html_tag OBRACE CBRACE"""


def p_html_block(p):
    """html_block : html_statement html_block
    | htmltag html_block
    | empty"""


def p_html_statement(p):
    """html_statement : html_assignment
    | html_condition
    | htmlscript
    | html_cycle
    | html_do_cycle
    | html_call
    | writing"""


def p_html_assignment(p):
    """html_assignment : INITCODEHTML ID snp_push_pending_operand EQ snp_push_pending_token expression snp_add_assignation_quad CCODEHTML"""


def p_html_condition(p):
    """html_condition : INITCODEHTML IF OPAREN expression CPAREN snp_conditional_statement_1 CCODEHTML html_block html_condition1_else html_end_condition"""


def p_html_condition1_else(p):
    """html_condition1_else : HTMLELSE snp_conditional_statement_3 html_block
    | empty"""


def p_html_end_condition(p):
    """html_end_condition : HTMLEND snp_conditional_statement_2"""


def p_html_cycle(p):
    """html_cycle : INITCODEHTML LOOP snp_while_1 OPAREN expression CPAREN CCODEHTML snp_conditional_statement_1 html_block html_end_cycle snp_while_3"""


def p_html_end_cycle(p):
    """html_end_cycle : HTMLEND"""


def p_html_do_cycle(p):
    """html_do_cycle : INITCODEHTML DO CCODEHTML snp_while_1 html_block html_end_do_cycle"""


def p_html_end_do_cycle(p):
    """html_end_do_cycle : HTMLENDDO OPAREN expression CPAREN CCODEHTML snp_do_while_gotot"""


def p_html_call(p):
    """html_call : INITCODEHTML ID snp_verify_module_existance OPAREN snp_add_era_size_quad params CPAREN snp_add_gosub CCODEHTML"""


# --- SEMANTIC NEURAL POINTS ---

# --- PROCEDURE/MODULE SEMANTIC ACTIONS---

# Start of script global scope (adds global scope to directory)
def p_snp_script_start(p):
    """snp_script_start : empty"""
    # global parser_helper.procedure_directory, parser_helper.curr_scope, parser_helper.curr_type
    # Set current values for global script
    parser_helper.curr_scope = "global_script"
    parser_helper.curr_type = "void"
    # Add global script to the directory
    parser_helper.procedure_directory[parser_helper.curr_scope] = {
        "type": parser_helper.curr_type,
        "scope_type": scope_to_code.get("global"),
        "params_count": 0,
        "queue_params": [],
        "queue_params_addresses": [],
        "starting_quad": -1,
        "var_table": {},
        "dim_list": {},
    }  # TODO : add more info later on


# Start of the module (add module to directory)
def p_snp_add_module(p):
    """snp_add_module : empty"""
    # global parser_helper.procedure_directory, parser_helper.curr_scope
    module_name = p[-1]  # get the last symbol read (left from this neural point)
    # Check if module already exists and add it to the directory
    # debbuging
    # print("TABLEE! parser_helper.procedure_directory", parser_helper.procedure_directory, "module to add:", module_name, "\n")
    if module_name in parser_helper.procedure_directory:
        error_message = f"Module {module_name} has already been declared"
        error_helper.add_error(0, error_message)
    else:
        parser_helper.procedure_directory[module_name] = {
            "type": None,
            "scope_type": scope_to_code.get("local"),
            "params_count": 0,
            "queue_params": [],
            "queue_params_addresses": [],
            "starting_quad": -1,
            "var_table": {},
            "dim_list": {},
        }  # TODO : add more info later on
        parser_helper.curr_scope = module_name
        memory.curr_scope_type = scope_to_code.get("local")
        quad_helper.add_quad(token_to_code.get("GOTO"), -1, -1, "pending_endproc")
        quad_helper.push_jump(quad_helper.quad_cont - 1)


# Save the last type defined
def p_snp_save_type_to_module_table(p):
    """snp_save_type_to_module_table : empty"""
    module_name = parser_helper.curr_scope

    parser_helper.procedure_directory[module_name]["type"] = parser_helper.curr_type

    # print("Curr type module_name", parser_helper.curr_type, module_name)
    var_memory_address = memory.set_var_addr(
        scope_to_code.get("global"), parser_helper.curr_type
    )
    if var_memory_address is not None:
        # print("MEMORY ADDRE ", var_memory_address)
        parser_helper.add_var_to_table(module_name, var_memory_address, "global_script")


# Save the last type defined
def p_snp_save_type(p):
    """snp_save_type : empty"""
    parser_helper.curr_type = p[-1]


# Save the last type as void (for modules)
def p_snp_save_void_type(p):
    """snp_save_void_type : empty"""
    parser_helper.curr_type = "void"


# --- ARRAYS - SLICES ---
# Acciones para el acceso a una variable dimensionada
def p_snp_add_dimension(p):
    """snp_add_dimension : empty"""
    slice_name = p[-3]
    # Add dimension to var table
    parser_helper.procedure_directory[parser_helper.curr_scope]["var_table"][
        slice_name
    ]["dimensions"] = parser_helper.curr_dimension_counter
    # Add slice to dimensioned var list
    slice_addr = parser_helper.get_var_address_from_dir(slice_name)
    parser_helper.procedure_directory[parser_helper.curr_scope]["dim_list"][
        slice_addr
    ] = slice_name
    # For debuging
    # print("DIMENSIONED VAR LIST \n")
    # print(parser_helper.procedure_directory[parser_helper.curr_scope]["dim_list"])

    # segunda pasada
    if parser_helper.curr_dimension_counter is 2:
        lower_limit = 0
        upper_limit = parser_helper.get_upper_limit(slice_name, 1)
        # For debuging
        # print("R ", parser_helper.curr_r, "Upper", upper_limit, "Lower", lower_limit)
        m1 = parser_helper.curr_r / ((int(upper_limit) - lower_limit + 1))
        parser_helper.procedure_directory[parser_helper.curr_scope]["var_table"][
            parser_helper.curr_slice
        ]["t_dimensions"]["m1"] = int(m1)
        const_addr = memory.get_or_set_addr_const(m1, "int")
        upper_limit = parser_helper.get_upper_limit(slice_name, 2)
        # m2 = m1/((int(upper_limit) - lower_limit + 1))
        k = 0
        parser_helper.procedure_directory[parser_helper.curr_scope]["var_table"][
            parser_helper.curr_slice
        ]["t_dimensions"]["m2"] = k
        const_addr = memory.get_or_set_addr_const(k, "int")
    #
    scope_type = parser_helper.get_scope_type(parser_helper.curr_scope)
    slice_type = parser_helper.get_var_type_from_dir(slice_name)
    memory.increase_next_mem(scope_type, slice_type, parser_helper.curr_r)

    # for debbuging
    # print("curr_r", parser_helper.curr_r)
    # print(f"Adding {parser_helper.curr_dimension_counter} dim for {slice_name} ")
    # print(
    #     "Dim Table: ",
    #     parser_helper.procedure_directory[parser_helper.curr_scope]["var_table"][
    #         parser_helper.curr_slice
    #     ],
    # )

    # Reset dimension count
    parser_helper.curr_dimension_counter = 0
    # Reset curr R
    parser_helper.curr_r = 1
    # for debbuging
    # print("NETX ADDRESSS ", memory.next_mem_global_int)
    # print(
    #     "var_table : ",
    #     parser_helper.procedure_directory[parser_helper.curr_scope]["var_table"]
    # )


# primera pasada
def p_snp_increase_dimension_count(p):
    """snp_increase_dimension_count : empty"""
    upper_limit = p[-2]
    ctei = int(upper_limit)

    # Checks that array has a value bigger than 0
    if ctei <= 0:
        error_helper.add_error(
            305, f"Slice index value ({ctei}) should be a CTEI greater than 0"
        )

    # indicates another dimension in slice
    parser_helper.curr_dimension_counter += 1
    # adds upper limit to t_dimensions
    dim_count = parser_helper.curr_dimension_counter
    parser_helper.procedure_directory[parser_helper.curr_scope]["var_table"][
        parser_helper.curr_slice
    ]["t_dimensions"]["ls" + str(dim_count)] = upper_limit
    const_addr = memory.get_or_set_addr_const(upper_limit, "int")
    # print("UPPER", parser_helper.curr_slice, "ls"+str(dim_count), upper_limit)
    # calculates R
    lower_limit = 0
    parser_helper.curr_r = parser_helper.curr_r * (int(upper_limit) - lower_limit + 1)


def p_snp_slice_access_2(p):
    """snp_slice_access_2 : empty"""
    var_addr = quad_helper.pop_operand()
    slice_name = parser_helper.get_dimensioned_name(var_addr)
    # For debuging
    # print(f"Var addr: {var_addr}")
    # print(f"Var name: {slice_name}")

    # Verifies that ud is a Dimnensional Variable
    if slice_name is not None:
        dim = parser_helper.get_dimensions(slice_name)

        # Check if dimension being accessed is valid
        dim_counter = parser_helper.curr_dimension_counter

        if not (dim <= dim_counter):
            error_helper.add_error(202, f": {slice_name}")
    else:
        error_helper.add_error(302, f"{slice_name} is not defined")


def p_snp_slice_access_3(p):
    """ snp_slice_access_3 : empty """
    s = quad_helper.pop_operand()  # No se saca

    slice_name = parser_helper.curr_slice
    slice_type = parser_helper.get_var_type_from_dir(slice_name)
    # print(f"slice_name: {slice_name}, dim: {parser_helper.curr_dimension_counter}")

    # Add VER quad
    lower_limit = 0
    upper_limit = parser_helper.get_upper_limit(
        slice_name, parser_helper.curr_dimension_counter
    )

    lower_limit_addr = memory.get_or_set_addr_const("0", "int")
    upper_limit_addr = memory.get_or_set_addr_const(upper_limit, "int")
    # print(f"lower_limit: {lower_limit}, upper_limit: {upper_limit}")
    quad_helper.add_quad(
        token_to_code.get("VER"), lower_limit_addr, upper_limit_addr, s
    )

    # Add base address to quad : +dirB(slice)
    base_dir = parser_helper.get_var_address_from_dir(slice_name)
    # assign memory address to temporary result variable and increase counter for temp/result vars
    temp_memory_address = memory.set_addr_temp("int")  # should always be an int
    # add the quad
    # assigns a constant to the base_dir so that VM can read it properly
    base_dir_addr = memory.get_or_set_addr_const(str(base_dir), "int")
    quad_helper.add_quad(token_to_code.get("+"), s, base_dir_addr, temp_memory_address)

    # Agregar (dircasilla) [pointer like address]
    # Push a la pila con la (dircasilla) para que el siguiente cuadruplo la use
    ptr_addr_cell = memory.set_addr_ptr(temp_memory_address)
    # For debugging
    # print(
    #     f"curr scope: {code_to_scope.get(parser_helper.get_scope_type(parser_helper.curr_scope))} addr_ptr: {ptr_addr_cell}"
    # )
    quad_helper.push_operand(ptr_addr_cell)


def p_snp_update_curr_slice(p):
    """snp_update_curr_slice : empty"""
    var_name = p[-1]
    parser_helper.curr_slice = var_name


def p_snp_increase_dim_access_count(p):
    """snp_increase_dim_access_count : empty"""
    # indicates another dimension in slice
    parser_helper.curr_dimension_counter += 1


def p_snp_reset_dim_access_count(p):
    """snp_reset_dim_access_count : empty"""
    # indicates another dimension in slice
    parser_helper.curr_dimension_counter = 0


def p_snp_init_slice_1d(p):
    """snp_init_slice_1d : empty"""
    # print("curr slice", parser_helper.curr_slice)
    slice_name = parser_helper.curr_slice
    slice_type = parser_helper.get_var_type_from_dir(slice_name)

    if slice_type in type_to_code:
        upper_limit = int(parser_helper.get_upper_limit(slice_name, 1))

        counter = 0
        default_value = type_to_init_value.get(slice_type)
        default_initial_value_address = memory.get_or_set_addr_const(
            default_value, slice_type
        )
        operand_address = parser_helper.get_var_address_from_dir(slice_name)

        while upper_limit > counter:
            quad_helper.add_quad(
                token_to_code.get("="),
                default_initial_value_address,
                -1,
                operand_address,
            )
            # for debugging
            # print("=", default_initial_value_address, -1, operand_address)
            counter += 1
            operand_address += 1

    else:
        print("Error: Invalid type")


# Add a false bottom to maintain presedence with arrays []
def p_snp_push_start_false_bottom(p):
    """snp_push_start_false_bottom : empty"""
    quad_helper.push_token("(")
    # debbuging
    # print("pushed token", quad_helper.top_token())


def p_snp_return_module(p):
    """snp_return_module : empty"""
    if parser_helper.curr_scope is "global_script":
        error_helper.add_error(0, "FIX ME")
    else:
        add_ret_endproc_quad()


# End of the module deltes the var table
# snp #7 in Intermediate Code Actions for Module Definition
def p_snp_end_module(p):
    """snp_end_module : empty"""
    # add_ret_endproc_quad()
    curr_module_type = parser_helper.procedure_directory[parser_helper.curr_scope][
        "type"
    ]
    if curr_module_type is "void":  # VOID MODULE
        # Delete var table for the module that ended
        quad_helper.add_quad(token_to_code.get("ENDPROC"), -1, -1, -1)
    reset_local_contex()
    end = quad_helper.pop_jump()
    cont = quad_helper.quad_cont
    quad_helper.fill(end, cont)


def reset_local_contex():
    # debbuging
    # print(f"CURR SCOPE: {parser_helper.curr_scope}")
    # print(f"TABLE: {parser_helper.procedure_directory} \n")
    parser_helper.procedure_directory[parser_helper.curr_scope]["var_table"].clear()
    memory.reset_local_vars()
    parser_helper.curr_scope = "global_script"
    memory.curr_scope_type = scope_to_code.get("global")


def add_ret_endproc_quad():
    curr_module_type = parser_helper.procedure_directory[parser_helper.curr_scope][
        "type"
    ]
    if curr_module_type is "void":  # VOID MODULE
        # Delete var table for the module that ended
        quad_helper.add_quad(token_to_code.get("ENDPROC"), -1, -1, -1)
    else:  # RETURNING MODULE
        return_value = quad_helper.pop_operand()
        return_type = code_to_type.get(quad_helper.pop_type())
        if return_type != curr_module_type:
            print(
                f"return_type: {return_type}, return_value: {return_value}, curr_module_type: {curr_module_type}"
            )
            error_helper.add_error(301, f"Return type is a mismatch")
        else:
            quad_helper.add_quad(
                token_to_code.get("RET"), return_value, -1, "memory address"
            )


# --- VARIABLE SEMANTIC ACTIONS ---

# Adds a variable defined to the current scope variable table
def p_snp_add_var(p):
    """snp_add_var : empty"""
    var_name = p[-1]  # get the last symbol read (left from this neural point)
    # For debbuging
    # Check if var already exists and add it to the table in currect scope
    if parser_helper.is_var_in_current_scope(var_name):
        error_message = f"Variable {var_name} has already been declared"
        error_helper.add_error(0, error_message)
    else:
        scope_type = parser_helper.get_scope_type(parser_helper.curr_scope)
        var_memory_address = memory.set_var_addr(scope_type, parser_helper.curr_type)
        parser_helper.curr_slice = var_name
        parser_helper.add_var_to_table(
            var_name, var_memory_address, parser_helper.curr_scope
        )

    #     parser_helper.procedure_directory[parser_helper.curr_scope]["var_table"][
    #         var_name
    #     ] = {
    #         "type": parser_helper.curr_type,
    #         "memory_address": var_memory_address,
    #     }  # TODO : add more info later on
    # # For debbuging
    # # print("MEMROEY ADDRESS FOR VAR: ", var_memory_address)
    # # print(
    # #     f"var_name {var_name}, current_scope, {parser_helper.curr_scope}, SCOPE TYPE: {scope_type}"
    # # )
    # # print("ProcDir for curr_scope:", parser_helper.procedure_directory, "\n")


# ---  ESTATUTOS SECUENCIALES ---
def p_snp_add_eval_quad(p):
    """snp_add_eval_quad : empty"""
    quad_helper.add_quad(quad_helper.pop_token(), -1, -1, quad_helper.pop_operand())


# --- MATHEMATICAL EXPRESSIONS (INTERMEDIATE REPRESENTATION) ---
# PUSH PilaO (id)
def p_snp_push_pending_operand(p):
    """snp_push_pending_operand : empty"""
    operand_id = p[-2] if p[-1] == None else p[-1]
    operand_type = parser_helper.get_var_type_from_dir(operand_id)
    quad_helper.push_type(operand_type)
    if parser_helper.is_var_declared(operand_id):
        operand_address = parser_helper.get_var_address_from_dir(operand_id)
    else:  # operand is a constant
        operand_address = memory.get_or_set_addr_const(operand_id, operand_type)
    quad_helper.push_operand(operand_address)
    # For debbuging
    # print("OPERAND", operand_id, quad_helper.top_operand())
    # print("TYPE", quad_helper.top_type())


def p_snp_save_type_int(p):
    """snp_save_type_int : empty"""
    parser_helper.curr_type = "int"
    # For debugging
    # print("save ", p[-1])


def p_snp_save_type_double(p):
    """snp_save_type_double : empty"""
    parser_helper.curr_type = "double"


def p_snp_save_type_str(p):
    """snp_save_type_str : empty"""
    parser_helper.curr_type = "str"


def p_snp_save_type_bool(p):
    """snp_save_type_bool : empty"""
    parser_helper.curr_type = "bool"


def p_snp_push_pending_token(p):
    """snp_push_pending_token : empty"""
    token = p[-1]
    quad_helper.push_token(token)
    # debbuging
    # print("pushed token: ", quad_helper.top_token())


def p_snp_push_pending_eval_token(p):
    """snp_push_pending_eval_token : empty"""
    quad_helper.push_token("eval")


def p_snp_push_solitary_operand(p):
    """snp_push_solitary_operand : empty"""

    """
    Variables declared without a corresponding initialization are zero-valued.
    For example, the zero value for an int is 0
    """
    operand_id = p[-2]
    operand_address = parser_helper.get_var_address_from_dir(operand_id)
    type = parser_helper.procedure_directory[parser_helper.curr_scope]["var_table"][
        operand_id
    ]["type"]
    default_initial_value = type_to_init_value.get(type)
    default_initial_value_address = memory.get_or_set_addr_const(
        default_initial_value, type
    )
    operator = token_to_code.get("=")

    quad_helper.add_quad(operator, default_initial_value_address, -1, operand_address)
    # for debbuging
    # print("Type", type, "address", default_initial_value_address)


def p_snp_add_assignation_quad(p):
    """snp_add_assignation_quad : empty"""
    add_quadruple_assignation()


def add_quadruple_assignation():
    right_operand = quad_helper.pop_operand()  # TODO: type int
    right_operand_type = quad_helper.pop_type()
    left_operand = quad_helper.pop_operand()  # TODO: type str
    left_operand_type = quad_helper.pop_type()
    token = quad_helper.pop_token()

    if semantic_cube.is_in_cube(right_operand_type, left_operand_type, token):  # baila?
        quad_helper.add_quad(token, right_operand, -1, left_operand)  # assignation
    else:
        error_helper.add_error(301)
    # For debbuging
    # print(
    #     "Semantic Cube Checked: ",
    #     "right: ",
    #     right_operand_type,
    #     "left: ",
    #     left_operand_type,
    #     "token: ",
    #     token,
    # )


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


# logic => "and|or"
def p_snp_check_precedence_and_create_quadruple_for_logic(p):
    """snp_check_precedence_and_create_quadruple_for_logic : empty"""
    top = quad_helper.top_token()
    and_op = token_to_code.get("and")
    or_op = token_to_code.get("or")

    is_logic = (top is and_op) or (top is or_op)

    if is_logic:
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
    # print("SMEMANTIC CUBE: ", right_operand, left_operand, token)
    # print("TYPES: ", right_operand_type, left_operand_type)
    if semantic_cube.is_in_cube(right_operand_type, left_operand_type, token):  # baila?
        # add the result (temp var) to the operand stack
        result_type = semantic_cube.cube[right_operand_type, left_operand_type, token]
        # assign memory address to temporary result variable and increase counter for temp/result vars
        temp_memory_address = memory.set_addr_temp(code_to_type.get(result_type))
        # add the quad
        quad_helper.add_quad(token, left_operand, right_operand, temp_memory_address)
        # expression
        quad_helper.push_operand(temp_memory_address)
        # add the result type (temp var) to the type stack
        quad_helper.push_type(code_to_type.get(result_type))
        # For debbuging
        # print("OPERAND", quad_helper.top_operand())
        # print("TYPE", quad_helper.top_type())
    else:
        error_helper.add_error(301)


def p_snp_checks_for_previous_declaration(p):
    """snp_checks_for_previous_declaration : empty"""
    var = p[-1]
    if not parser_helper.is_var_declared(var):
        error_helper.add_error(302, f"{var} doesn't exist")


# --- NON-LINEAR STATEMENTS (INTERMEDIATE REPRESENTATION) ---

# --- CONDITIONALS ---

# Actions to produce intermediate representation for non-linear statements using quadruples
# snp for single IF
# Equivalent to snp_while_2
def p_snp_conditional_statement_1(p):
    """snp_conditional_statement_1 : empty"""
    top_type_code = quad_helper.pop_type()
    result = quad_helper.pop_operand()

    # Check if top_oper's type is type bool(1)
    if code_to_type.get(top_type_code) is "bool":
        # debbuging
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
    end = quad_helper.pop_jump()
    ret = quad_helper.pop_jump()
    quad_helper.add_quad(token_to_code.get("GOTO"), -1, -1, ret)
    count = quad_helper.quad_cont
    quad_helper.fill(end, count)


def p_snp_do_while_gotot(p):
    """snp_do_while_gotot : empty"""
    top_type_code = quad_helper.pop_type()
    result = quad_helper.pop_operand()
    ret = quad_helper.pop_jump()

    # Check if top_oper's type is type bool(1)
    if code_to_type.get(top_type_code) is "bool":
        quad_helper.add_quad(token_to_code.get("GOTOT"), result, -1, ret)
    else:
        error_helper.add_error(
            0, "Type Missmatch: Expression is not a bool"
        )  # TODO define code and custom error message


###Intermediate Code Actions for a Module Definition
def p_snp_counts_params(p):
    """snp_counts_params : empty"""
    parser_helper.queue_params.append(type_to_code.get(parser_helper.curr_type))
    parser_helper.curr_module_param_counter = (
        parser_helper.curr_module_param_counter + 1
    )
    param_var_name = p[-2]
    param_var_addr = parser_helper.get_var_address_from_dir(param_var_name)
    parser_helper.queue_params_addresses.append(param_var_addr)
    # For debbuging
    # print ("Pushed type: ",parser_helper.queue_params[len(parser_helper.queue_params)-1])
    # print("PARAM NAME: ", param_var_name, "PARAM VALUE: ", param_var_addr)
    # print("Pushed addr: ",parser_helper.queue_params_addresses[len(parser_helper.queue_params_addresses)-1])


# snp_add_params_count_to_table is snp #4 in Intermediate Code Actions for Module Definition
def p_snp_add_params_count_to_table(p):
    """snp_add_params_count_to_table : empty"""
    # add counter value to table
    parser_helper.procedure_directory[parser_helper.curr_scope][
        "params_count"
    ] = parser_helper.curr_module_param_counter
    # add the param list to the table
    parser_helper.procedure_directory[parser_helper.curr_scope][
        "queue_params"
    ] = parser_helper.queue_params
    # add the param address list to the table
    parser_helper.procedure_directory[parser_helper.curr_scope][
        "queue_params_addresses"
    ] = parser_helper.queue_params_addresses
    # clears counter
    parser_helper.curr_module_param_counter = 0
    # clears the param list
    parser_helper.queue_params = []
    # clears the param address list
    parser_helper.queue_params_addresses = []
    # debbuging
    # counter = parser_helper.procedure_directory[parser_helper.curr_scope][
    #     "params_count"
    # ]
    # print(f"current scope: {parser_helper.curr_scope} counter: {counter}")


# --- INTERMEDIATECODE ACTIONS FOR MODULE DEFINITION (INTERMEDIATE REPRESENTATION) ---

# snp #6 in Intermediate Code Actions for Module Definition
def p_snp_add_quad_cont_to_table(p):
    """snp_add_quad_cont_to_table : empty"""
    parser_helper.procedure_directory[parser_helper.curr_scope][
        "starting_quad"
    ] = quad_helper.quad_cont
    # debbuging
    # print("I start from: ", parser_helper.procedure_directory[parser_helper.curr_scope]["starting_quad"])


# --- INTERMEDIATECODE ACTIONS FOR MODULE CALL (INTERMEDIATE REPRESENTATION) ---

# snp #1 Module Call
# Verify that the procedure exists in the Procedure Directory
def p_snp_verify_module_existance(p):
    """snp_verify_module_existance : empty"""
    module_name = p[-1]
    if not parser_helper.is_module_in_procedure_dir(module_name):
        error_helper.add_error(303, f"{module_name} doesn't exist")
    parser_helper.stack_calls.push(module_name)


# snp #2 Module Call
# Generate ERA size (Activation Record expansion - NEW - size)
# Add a pointer to the first prarameter type in the parameter table
def p_snp_add_era_size_quad(p):
    """snp_add_era_size_quad :  empty"""
    module_name = parser_helper.stack_calls.top()
    quad_helper.add_quad(token_to_code.get("ERA"), module_name, -1, -1)


# snp #3 Module Call
# Verify Argument type agains current parameter(#k) in parameter table
# Generate action PARAMETER, Argument, Argument#k
def p_snp_check_param(p):
    """snp_check_param : empty"""

    # # Get the last read parameter from the call
    input_param = quad_helper.pop_operand()
    input_param_type = quad_helper.pop_type()

    # parser_helper.stack_param_calls([])
    # top_queue = parser_helper.stack_param_calls.top()
    # top_queue.append(input_param_type)

    # Get the last call from the stack and its queue_params
    module_name = parser_helper.stack_calls.top()
    module_queue_params = parser_helper.get_queue_params(module_name)
    module_queue_params_addresses = parser_helper.get_queue_params_addresses(
        module_name
    )
    pointer = parser_helper.stack_param_pointers.top()

    # Check if param matches the type/order
    is_not_none = module_queue_params is not None
    if (
        is_not_none
        and pointer <= len(module_queue_params) - 1
        and input_param_type is module_queue_params[pointer]
    ):
        param_assigned_addr = module_queue_params_addresses[pointer]
        # print("MODULE PARAM ADDRES: ", module_queue_params_addresses)
        quad_helper.add_quad(
            token_to_code.get("PARAMETER"), input_param, -1, param_assigned_addr
        )  # assignation
    else:
        error_helper.add_error(301, "Params do not match type")
        # For debbuging
        # print("Expected: ",module_queue_params[pointer], " Received: ", input_param_type)
    # snp #4 Module Call - Increase pointer after check
    # Move to the next parameter (k++)
    param_pointer = parser_helper.stack_param_pointers.pop()
    parser_helper.stack_param_pointers.push(param_pointer + 1)


def p_snp_check_return(p):
    """snp_check_return : empty"""
    module_name = parser_helper.stack_calls.top()
    module_type = parser_helper.get_module_type(module_name)
    if module_type is "void" or module_type is "error":
        error_helper.add_error(
            301,
            f'Function "{module_name}" is void, therefore you cant use it to assign a value.',
        )


# snp #6 Module Call
# Generate quad GOSUB, procedure_name, -1, intitial-address
def p_snp_add_gosub(p):
    """snp_add_gosub : empty"""
    # Get the last call from the stack and its queue_params
    module_name = parser_helper.stack_calls.top()
    module_queue_params = parser_helper.get_queue_params(module_name)
    param_pointer = parser_helper.stack_param_pointers.top()
    # snp #5 Module Call
    # Verify that last parameter points to null (coherence in number of params)
    if module_queue_params is not None:
        # Clear the stack and pointer after call ends
        module_name = parser_helper.stack_calls.pop()
        parser_helper.stack_param_pointers.pop()
        parser_helper.stack_param_pointers.push(0)
        if param_pointer is len(module_queue_params):
            # Clear the stack and pointer after call ends
            module_quad_num = parser_helper.get_starting_quad(module_name)
            # Generate a quad with GOSUB, next_quad after this call, -1, quad where VM needs to jump
            quad_helper.add_quad(
                token_to_code.get("GOSUB"),
                quad_helper.quad_cont + 1,
                -1,
                module_quad_num,
            )
            # Assign return temporal to module
            module_type = parser_helper.get_module_type(module_name)
            # print("THE MODULE TYPE ", module_type)
            if module_type is not "void":
                # get the memory_address for the module variable
                if parser_helper.is_var_declared(module_name):
                    module_address = parser_helper.get_var_address_from_dir(module_name)
                    # get the memory_address for the return variable
                    temp_memory_address = memory.set_addr_temp(module_type)
                    # add the quad
                    quad_helper.add_quad(
                        token_to_code.get("="), module_address, -1, temp_memory_address
                    )
                    # For debbuging
                    # print(
                    #     "added quadd: ",
                    #     token_to_code.get("="),
                    #     module_address,
                    #     -1,
                    #     temp_memory_address,
                    # )
                    # expression
                    quad_helper.push_operand(temp_memory_address)
                    # add the result type (temp var) to the type stack
                    quad_helper.push_type(module_type)
                else:
                    print(
                        "HEL:LWDHkjSHD"
                    )  # TODO: lanzar un error de var/module not defined?
                    exit(1)
        else:
            error_helper.add_error(
                304,
                f"This function was expecting {len(module_queue_params)} params, but received {param_pointer}",
            )


# --- HTML ---


def p_snp_open_html_tag(p):
    """snp_open_html_tag : empty"""
    html_tag = p[-2].upper()
    quad_helper.push_tag(token_to_code.get(html_tag))
    quad_helper.add_quad(token_to_code.get("eval"), -1, -1, token_to_code.get(html_tag))
    # For debbuging
    # print("Html tag: ", html_tag)
    # print("Top tag: ", quad_helper.top_tag())


def p_snp_class_quad(p):
    """snp_class_quad : empty"""
    class_str = p[-1]
    cte_s = memory.get_or_set_addr_const(class_str, "str")
    quad_helper.add_quad(
        token_to_code.get("eval"), -1, cte_s, token_to_code.get("CLASS")
    )


def p_snp_href_quad(p):
    """snp_href_quad : empty"""
    href_str = p[-1]
    cte_s = memory.get_or_set_addr_const(href_str, "str")
    quad_helper.add_quad(
        token_to_code.get("eval"), -1, cte_s, token_to_code.get("HREF")
    )


def p_snp_img_quad(p):
    """snp_img_quad : empty"""
    img_str = p[-1]
    cte_s = memory.get_or_set_addr_const(img_str, "str")
    quad_helper.add_quad(token_to_code.get("eval"), -1, cte_s, token_to_code.get("SRC"))


def p_snp_close_html_tag(p):
    """snp_close_html_tag : empty"""
    html_tag = quad_helper.pop_tag()
    closing_tag = html_tag + 1
    # Checks that the respective html_tag has a closing tag
    # for example: img doesn't have one, but h1 yes (<h1></h1>)
    if html_tag is not token_to_code.get("IMG"):
        quad_helper.add_quad(token_to_code.get("eval"), -1, -1, closing_tag)


def p_snp_br_html_tag(p):
    """snp_br_html_tag : empty"""
    html_tag = p[-1].upper()
    # For debbuging
    # print("Html tag: ", html_tag)

    quad_helper.add_quad(token_to_code.get("eval"), -1, -1, token_to_code.get(html_tag))


def p_snp_push_eval_pending_token(p):
    """snp_push_eval_pending_token : empty"""
    quad_helper.push_token("eval")
    # For debbuging
    # print("Top token: ", quad_helper.top_token())


import ply.yacc as yacc

parser = yacc.yacc()
