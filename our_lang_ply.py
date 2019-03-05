# TOKENS
reserved_words_code = {
    'program':'PROGRAM',
    'script':'SCRIPT',
    'str':'STR',
    'int':'INT',
    'double':'DOUBLE',
    'char':'CHAR',
    'bool':'BOOL',
    'if':'IF',
    'else':'ELSE',
    'loop':'LOOP',
    'is':'IS',
    'not':'NOT',
    'or':'OR',
    'and':'AND',
    'True':'TRUE',
    'False':'FALSE',
    'eval':'EVAL',
    'def':'DEF',
    'spit':'SPIT',
    'suck_csv':'SUCK_CSV',
    'sort_slice':'SORT_SLICE',
    'sort_2D_slice':'SORT_2D_SLICE'
    'median':'MEDIAN',
    'mode':'MODE',
    'avg':'AVG',
    'pow':'POW'
}

reserved_words_html = {
  'h1':'H1',
  'h2':'H2',
  'div':'DIV',
  'p':'P',
  'class':'CLASS'
  'table':'TABLE',
  'tr':'TR',
  'th':'TH',
  'embed':'EMBED'
}

tokens = list(reserved_words_code.values()) +
    list(reserved_words_html.values())[
    'SIGN','OP','REL','ASSOCIATIVE','EQ','COMMA',
    'SEMI','COLON','OPAREN','CPAREN','OBRACE',
    'CBRACE','OBRACK','CBRACK','OEVALSCRIPT',
    'CEVALSCRIPT','STRING','ID','I','D']

t_SIGN    = r'\+|-'
t_OP   = r'\*|/'
t_REL   = r'is|not|>|<|>=|<='
t_ASSOCIATIVE = r'or|and'
t_EQ  = r'='
t_COMMA  = r','
t_SEMI  = r';'
t_COLON  = r':'
t_OPAREN    = r'\('
t_CPAREN   = r'\)'
t_OBRACE   = r'{'
t_CBRACE   = r'}'
t_OBRACK   = r'['
t_CBRACK   = r']'
t_OEVALSCRIPT = r'<^'
t_CEVALSCRIPT = r'^>'
t_STRING   = r'\"[^\"]*\"'

def  t_ID(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    return t

def t_D(t):
    r'(-?[0-9]+[.])[0-9]+'
    return t

def t_I(t):
    r'-?[0-9]+'
    return t
