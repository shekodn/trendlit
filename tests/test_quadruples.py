import unittest  # Reference: https://docs.python.org/2/library/unittest.html
from quadruple.quadruple import Quadruple

TESTING_PREFIX = "tests/tl_test_quadruples/"


def aux_tl_file(file_name, name_of_test):
    try:
        f = open(file_name, "r")
        data = f.read()
        f.close()
        yacc.parse(data, tracking=True)
        if error_helper.error_cont is 0:
            quad_helper.print_to_file(name_of_test + ".obj")
            return True
        else:
            return False
    except EOFError:
        print("EOFError")


class QuadruplesTestCase(unittest.TestCase):
    def test_quadruple_1(self):

        """
        IN:
        A * B + C

        OUT:
        * A B t1
        + t1 C t2
        """
        # quad = Quadruple()
        # operation = quad.token
        # operan1 = quad.operand1
        # operand2 = quad.operand2
        # result = quad.operand3

        # file_name =
        # name_of_test =
        # result = aux_tl_file()

        self.assertEqual(True, True)
