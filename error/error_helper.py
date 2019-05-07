#!/usr/bin/python3
from error.error import Error

# Errors
unknwon_error = "Unkown Error. "
type_mismatch = "No baila"
syntax_error = "Syntax error:"
var_not_defined = "Var"
module_not_defined = "Module"
wrong_params_num = "Wrong number of params"
zero_division = "ZeroDivisionError: division by zero"
index_out_of_range = "Index Out Of Range"
invalid_index = "Slice's CTEI index not valid."

error_to_code = {
    # Unkown 0
    unknwon_error: 0,
    # Lexer 100
    # Sintax 200
    syntax_error: 201,
    index_out_of_range: 202,
    # Semantic 300
    type_mismatch: 301,
    var_not_defined: 302,
    module_not_defined: 303,
    wrong_params_num: 304,
    invalid_index: 305,
    # Runtime errors 400
    zero_division: 401,
}

code_to_error = {
    # Unkown 0
    0: unknwon_error,
    # Lexer 100
    # Syntax 200
    201: syntax_error,
    202: index_out_of_range,
    # Semantic 300
    301: type_mismatch,
    302: var_not_defined,
    303: module_not_defined,
    304: wrong_params_num,
    305: invalid_index,
    # Runtime errors 400
    401: zero_division,
}


class ErrorHelper(object):
    def __init__(self):
        self.queue_error = []  # Stores all errors found and prints them in the end
        self.error_cont = 0  # Error count (useful for tests)

    def add_error(self, code, custom_message=""):
        """
            Description: Adds an error message into the queue_error, that will
            Params:
                code (int): The code of the error code that will be triggered
                custom_message (str): The extra message that will be added. Optional param.
            Return:
        """
        error = Error(code, custom_message)
        self.queue_error.append(error)
        self.error_cont = self.error_cont + 1

    def print_errors(self):
        """
            Description: Prints all error messages found (if any). Called when parser is done attempting to compile.
            Params:
            Return:
        """
        for error in self.queue_error:
            error_message = code_to_error.get(error.code)

            print(f"Error code: {error.code} -> {error_message} {error.custom_message}")

    def reset(self):
        self.__init__()
