#!/usr/bin/python3
from error.error import Error

error_to_code = {
    # Lexer 100
    # Parser 200
    # Semantic 300
    "no baila" : 301
}

code_to_error = {
    # Lexer 100
    # Parser 200
    # Semantic 300
    301 : "no baila"
}


class ErrorHelper(object):
    def __init__(self):
        self.queue_error = []
        self.error_cont = 0

    def add_error(self, code):
        error = Error(code)
        self.queue_error.append(error)
        self.error_cont = self.error_cont + 1

    def print_errors(self):
        error_code = self.queue_error[0].code
        error_message = code_to_error.get(error_code) # TODO: convert to message using mapping
        print(error_message)

        # for error in self.queue_error:
        #     print(f"Code: {self.code}: {self.message}")
