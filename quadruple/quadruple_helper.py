#!/usr/bin/python3

from quadruple import Quadruple

# import sys
# sys.path.append('../')
# print(sys.path)

from semantic_cube.semantic_cube_helper import code_to_token, token_to_code


# from stack.stack import Stack


# from stack.stack import Stack


class QuadrupleHelper(object):
    def __init__(self):
        self.stack_tokens = Stack()
        self.stack_operands = Stack()
        self.stack_types = Stack()
        self.stack_tokens.push(999)
        self.stack_operands.push(999)
        self.stack_types.push(999)
        self.queue_quad = []
        self.quad_cont = 0

    # token = Numeric code representation of an operator.
    # operand1 = Memory address of operand 1.
    # operand2 = Memory address of operand 2.
    # operand3 = Memory address of operand 3.
    def add_quad(self, token, operand1, operand2, operand3):
        new_quad = Quadruple(token, operand1, operand2, operand3)
        self.queue_quad.append(new_quad)
        self.quad_cont = self.quad_cont + 1

    def push_operand(self, operand):
        self.stack_operands.push(operand)

    def pop_operand(self):
        return self.stack_operands.pop()

    def top_operand(self):
        return self.stack_operands.top()

    def push_token(self, token):
        self.stack_tokens.push(token_to_code.get(token))

    def pop_token(self):
        return self.stack_tokens.pop()

    def top_token(self):
        return self.stack_tokens.top()

    def push_type(self, type):
        self.stack_types.push(type)

    def pop_type(self):
        return self.stack_types.pop()

    def top_type(self):
        return self.stack_types.top()

    def fill(self, quadruple_index, value):
        self.queue_quad[quadruple_index].operand3 = value

    def print_to_file(self, file_name):
        """
        Description: Generates .obj file
        """
        file = open(file_name, "w")
        cont = 0  # for debugging purposes.
        for quad in self.queue_quad:
            file.write(str(quad))
            file.write("\n")
            # Print for debugging.
            print(
                "%d) %s, %d, %s, %d"
                % (
                    cont,
                    codeToOper.get(quad.token),
                    quad.operand1,
                    quad.operand2,
                    quad.operand3,
                )
            )
            cont = cont + 1
        file.close()


# if __name__ == '__main__':
#     print("Quad")
