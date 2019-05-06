#!/usr/bin/python3

# --------------------- LEX ---------------------------

# TOKENS
reserved_words = {
    # reserved words code
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
    "do": "DO",
    "loop": "LOOP",
    "str": "STR",
    # Functions
    "def": "DEF",
    "eval": "EVAL",
    "spit": "SPIT",
    # reserved words html tags
    "class": "CLASS",
    "div": "DIV",
    "href": "HREF",
    "link": "LINK",
    "img": "IMG",
    "src": "SRC",
    "head": "HEAD",
    # Headers
    "h1": "H1",
    "h2": "H2",
    "h3": "H3",
    "h4": "H4",
    "h5": "H5",
    "h6": "H6",
    "p": "P",
    # Tables
    "table": "TABLE",
    "th": "TH",
    "tr": "TR",
    "thead": "THEAD",
    "td": "TD",
    "tbody": "TBODY",
    # Others
    "br": "BR",
    "span": "SPAN",
    # Lists
    "ol": "OL",
    "ul": "UL",
    "li": "LI",
}

tokens = list(reserved_words.values()) + [
    "ASSOCIATIVE",
    "CBRACE",
    "CBRACK",
    "CCODEHTML",
    "CEVALSCRIPT",
    "COLON",
    "COMMA",
    "CPAREN",
    "CTED",
    "CTEI",
    "CTESTR",
    "HTMLENDDO",
    "EQ",
    "HTMLELSE",
    "HTMLEND",
    "ID",
    "INITCODEHTML",
    "OBRACE",
    "OBRACK",
    "OEVALSCRIPT",
    "OP",
    "OPAREN",
    "REL",
    "SIGN",
]

t_SIGN = r"\+|-"
t_OP = r"\*|/"  # * or /
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


def t_HTMLELSE(t):
    r"<%[ ]*else[ ]*%>"
    return t


def t_HTMLEND(t):
    r"<%[ ]*end[ ]*%>"
    return t


def t_HTMLENDDO(t):
    r"<%[ ]*endloop"
    return t


def t_INITCODEHTML(t):
    r"<%"
    return t


def t_CCODEHTML(t):
    r"%>"
    return t


def t_REL(t):
    r"is|not|>=|<=|>|<"
    return t


def t_ASSOCIATIVE(t):
    r"or|and"
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
    # print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Discarded tokens
# Reference: https://www.dabeaz.com/ply/ply.html#ply_nn8
def t_COMMENT(t):
    r"\#.*"
    pass
    # No return value. Token discarded


# Build the lexer
import ply.lex as lex

lexer = lex.lex()
