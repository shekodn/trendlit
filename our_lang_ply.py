# TOKENS
reserved_words = {
    # reserved words code
    "program": "PROGRAM",
    "script": "SCRIPT",

    # Data types
    "str": "STR",
    "int": "INT",
    "double": "DOUBLE",
    # "char": "CHAR",
    "bool": "BOOL",
    
    "if": "IF",
    "else": "ELSE",
    "loop": "LOOP",
    "True": "TRUE",
    "False": "FALSE",
    "eval": "EVAL",
    "def": "DEF",
    "spit": "SPIT",
    "suck_csv": "SUCK_CSV",
    "sort_slice": "SORT_SLICE",
    "sort_2D_slice": "SORT_2D_SLICE",
    "median": "MEDIAN",
    "mode": "MODE",
    "avg": "AVG",
    "pow": "POW",
    # reserved words html
    "h1": "H1",
    "h2": "H2",
    "div": "DIV",
    "p": "P",
    "class": "CLASS",
    "table": "TABLE",
    "tr": "TR",
    "th": "TH",
    "embed": "EMBED",
}

tokens = list(reserved_words.values()) + [
    "SIGN",
    "OP",
    "REL",
    "ASSOCIATIVE",
    "EQ",
    "COMMA",
    "COLON",
    "OPAREN",
    "CPAREN",
    "OBRACE",
    "CBRACE",
    "OBRACK",
    "CBRACK",
    "OEVALSCRIPT",
    "CEVALSCRIPT",
    # "CTECHAR",
    "CTESTR",
    "ID",
    "CTEI",
    "CTED",
]

t_SIGN = r"\+|-"
t_OP = r"\*|/"
t_REL = r"is|not|>|<|>=|<="
t_ASSOCIATIVE = r"or|and"
t_EQ = r"="
t_COMMA = r","
t_COLON = r":"
t_OPAREN = r"\("
t_CPAREN = r"\)"
t_OBRACE = r"{"
t_CBRACE = r"}"
t_OBRACK = r"\["
t_CBRACK = r"\]"
# t_CTECHAR = r"'.?'"


def t_OEVALSCRIPT(t):
    r"<\^"
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


def p_program1(p):
    """program1 : script program2
        | program2"""


def p_program2(p):
    """program2 : htmltag program2
        | empty"""


def p_script(p):
    """script : SCRIPT block"""


def p_block(p):
    """block : OBRACE block1 CBRACE"""


def p_block1(p):
    """block1 : statement block1
        | empty"""


def p_declaration(p):
    """declaration : type ID"""


def p_type(p):
    """type : STR
        | INT
        | DOUBLE
        | BOOL"""


def p_statement(p):
    """statement : declaration
        | assignment
        | condition
        | cycle
        | call
        | module
        | writing"""


def p_assignment(p):
    """assignment : type assignment1
        | assignment1"""


def p_assignment1(p):
    """assignment1 : ID EQ expression"""


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
        | CTEI
        | CTED
        | CTESTR
        | FALSE
        | TRUE"""


def p_condition(p):
    """condition : IF OPAREN expression CPAREN block condition1"""


def p_condition1(p):
    """condition1 : ELSE OPAREN expression CPAREN block
        | empty"""


def p_cycle(p):
    """cycle : LOOP OPAREN expression CPAREN block"""


def p_module(p):
    """module : DEF ID OPAREN arguments CPAREN COLON module1"""


def p_module1(p):
    """module1 : OBRACE module3 CBRACE
        | type OBRACE module2 CBRACE"""


def p_module2(p):
    """module2 : statement module2
        | empty"""


def p_module3(p):
    """module3 : statement module3
        | SPIT expression"""


def p_call(p):
    """call : ID call1
        | predef call1"""


def p_call1(p):
    """call1 : OPAREN expression CPAREN"""


def p_predef(p):
    """predef : SUCK_CSV
        | SORT_SLICE
        | SORT_2D_SLICE
        | MEDIAN
        | MODE
        | AVG
        | POW"""


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
