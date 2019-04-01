class Quadruple(object):
    def __init__(self, token, operand1, operand2, operand3):
        self.token = token
        self.operand1 = operand1
        self.operand2 = operand2
        self.operand3 = operand3

    def __str__(self):
        # print (type(self.token), type(self.operand1), type(self.operand2), type(self.operand3))
        return "%d %s %s %s" % (self.token, self.operand1, self.operand2, self.operand3)

    def is_quadruple(self):
        my_int = 666
        a = type(self.token) == type(my_int)
        b = type(self.operand1) == type(my_int)
        c = type(self.operand2) == type(my_int)
        d = type(self.operand3) == type(my_int)

        if a and b and c and d:
            return True
        return False
