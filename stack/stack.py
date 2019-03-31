#!/usr/bin/python3
from quadruple.quadruple import Quadruple


class Stack(object):
    def __init__(self):
        self.stack = []

    def empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def top(self):
        return self.stack[len(self.stack) - 1]

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        top = self.top()
        self.stack.pop()
        return top
