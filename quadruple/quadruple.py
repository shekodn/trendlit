class Quadruple(object):
    def __init__(self, op, oper1, oper2, oper3):
        self.op = op
        self.oper1 = oper1
        self.oper2 = oper2
        self.oper3 = oper3

    def __str__(self):
        return "%d %d %d %d" % (self.op, self.oper1, self.oper2, self.oper3)

    def is_quadruple(self):
        my_int = 666
        a = type(self.op) == type(my_int)
        b = type(self.oper1) == type(my_int)
        c = type(self.oper2) == type(my_int)
        d = type(self.oper3) == type(my_int)

        if a and b and c and d:
            return True
        return False
