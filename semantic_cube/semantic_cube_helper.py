token_to_code = {
    # SIG and OP
    "+": 101,
    "-": 102,
    "*": 103,
    "/": 104,
    "=": 105,
    # See PLY's documentation
    "UMINUS": 106,
    # REL
    "is": 201,
    "not": 202,
    ">=": 203,
    "<=": 204,
    ">": 205,
    "<": 206,
    # LOGIC
    "and": 207,
    "or": 208,
    # TODO - assign good name
    "eval": 301,
    # TODO - assign good name
    "GOTO": 401,
    "GOTOF": 402,
    "GOTOT": 403,
    "GOSUB": 404,
    "ERA": 501,
    "PARAMETER": 502,
    "ENDPROC": 503,
    "RET": 504,
    "VER": 505,
    # Html
    "H1": 600,
    "/H1": 601,
    "H2": 602,
    "/H2": 603,
    "H3": 604,
    "/H3": 605,
    "H4": 606,
    "/H4": 607,
    "H5": 608,
    "/H5": 609,
    "H6": 610,
    "/H6": 611,
    "DIV": 612,
    "/DIV": 613,
    "P": 614,
    "/P": 615,
    "TABLE": 616,
    "/TABLE": 617,
    "TR": 618,
    "/TR": 619,
    "TH": 620,
    "/TH": 621,
    "BR": 622,
    "CLASS": 623,
    # Aux
    "false_bottom": 999,
    "(": 1001,
}


code_to_token = {
    # SIG and OP
    101: "+",
    102: "-",
    103: "*",
    104: "/",
    105: "=",
    # See PLY's documentation
    106: "UMINUS",
    # REL
    201: "is",
    202: "not",
    203: ">=",
    204: "<=",
    205: ">",
    206: "<",
    # LOGIC
    207: "and",
    208: "or",
    # TODO - assign good name
    301: "eval",
    # TODO - assign good name
    401: "GOTO",
    402: "GOTOF",
    403: "GOTOT",
    404: "GOSUB",
    501: "ERA",
    502: "PARAMETER",
    503: "ENDPROC",
    504: "RET",
    505: "VER",
    # Html
    600: "H1",
    601: "/H1",
    602: "H2",
    603: "/H2",
    604: "H3",
    605: "/H3",
    606: "H4",
    607: "/H4",
    608: "H5",
    609: "/H5",
    610: "H6",
    611: "/H6",
    612: "DIV",
    613: "/DIV",
    614: "P",
    615: "/P",
    616: "TABLE",
    617: "/TABLE",
    618: "TR",
    619: "/TR",
    620: "TH",
    621: "/TH",
    622: "BR",
    623: "CLASS",
    # Aux
    999: "false_bottom",
    1001: "(",
}

type_to_code = {"bool": 1, "str": 2, "double": 3, "error": 4, "int": 5, "void": 6}

code_to_type = {1: "bool", 2: "str", 3: "double", 4: "error", 5: "int", 6: "void"}

type_to_init_value = {"bool": "False", "str": '""', "double": "0.0", "int": "0"}

scope_to_code = {"global": 1, "local": 2}

code_to_scope = {1: "global", 2: "local"}
