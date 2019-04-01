import unittest  # Reference: https://docs.python.org/2/library/unittest.html
from parser.parser import parser, yacc, procedure_directory, quad_helper, error_helper

TESTING_PREFIX = "our_tests/"


# def __eq__(self, other):
#     """Overrides the default implementation"""
#     if isinstance(other, Number):
#         return self.number == other.number
#     return False


def aux_tl_file(file_name, expected_number_of_errors):
    try:
        f = open(file_name, "r")
        data = f.read()
        f.close()
        yacc.parse(data, tracking=True)
        number_of_errors = error_helper.error_cont
        error_helper.reset()
        return number_of_errors
    except EOFError:
        print("EOFError")


class OurTestCase(unittest.TestCase):

    def test_0_0_pass_estatutos_secuenciales(self):
        file_name = TESTING_PREFIX + "0_0_pass_estatutos_secuenciales.tl"
        expected_errors = 0
        result = aux_tl_file(file_name, expected_errors)
        print(f"\nTESTING: {file_name}\n")
        self.assertEqual(result, expected_errors)

    def test_0_1_pass_estatutos_secuenciales(self):
        file_name = TESTING_PREFIX + "0_1_pass_estatutos_secuenciales.tl"
        expected_errors = 0
        result = aux_tl_file(file_name, expected_errors)
        print(f"\nTESTING: {file_name}\n")
        self.assertEqual(result, expected_errors)

    def test_1_0_fail_estatutos_secuenciales(self):
        file_name = TESTING_PREFIX + "1_0_fail_estatutos_secuenciales.tl"
        expected_errors = 1
        result = aux_tl_file(file_name, expected_errors)
        print(f"\nTESTING: {file_name}\n")
        self.assertEqual(result, expected_errors)

    def test_2_0_pass_estatutos_secuenciales(self):
        file_name = TESTING_PREFIX + "2_0_pass_estatutos_secuenciales.tl"
        expected_errors = 0
        result = aux_tl_file(file_name, expected_errors)
        print(f"\nTESTING: {file_name}\n")
        self.assertEqual(result, expected_errors)
