#!/usr/bin/python3

from quadruple.quadruple import Quadruple
from stack.stack import Stack
from semantic_cube.semantic_cube_helper import (
    token_to_code,
    code_to_token,
    type_to_code,
)


class QuadrupleHelper(object):
    def __init__(self):
        self.stack_tokens = Stack()
        self.stack_operands = Stack()
        self.stack_tags = Stack()
        self.stack_types = Stack()
        self.stack_jumps = Stack()
        self.stack_dimensions = Stack()
        self.stack_tokens.push(999)
        self.stack_operands.push(999)
        self.stack_types.push(999)
        self.stack_jumps.push(999)
        self.stack_tags.push(999)
        self.stack_dimensions.push(999)
        self.queue_quad = []
        self.quad_cont = 0
        self.temp_cont = 10001

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
        self.stack_types.push(type_to_code.get(type))

    def pop_type(self):
        return self.stack_types.pop()

    def top_type(self):
        return self.stack_types.top()

    def push_jump(self, jump):
        self.stack_jumps.push(jump)

    def pop_jump(self):
        return self.stack_jumps.pop()

    def top_jump(self):
        return self.stack_jumps.top()

    def push_tag(self, tag):
        self.stack_tags.push(tag)

    def pop_tag(self):
        return self.stack_tags.pop()

    def top_tag(self):
        return self.stack_tags.top()

    def push_dimension(self, id, dimension):
        self.stack_dimensions.push(id, dimension)

    def pop_dimension(self):
        return self.stack_dimensions.pop()

    def top_dimension(self):
        return self.stack_dimensions.top()

    def fill(self, quadruple_index, value):
        self.queue_quad[quadruple_index].operand3 = value

    def reset(self):
        self.__init__()

    def print_to_file(self, file_name):
        """
        Description: Generates .obj file
        """
        file = open(file_name, "w")
        cont = 0  # for debugging purposes.
        for quad in self.queue_quad:
            file.write(str(quad))
            file.write("\n")
            # TODO: Every quad should be an INT bc it is a memory address
            # Print for debugging.
            # print(type(code_to_token.get(quad.token)), code_to_token.get(quad.token))
            # print(type(quad.operand1), quad.operand1)
            # print(type(quad.operand2), quad.operand2)
            # print(type(quad.operand3), quad.operand3)
            # # Uncomment for debbuging
            print(
                "%s %s, %s, %s, %s"
                % (
                    cont,
                    code_to_token.get(quad.token),
                    quad.operand1,
                    quad.operand2,
                    quad.operand3,
                )
            )
            cont = cont + 1
        file.close()
