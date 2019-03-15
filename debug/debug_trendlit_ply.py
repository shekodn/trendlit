# TOKENS
reserved_words = {
    # reserved words code
    "max": "MAX",
    "min": "MIN",
    "program": "PROGRAM",
    "script": "SCRIPT",
    # Data types
    "False": "FALSE",
    "True": "TRUE",
    "bool": "BOOL",
    "double": "DOUBLE",
    "else": "ELSE",
    "if": "IF",
    "int": "INT",
    "loop": "LOOP",
    "str": "STR",
    # Functions
    "def": "DEF",
    "eval": "EVAL",
    "spit": "SPIT",
    # Special Functions
    "avg": "AVG",
    "find_max": "FIND_MAX",
    "find_min": "FIND_MIN",
    "median_1Dslice": "MEDIAN",
    "mode_1Dslice": "MODE",
    "multiply_1Dslice": "MULTIPLY_1DSLICE",
    "pow": "POW",
    "randoms": "RANDOMS",
    "sort_slice": "SORT_SLICE",
    "suck_csv": "SUCK_CSV",
    "zeros": "ZEROS",
    # reserved words html
    "class": "CLASS",
    "div": "DIV",
    "embed": "EMBED",
    "h1": "H1",
    "h2": "H2",
    "p": "P",
    "table": "TABLE",
    "th": "TH",
    "tr": "TR",
}

tokens = list(reserved_words.values()) + [
    "ASSOCIATIVE",
    "CBRACE",
    "CBRACK",
    "CEVALSCRIPT",
    "COLON",
    "COMMA",
    "CPAREN",
    "CTED",
    "CTEI",
    "CTESTR",
    "EQ",
    "ID",
    "OBRACE",
    "OBRACK",
    "OEVALSCRIPT",
    "OP",
    "OPAREN",
    "REL",
    "SIGN",
]

t_SIGN = r"\+|-"
t_OP = r"\*|/"
t_ASSOCIATIVE = r"or|and"
t_EQ = r"="
t_COMMA = r","
t_COLON = r":"
t_OPAREN = r"\("
t_CPAREN = r"\)"
t_OBRACE = r"\{"
t_CBRACE = r"\}"
t_OBRACK = r"\["
t_CBRACK = r"\]"


def t_OEVALSCRIPT(t):
    r"<\^"
    return t


def t_REL(t):
    r"is|not|>=|<=|>|<"
    return t


def t_CEVALSCRIPT(t):
    r"\^>"
    return t


def t_ID(t):
    r"[A-Za-z_][A-Za-z0-9_]*"
    t.type = reserved_words.get(t.value, "ID")
    return t


def t_CTED(t):
    r"(-?[0-9]+[.])[0-9]+"
    return t


def t_CTEI(t):
    r"-?[0-9]+"
    return t


def t_CTESTR(t):
    r"\"[^\"]*\""
    return t


# Ignored
t_ignore = " \t"


def t_newline(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Discarded tokens
# Reference: https://www.dabeaz.com/ply/ply.html#ply_nn8
def t_COMMENT(t):
    r"\#.*"
    pass
    # No return value. Token discarded


# Build the lexer
import ply.lex as lex

lex.lex()


def p_program(p):
    """program : PROGRAM ID program1"""
    print("it compiles !")
    print("p_program")


def p_program1(p):
    """program1 : script program2
        | program2"""
    print("p_program1")


def p_program2(p):
    """program2 : htmltag program2
        | empty"""
    print("p_program2")


def p_script(p):
    """script : SCRIPT block"""

    print("p_script")


def p_block(p):
    """block : OBRACE declareBlock block1 CBRACE"""

    print("p_block")


def p_block1(p):
    """block1 : statement block1
        | empty"""
    print("p_block1")


def p_simpleBlock(p):
    """simpleBlock : OBRACE simpleBlock1 CBRACE"""

    print("p_simpleBlock")


def p_simpleBlock1(p):
    """simpleBlock1 : statement simpleBlock1
        | empty"""
    print("p_simpleBlock1")


def p_declareBlock(p):
    """declareBlock : declare declareBlock
        | empty"""
    print("p_declareBlock")


def p_declare(p):
    """declare : type ID
        | type ID initializeSlices
        | initialize"""
    print("p_declare")


def p_initialize(p):
    """initialize : type initialize1 initialize2"""

    print("p_initialize")


def p_initialize1(p):
    """initialize1 : ID EQ value
        | ID initializeSlices EQ constSlices"""
    print("p_initialize1")


def p_initialize2(p):
    """initialize2 : COMMA initialize1 initialize2
        | empty"""
    print("p_initialize2")


def p_initializeSlices(p):
    """initializeSlices : initializeSlices1D
        | initializeSlices2D"""
    print("p_initializeSlices")


def p_initializeSlices1D(p):
    """initializeSlices1D : OBRACK CTEI CBRACK"""

    print("p_initializeSlices1D")


def p_initializeSlices2D(p):
    """initializeSlices2D : OBRACK CTEI CBRACK OBRACK CTEI CBRACK"""

    print("p_initializeSlices2D")


def p_constSlices(p):
    """constSlices : constSlice1D
        | constSlice2D"""
    print("p_constSlices")


def p_constSlice1D(p):
    """constSlice1D : OBRACK value constSlice1D1 CBRACK"""

    print("p_constSlice1D")


def p_constSlice1D1(p):
    """constSlice1D1 : COMMA value constSlice1D1
        | empty"""
    print("p_constSlice1D1")


# TODO: FIX 2D SLICE
def p_constSlice2D(p):
    """constSlice2D : OBRACK constSlice1D COMMA CBRACK
        | OBRACK constSlice1D CBRACK"""
    print("p_constSlice2D")


def p_type(p):
    """type : STR
        | INT
        | DOUBLE
        | BOOL"""
    print("p_type")


def p_statement(p):
    """statement : assignment
        | condition
        | cycle
        | call
        | module
        | writing"""
    print("p_statement")


def p_assignment(p):
    """assignment : ID assignmentSlice EQ expression"""

    print("p_assignment")


def p_assignmentSlice(p):
    """assignmentSlice : assignmentSlice1D
        | assignmentSlice2D
        | empty"""
    print("p_assignmentSlice")


def p_assignmentSlice1D(p):
    """assignmentSlice1D : OBRACK expression CBRACK"""

    print("p_assignmentSlice1D")


def p_assignmentSlice2D(p):
    """assignmentSlice2D : OBRACK expression CBRACK OBRACK expression CBRACK"""

    print("p_assignmentSlice2D")


def p_expression(p):
    """expression : exp expression1"""

    print("p_expression")


def p_expression1(p):
    """expression1 : REL exp
        | ASSOCIATIVE exp
        | empty"""
    print("p_expression1")


def p_exp(p):
    """exp : term exp1"""

    print("p_exp")


def p_exp1(p):
    """exp1 : SIGN exp exp1
        | empty"""
    print("p_exp1")


def p_term(p):
    """term : factor term1"""

    print("p_term")


def p_term1(p):
    """term1 : OP term term1
        | empty"""
    print("p_term1")


def p_factor(p):
    """factor : OPAREN expression CPAREN
        | factor1"""
    print("p_factor")


def p_factor1(p):
    """factor1 : value
        | SIGN value"""
    print("p_factor1")


def p_value(p):
    """value : ID
        | valueSlice
        | call
        | CTEI
        | CTED
        | CTESTR
        | FALSE
        | TRUE"""
    print("p_value")


def p_valueSlice(p):
    """valueSlice : valueSlice1D
        | valueSlice2D"""
    print("p_valueSlice")


def p_valueSlice1D(p):
    """valueSlice1D : ID OBRACK expression CBRACK"""

    print("p_valueSlice1D")


def p_valueSlice2D(p):
    """valueSlice2D : ID OBRACK expression CBRACK OBRACK expression CBRACK"""

    print("p_valueSlice2D")


def p_condition(p):
    """condition : IF OPAREN expression CPAREN simpleBlock condition1"""

    print("p_condition")


def p_condition1(p):
    """condition1 : ELSE simpleBlock
        | empty"""
    print("p_condition1")


def p_cycle(p):
    """cycle : LOOP OPAREN expression CPAREN simpleBlock"""

    print("p_cycle")


def p_module(p):
    """module : DEF ID OPAREN arguments CPAREN module1"""

    print("p_module")


def p_module1(p):
    """module1 : block
        | COLON type OBRACE declareBlock module2 CBRACE"""
    print("p_module1")


def p_module2(p):
    """module2 : statement module2
        | SPIT expression"""
    print("p_module2")


def p_call(p):
    """call : ID call1
        | predef"""
    print("p_call")


def p_call1(p):
    """call1 : OPAREN params CPAREN"""

    print("p_call1")


def p_params(p):
    """params : expression params1"""

    print("p_params")


def p_params1(p):
    """params1 : COMMA params
        | empty"""
    print("p_params1")


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
    print("p_predef")


def p_predef_avg(p):
    """predef_avg : AVG OPAREN ID CPAREN"""

    print("p_predef_avg")


def p_predef_find_max(p):
    """predef_find_max : FIND_MAX OPAREN ID COMMA predef_find_max_args CPAREN"""

    print("p_predef_find_max")


def p_predef_find_max_args(p):
    """predef_find_max_args : ID
        | CTEI"""
    print("p_predef_find_max_args")


def p_predef_find_min(p):
    """predef_find_min : FIND_MIN OPAREN ID COMMA predef_find_min_args CPAREN"""

    print("p_predef_find_min")


def p_predef_find_min_args(p):
    """predef_find_min_args : ID
        | CTEI"""
    print("p_predef_find_min_args")


def p_predef_find_mult_slice(p):
    """predef_find_mult_slice : MULTIPLY_1DSLICE OPAREN ID COMMA predef_find_mult_slice_args CPAREN"""

    print("p_predef_find_mult_slice")


def p_predef_find_mult_slice_args(p):
    """predef_find_mult_slice_args : ID
        | CTEI"""
    print("p_predef_find_mult_slice_args")


def p_predef_median(p):
    """predef_median : MEDIAN OPAREN ID CPAREN"""

    print("p_predef_median")


def p_predef_mode(p):
    """predef_mode : MODE OPAREN ID CPAREN"""

    print("p_predef_mode")


def p_predef_pow(p):
    """predef_pow : POW OPAREN predef_pow_args COMMA predef_pow_args CPAREN"""

    print("p_predef_pow")


def p_predef_pow_args(p):
    """predef_pow_args : ID
        | CTEI"""
    print("p_predef_pow_args")


def p_predef_randoms(p):
    """predef_randoms : RANDOMS OPAREN predef_randoms_args CPAREN"""

    print("p_predef_randoms")


def p_predef_randoms_args(p):
    """predef_randoms_args : ID
        | CTEI"""
    print("p_predef_randoms_args")


def p_predef_zeros(p):
    """predef_zeros : ZEROS OPAREN predef_zeros_args CPAREN"""

    print("p_predef_zeros")


def p_predef_zeros_args(p):
    """predef_zeros_args : ID
        | CTEI"""
    print("p_predef_zeros_args")


def p_predef_sort_slice(p):
    """predef_sort_slice : SORT_SLICE OPAREN ID COMMA predef_sort_slice_option CPAREN"""

    print("p_predef_sort_slice")


def p_predef_sort_slice_option(p):
    """predef_sort_slice_option : MAX
        | MIN"""
    print("p_predef_sort_slice_option")


def p_predef_suck_csv(p):
    """predef_suck_csv : SUCK_CSV OPAREN predef_suck_csv_args CPAREN"""

    print("p_predef_suck_csv")


def p_predef_suck_csv_args(p):
    """predef_suck_csv_args : ID
        | CTESTR"""
    print("p_predef_suck_csv_args")


def p_writing(p):
    """writing : EVAL OPAREN expression CPAREN"""

    print("p_writing")


def p_arguments(p):
    """arguments : type ID arguments1
        | empty"""
    print("p_arguments")


def p_arguments1(p):
    """arguments1 : COMMA type ID arguments1
        | empty"""
    print("p_arguments1")


def p_htmltag(p):
    """htmltag : tag OBRACE class htmltag1 CBRACE"""

    print("p_htmltag")


def p_htmltag1(p):
    """htmltag1 : CTESTR htmltag1
        | htmlscript htmltag1
        | htmltag htmltag1
        | empty"""
    print("p_htmltag1")


def p_tag(p):
    """tag : H1
        | H2
        | DIV
        | P
        | TABLE
        | TR
        | TH"""
    print("p_tag")


def p_class(p):
    """class : CLASS COLON CTESTR
        | empty"""
    print("p_class")


def p_htmlscript(p):
    """htmlscript : OEVALSCRIPT expression CEVALSCRIPT
        | embedscript"""
    print("p_htmlscript")


# TODO : FIX THIS!!!
def p_embedscript(p):
    """embedscript : EMBED ID block"""
    # """embedscript : EMBED ID OBRACE eblock CBRACE"""
    print("p_embedscript")


def p_empty(p):
    """empty :"""

    print("p_empty")


def p_error(p):
    print("Syntax error at '%s'" % p)

    print("p_error")


import ply.yacc as yacc

yacc.yacc()

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file = sys.argv[1]
        try:
            f = open(file, "r")
            data = f.read()
            f.close()
            yacc.parse(data, tracking=True)
        except EOFError:
            print("EOFError")
    else:
        print("File missing")
