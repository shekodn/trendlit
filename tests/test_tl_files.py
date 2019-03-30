import unittest  # Reference: https://docs.python.org/2/library/unittest.html
from parser.parser import parser, yacc, procedure_directory, quad_helper, error_helper
TESTING_PREFIX = "tests/tl_test_files/"

def aux_tl_file(file_name, expected_number_of_errors):
    try:
        f = open(file_name, "r")
        real_number_of_errors = 0
        data = f.read()
        f.close()
        yacc.parse(data, tracking=True)
        if (expected_number_of_errors is error_helper.error_cont):
            return True
        else:
            return False
        return real_number_of_errors

    except EOFError:
        print("EOFError")

class OurTestCase(unittest.TestCase):
    def test_tl_file_estatutos_secuenciales_0(self):
        file_name = TESTING_PREFIX + "estatutos_secuenciales_0.tl"
        expected_errors = 0
        result =  aux_tl_file(file_name, expected_errors)
        print(f"\nTESTING: {file_name}\n")
        self.assertEqual(result, True)
