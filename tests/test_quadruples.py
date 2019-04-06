import unittest  # Reference: https://docs.python.org/2/library/unittest.html
from quadruple.quadruple import Quadruple
import filecmp

OBJECT_CODE = "object_code/"
TESTING_CODE = "tests/tl_test_quadruples/"


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
    def test_quadruple_2_2_pass_estatutos_secuenciales_eval(self):

        file1_name = TESTING_CODE + "2_2_pass_estatutos_secuenciales_eval.tl.test"
        file2_name = OBJECT_CODE + "2_2_pass_estatutos_secuenciales_eval.tl.obj"

        print(f"\nTESTING QUADRUPLES: {file1_name}\n")
        result = filecmp.cmp(file1_name, file2_name)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_quadruple_2_3_pass_estatutos_secuenciales_eval(self):

        file1_name = TESTING_CODE + "2_3_pass_estatutos_secuenciales_eval.tl.test"
        file2_name = OBJECT_CODE + "2_3_pass_estatutos_secuenciales_eval.tl.obj"

        print(f"\nTESTING QUADRUPLES: {file1_name}\n")
        result = filecmp.cmp(file1_name, file2_name)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_quadruple_2_4_pass_estatutos_secuenciales_eval(self):
        file1_name = TESTING_CODE + "2_4_pass_estatutos_secuenciales_eval.tl.test"
        file2_name = OBJECT_CODE + "2_4_pass_estatutos_secuenciales_eval.tl.obj"

        print(f"\nTESTING QUADRUPLES: {file1_name}\n")
        result = filecmp.cmp(file1_name, file2_name)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_quadruple_3_4_pass_estatutos_condicionales_if_else(self):
        file1_name = TESTING_CODE + "3_4_pass_estatutos_condicionales_if_else.tl.test"
        file2_name = OBJECT_CODE + "3_4_pass_estatutos_condicionales_if_else.tl.obj"

        print(f"\nTESTING QUADRUPLES: {file1_name}\n")
        result = filecmp.cmp(file1_name, file2_name)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_quadruple_3_0_1_pass_estatutos_condicionales_if(self):
        file1_name = TESTING_CODE + "3_0_1_pass_estatutos_condicionales_if.tl.test"
        file2_name = OBJECT_CODE + "3_0_1_pass_estatutos_condicionales_if.tl.obj"

        print(f"\nTESTING QUADRUPLES: {file1_name}\n")
        result = filecmp.cmp(file1_name, file2_name)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_quadruple_4_0_pass_loops(self):
        file1_name = TESTING_CODE + "4_0_pass_loops.tl.test"
        file2_name = OBJECT_CODE + "4_0_pass_loops.tl.obj"

        print(f"\nTESTING QUADRUPLES: {file1_name}\n")
        result = filecmp.cmp(file1_name, file2_name)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_quadruple_4_1_pass_do_loop(self):
        file1_name = TESTING_CODE + "4_1_pass_do_loop.tl.test"
        file2_name = OBJECT_CODE + "4_1_pass_do_loop.tl.obj"

        print(f"\nTESTING QUADRUPLES: {file1_name}\n")
        result = filecmp.cmp(file1_name, file2_name)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_quadruple_4_2_pass_integration_test(self):
        file1_name = TESTING_CODE + "4_2_pass_integration_test.tl.test"
        file2_name = OBJECT_CODE + "4_2_pass_integration_test.tl.obj"

        print(f"\nTESTING QUADRUPLES: {file1_name}\n")
        result = filecmp.cmp(file1_name, file2_name)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)
