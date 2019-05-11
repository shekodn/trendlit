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
    def test_quadruple_0_1_0_pass_str_estatutos_secuenciales(self):

        file1_name = TESTING_CODE + "0_1_0_pass_str_estatutos_secuenciales.tl.test"
        file2_name = OBJECT_CODE + "0_1_0_pass_str_estatutos_secuenciales.tl.obj"

    def test_quadruple_2_0_pass_estatutos_secuenciales(self):

        file1_name = TESTING_CODE + "2_0_pass_estatutos_secuenciales.tl.test"
        file2_name = OBJECT_CODE + "2_0_pass_estatutos_secuenciales.tl.obj"

        print(f"\nTESTING QUADRUPLES: {file1_name}\n")
        result = filecmp.cmp(file1_name, file2_name)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

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

    # def test_quadruple_4_0_pass_loops(self):
    #     file1_name = TESTING_CODE + "4_0_pass_loops.tl.test"
    #     file2_name = OBJECT_CODE + "4_0_pass_loops.tl.obj"
    #
    #     print(f"\nTESTING QUADRUPLES: {file1_name}\n")
    #     result = filecmp.cmp(file1_name, file2_name)
    #     should_files_be_equal = True
    #     self.assertEqual(should_files_be_equal, result)

    # def test_quadruple_4_1_pass_do_loop(self):
    #     file1_name = TESTING_CODE + "4_1_pass_do_loop.tl.test"
    #     file2_name = OBJECT_CODE + "4_1_pass_do_loop.tl.obj"
    #
    #     print(f"\nTESTING QUADRUPLES: {file1_name}\n")
    #     result = filecmp.cmp(file1_name, file2_name)
    #     should_files_be_equal = True
    #     self.assertEqual(should_files_be_equal, result)

    def test_quadruple_4_2_pass_integration_test(self):
        file1_name = TESTING_CODE + "4_2_pass_integration_test.tl.test"
        file2_name = OBJECT_CODE + "4_2_pass_integration_test.tl.obj"

        print(f"\nTESTING QUADRUPLES: {file1_name}\n")
        result = filecmp.cmp(file1_name, file2_name)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_quadruple_5_0_pass_void_function(self):
        file1_name = TESTING_CODE + "5_0_pass_void_function.tl.test"
        file2_name = OBJECT_CODE + "5_0_pass_void_function.tl.obj"

        print(f"\nTESTING QUADRUPLES: {file1_name}\n")
        result = filecmp.cmp(file1_name, file2_name)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_quadruple_5_1_pass_returning_function(self):
        file1_name = TESTING_CODE + "5_1_pass_returning_function.tl.test"
        file2_name = OBJECT_CODE + "5_1_pass_returning_function.tl.obj"

        print(f"\nTESTING QUADRUPLES: {file1_name}\n")
        result = filecmp.cmp(file1_name, file2_name)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_quadruple_5_6_3_pass_many_calls_to_function(self):
        file1_name = TESTING_CODE + "5_6_3_pass_many_calls_to_function.tl.test"
        file2_name = OBJECT_CODE + "5_6_3_pass_many_calls_to_function.tl.obj"

        print(f"\nTESTING QUADRUPLES: {file1_name}\n")
        result = filecmp.cmp(file1_name, file2_name)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_quadruple_8_0_pass_gorritos_html(self):
        file1_name = TESTING_CODE + "8_0_pass_gorritos_html.tl.test"
        file2_name = OBJECT_CODE + "8_0_pass_gorritos_html.tl.obj"

        print(f"\nTESTING QUADRUPLES: {file1_name}\n")
        result = filecmp.cmp(file1_name, file2_name)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_quadruple_8_2_pass_gorritos_html(self):
        file1_name = TESTING_CODE + "8_2_pass_gorritos_html.tl.test"
        file2_name = OBJECT_CODE + "8_2_pass_gorritos_html.tl.obj"

        print(f"\nTESTING QUADRUPLES: {file1_name}\n")
        result = filecmp.cmp(file1_name, file2_name)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_quadruple_8_3_pass_loop_html(self):
        file1_name = TESTING_CODE + "8_3_pass_loop_html.tl.test"
        file2_name = OBJECT_CODE + "8_3_pass_loop_html.tl.obj"

        print(f"\nTESTING QUADRUPLES: {file1_name}\n")
        result = filecmp.cmp(file1_name, file2_name)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_quadruple_8_4_pass_nested_loop_html(self):
        file1_name = TESTING_CODE + "8_4_pass_nested_loop_html.tl.test"
        file2_name = OBJECT_CODE + "8_4_pass_nested_loop_html.tl.obj"

        print(f"\nTESTING QUADRUPLES: {file1_name}\n")
        result = filecmp.cmp(file1_name, file2_name)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_quadruple_8_5_1_pass_if_else_html(self):
        file1_name = TESTING_CODE + "8_5_1_pass_if_else_html.tl.test"
        file2_name = OBJECT_CODE + "8_5_1_pass_if_else_html.tl.obj"

        print(f"\nTESTING QUADRUPLES: {file1_name}\n")
        result = filecmp.cmp(file1_name, file2_name)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_quadruple_8_5_2_pass_nested_if_else_html(self):
        file1_name = TESTING_CODE + "8_5_2_pass_nested_if_else_html.tl.test"
        file2_name = OBJECT_CODE + "8_5_2_pass_nested_if_else_html.tl.obj"

        print(f"\nTESTING QUADRUPLES: {file1_name}\n")
        result = filecmp.cmp(file1_name, file2_name)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_quadruple_8_5_pass_if_inside_loop_html(self):
        file1_name = TESTING_CODE + "8_5_pass_if_inside_loop_html.tl.test"
        file2_name = OBJECT_CODE + "8_5_pass_if_inside_loop_html.tl.obj"

        print(f"\nTESTING QUADRUPLES: {file1_name}\n")
        result = filecmp.cmp(file1_name, file2_name)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_quadruple_8_6_pass_do_loop_html(self):
        file1_name = TESTING_CODE + "8_6_pass_do_loop_html.tl.test"
        file2_name = OBJECT_CODE + "8_6_pass_do_loop_html.tl.obj"

        print(f"\nTESTING QUADRUPLES: {file1_name}\n")
        result = filecmp.cmp(file1_name, file2_name)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_quadruple_9_0_pass_array(self):
        file1_name = TESTING_CODE + "9_0_pass_array.tl.test"
        file2_name = OBJECT_CODE + "9_0_pass_array.tl.obj"

        print(f"\nTESTING QUADRUPLES: {file1_name}\n")
        result = filecmp.cmp(file1_name, file2_name)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_quadruple_9_1_pass_array_access(self):
        file1_name = TESTING_CODE + "9_1_pass_array_access.tl.test"
        file2_name = OBJECT_CODE + "9_1_pass_array_access.tl.obj"

        print(f"\nTESTING QUADRUPLES: {file1_name}\n")
        result = filecmp.cmp(file1_name, file2_name)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)
