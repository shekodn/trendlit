# TOKENS
reserved_words_code = {
    "program": "PROGRAM",
    "script": "SCRIPT",
    "str": "STR",
    "int": "INT",
    "double": "DOUBLE",
    "char": "CHAR",
    "bool": "BOOL",
    "if": "IF",
    "else": "ELSE",
    "loop": "LOOP",
    "is": "IS",
    "not": "NOT",
    "or": "OR",
    "and": "AND",
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
    # }
    #
    # reserved_words_html = {
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

tokens = list(reserved_words_code.values()) + [
    "SIGN",
    "OP",
    "REL",
    "ASSOCIATIVE",
    "EQ",
    "COMMA",
    "SEMI",
    "COLON",
    "OPAREN",
    "CPAREN",
    "OBRACE",
    "CBRACE",
    "OBRACK",
    "CBRACK",
    "OEVALSCRIPT",
    "CEVALSCRIPT",
    "STRING",
    "ID",
    "I",
    "D",
]

t_SIGN = r"\+|-"
t_OP = r"\*|/"
t_REL = r"is|not|>|<|>=|<="
t_ASSOCIATIVE = r"or|and"
t_EQ = r"="
t_COMMA = r","
t_SEMI = r";"
t_COLON = r":"
t_OPAREN = r"\("
t_CPAREN = r"\)"
t_OBRACE = r"{"
t_CBRACE = r"}"
t_OBRACK = r"\["
t_CBRACK = r"\]"
t_OEVALSCRIPT = r"<^"
t_CEVALSCRIPT = r"^>"
t_STRING = r"\"[^\"]*\""


def t_ID(t):
    r"[A-Za-z_][A-Za-z0-9_]*"
    return t


def t_D(t):
    r"(-?[0-9]+[.])[0-9]+"
    return t


def t_I(t):
    r"-?[0-9]+"
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


def p_(p):
    """program : PROGRAM ID program1"""


def p_(p):
    """program1 : script
        | html
        | empty"""


def p_(p):
    """script : SCRIPT block"""


def p_(p):
    """block : OBRACE block1 CBRACE"""


def p_(p):
    """block1 : statement block1
        | empty"""


def p_(p):
    """declaration : type ID"""


def p_(p):
    """type : STR
        | INT
        | DOUBLE
        | CHAR
        | BOOL"""


def p_(p):
    """statement : declaration
        | assignment
        | condition
        | cycle
        | call
        | module
        | writing"""


def p_(p):
    """assignment : type assignment1
        | assignment1"""


def p_(p):
    """assignment1 : ID EQ expression"""


def p_(p):
    """expression : exp expression1"""


def p_(p):
    """expression1 : REL exp
        | ASSOCIATIVE exp
        | empty"""


def p_(p):
    """exp : term exp1"""


def p_(p):
    """exp1 : SIGN exp exp1
        | empty"""


def p_(p):
    """term : factor term1"""


def p_(p):
    """term1 : OP term term1
        | empty"""


def p_(p):
    """factor : OPAREN expresion CPAREN
        | factor1"""


def p_(p):
    """factor1 : value
        | SIGN value"""


def p_(p):
    """value : ID
        | I
        | D
        | STRING
        | FALSE
        | TRUE"""


def p_(p):
    """condition : IF OPAREN expression CPAREN block condition1"""


def p_(p):
    """condition1 : ELSE OPAREN expression CPAREN block
        | empty"""


def p_(p):
    """cycle : LOOP OPAREN expression CPAREN block"""


def p_(p):
    """module : DEF ID OPAREN arguments CPAREN COLON spitval block"""


def p_(p):
    """call : ID OPAREN expresion CPAREN"""


def p_(p):
    """writing : EVAL OPAREN expresion CPAREN"""


def p_(p):
    """arguments : STR ID
        | INT ID
        | DOUBLE ID
        | CHAR ID
        | BOOL ID
        | empty"""


def p_(p):
    """spitval : STR
        | INT
        | DOUBLE
        | CHAR
        | BOOL
        | empty"""


def p_(p):
    """html : htmltag
        | empty"""


def p_(p):
    """htmltag : tag OBRACE class htmltag1 CBRACE"""


def p_(p):
    """htmltag1 : text htmltag1
        | htmlscript htmltag1
        | htmltag htmltag1
        | empty"""


def p_(p):
    """tag : H1
        | H2
        | DIV
        | P
        | TABLE
        | TR
        | TH"""


def p_(p):
    """text : STRING
        | empty"""


def p_(p):
    """class : CLASS COLON STRING
        | empty"""


def p_(p):
    """htmlscript : OEVALSCRIPT expression CEVALSCRIPT
        | embedscript"""


def p_(p):
    """embedscript : EMBED ID OBRACE eblock CBRACE"""


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
