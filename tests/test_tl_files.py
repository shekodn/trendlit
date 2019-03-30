import unittest  # Reference: https://docs.python.org/2/library/unittest.html
from parser.parser import parser, yacc, procedure_directory, quad_helper, error_helper

TESTING_PREFIX = "tests/tl_test_files/"


def aux_tl_file(file_name, expected_number_of_errors):
    try:
        f = open(file_name, "r")
        data = f.read()
        f.close()
        yacc.parse(data, tracking=True)
        return error_helper.error_cont
    except EOFError:
        print("EOFError")


class OurTestCase(unittest.TestCase):
    def test_tl_file_estatutos_secuenciales_0(self):
        file_name = TESTING_PREFIX + "estatutos_secuenciales_0.tl"
        expected_errors = 0
        result = aux_tl_file(file_name, expected_errors)
        print(f"\nTESTING: {file_name}\n")
        self.assertEqual(result, expected_errors)

    def test_tl_file_fail_estatutos_secuenciales_1(self):
        file_name = TESTING_PREFIX + "fail_estatutos_secuenciales_1.tl"
        expected_errors = 1
        result = aux_tl_file(file_name, expected_errors)
        print(f"\nTESTING: {file_name}\n")
        self.assertEqual(result, expected_errors)
