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
    # TODO - assign good name
    "eval": 301,
    # TODO - assign good name
    "GOTO": 401,
    "GOTOF": 402,
    "GOTOT": 403,
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
    # TODO - assign good name
    301: "eval",
    # TODO - assign good name
    401: "GOTO",
    402: "GOTOF",
    403: "GOTOT",
}

type_to_code = {
    "bool": 1,
    "char": 2,
    "class": 3,
    "double": 4,
    "error": 5,
    "int": 6,
    "object": 7,
    "void": 8,
}

code_to_type = {
    1: "bool",
    2: "char",
    3: "class",
    4: "double",
    5: "error",
    6: "int",
    7: "object",
    8: "void",
}