#!/usr/bin/python3
from error.error import Error

# Errors
unknwon_error = "Unkown"
type_mismatch = "No baila"
syntax_error = "Sintax error:"
var_not_defined = "Var"

error_to_code = {
    # Unkown 0
    unknwon_error: 0,
    # Lexer 100
    # Sintax 200
    syntax_error: 201,
    # Semantic 300
    type_mismatch: 301,
    var_not_defined: 302,
}

code_to_error = {
    # Unkown 0
    0: unknwon_error,
    # Lexer 100
    # Sintax 200
    201: syntax_error,
    # Semantic 300
    301 : type_mismatch,
    302 :var_not_defined,
}


class ErrorHelper(object):
    def __init__(self):
        self.queue_error = []
        self.error_cont = 0

    def add_error(self, code, custom_message=""):
        error = Error(code, custom_message)
        self.queue_error.append(error)
        self.error_cont = self.error_cont + 1

    def print_errors(self):
        for error in self.queue_error:
            error_message = code_to_error.get(error.code)

            print(f"Error code: {error.code} -> {error_message} {error.custom_message}")

    def reset(self):
        self.__init__()
