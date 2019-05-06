import unittest  # Reference: https://docs.python.org/2/library/unittest.html
from quadruple.quadruple import Quadruple
import filecmp
from trendlit_helper.trendlit_helper import TrendlitHelper

trendlit_helper = TrendlitHelper()

# Test generated folder
COMPILED_CODE_DIR = "compiled_code_test/"
TESTING_CODE_DIR = "tests/compiled_code/"
OUR_TESTS_PATH = "our_tests/"


class QuadruplesTestCase(unittest.TestCase):
    def test_0_2_1_pass_eval_comma(self):
        tl_file_to_compile = "0_2_1_pass_eval_comma.tl"
        trendlit_helper.reads_file(
            COMPILED_CODE_DIR, OUR_TESTS_PATH + tl_file_to_compile
        )
        expected_file = TESTING_CODE_DIR + tl_file_to_compile + ".html.test"
        generated_file = COMPILED_CODE_DIR + tl_file_to_compile + ".html"
        result = filecmp.cmp(expected_file, generated_file)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_0_2_1_pass_uminus(self):
        tl_file_to_compile = "0_2_1_pass_uminus.tl"
        trendlit_helper.reads_file(
            COMPILED_CODE_DIR, OUR_TESTS_PATH + tl_file_to_compile
        )
        expected_file = TESTING_CODE_DIR + "0_2_1_pass_uminus.tl.html.test"
        generated_file = COMPILED_CODE_DIR + "0_2_1_pass_uminus.tl.html"
        result = filecmp.cmp(expected_file, generated_file)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_2_5_pass_and_or(self):
        tl_file_to_compile = "2_5_pass_and_or.tl"
        trendlit_helper.reads_file(
            COMPILED_CODE_DIR, OUR_TESTS_PATH + tl_file_to_compile
        )
        expected_file = TESTING_CODE_DIR + "2_5_pass_and_or.tl.html.test"
        generated_file = COMPILED_CODE_DIR + "2_5_pass_and_or.tl.html"
        result = filecmp.cmp(expected_file, generated_file)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_9_2_1_pass_array_precedence(self):
        tl_file_to_compile = "9_2_1_pass_array_precedence.tl"
        trendlit_helper.reads_file(
            COMPILED_CODE_DIR, OUR_TESTS_PATH + tl_file_to_compile
        )
        expected_file = TESTING_CODE_DIR + "9_2_1_pass_array_precedence.tl.html.test"
        generated_file = COMPILED_CODE_DIR + "9_2_1_pass_array_precedence.tl.html"
        result = filecmp.cmp(expected_file, generated_file)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_9_2_pass_array_access(self):
        tl_file_to_compile = "9_2_pass_array_access.tl"
        trendlit_helper.reads_file(
            COMPILED_CODE_DIR, OUR_TESTS_PATH + tl_file_to_compile
        )
        expected_file = TESTING_CODE_DIR + tl_file_to_compile + ".html.test"
        generated_file = COMPILED_CODE_DIR + tl_file_to_compile + ".html"
        result = filecmp.cmp(expected_file, generated_file)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_5_6_7_pass_calls_function(self):
        tl_file_to_compile = "5_6_7_pass_calls_function.tl"
        trendlit_helper.reads_file(
            COMPILED_CODE_DIR, OUR_TESTS_PATH + tl_file_to_compile
        )
        expected_file = TESTING_CODE_DIR + tl_file_to_compile + ".html.test"
        generated_file = COMPILED_CODE_DIR + tl_file_to_compile + ".html"
        result = filecmp.cmp(expected_file, generated_file)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_5_6_7_1_pass_calls_params_function(self):
        tl_file_to_compile = "5_6_7_1_pass_calls_params_function.tl"
        trendlit_helper.reads_file(
            COMPILED_CODE_DIR, OUR_TESTS_PATH + tl_file_to_compile
        )
        expected_file = TESTING_CODE_DIR + tl_file_to_compile + ".html.test"
        generated_file = COMPILED_CODE_DIR + tl_file_to_compile + ".html"
        result = filecmp.cmp(expected_file, generated_file)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_5_6_0_pass_calls_function(self):
        tl_file_to_compile = "5_6_0_pass_calls_function.tl"
        trendlit_helper.reads_file(
            COMPILED_CODE_DIR, OUR_TESTS_PATH + tl_file_to_compile
        )
        expected_file = TESTING_CODE_DIR + tl_file_to_compile + ".html.test"
        generated_file = COMPILED_CODE_DIR + tl_file_to_compile + ".html"
        result = filecmp.cmp(expected_file, generated_file)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_final_function_bubble_sort(self):
        tl_file_to_compile = "final_function_bubble_sort.tl"
        trendlit_helper.reads_file(
            COMPILED_CODE_DIR, OUR_TESTS_PATH + tl_file_to_compile
        )
        expected_file = TESTING_CODE_DIR + tl_file_to_compile + ".html.test"
        generated_file = COMPILED_CODE_DIR + tl_file_to_compile + ".html"
        result = filecmp.cmp(expected_file, generated_file)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_final_function_find(self):
        tl_file_to_compile = "final_function_find.tl"
        trendlit_helper.reads_file(
            COMPILED_CODE_DIR, OUR_TESTS_PATH + tl_file_to_compile
        )
        expected_file = TESTING_CODE_DIR + tl_file_to_compile + ".html.test"
        generated_file = COMPILED_CODE_DIR + tl_file_to_compile + ".html"
        result = filecmp.cmp(expected_file, generated_file)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_final_fibonacci_iterative(self):
        tl_file_to_compile = "final_fibonacci_iterative.tl"
        trendlit_helper.reads_file(
            COMPILED_CODE_DIR, OUR_TESTS_PATH + tl_file_to_compile
        )
        expected_file = TESTING_CODE_DIR + tl_file_to_compile + ".html.test"
        generated_file = COMPILED_CODE_DIR + tl_file_to_compile + ".html"
        result = filecmp.cmp(expected_file, generated_file)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_final_fibonacci_recursive(self):
        tl_file_to_compile = "final_fibonacci_recursive.tl"
        trendlit_helper.reads_file(
            COMPILED_CODE_DIR, OUR_TESTS_PATH + tl_file_to_compile
        )
        expected_file = TESTING_CODE_DIR + tl_file_to_compile + ".html.test"
        generated_file = COMPILED_CODE_DIR + tl_file_to_compile + ".html"
        result = filecmp.cmp(expected_file, generated_file)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_final_factorial_iterative(self):
        tl_file_to_compile = "final_factorial_iterative.tl"
        trendlit_helper.reads_file(
            COMPILED_CODE_DIR, OUR_TESTS_PATH + tl_file_to_compile
        )
        expected_file = TESTING_CODE_DIR + tl_file_to_compile + ".html.test"
        generated_file = COMPILED_CODE_DIR + tl_file_to_compile + ".html"
        result = filecmp.cmp(expected_file, generated_file)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_final_factorial_recursive(self):
        tl_file_to_compile = "final_factorial_recursive.tl"
        trendlit_helper.reads_file(
            COMPILED_CODE_DIR, OUR_TESTS_PATH + tl_file_to_compile
        )
        expected_file = TESTING_CODE_DIR + tl_file_to_compile + ".html.test"
        generated_file = COMPILED_CODE_DIR + tl_file_to_compile + ".html"
        result = filecmp.cmp(expected_file, generated_file)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)

    def test_final_factorial_recursive(self):
        tl_file_to_compile = "final_factorial_recursive.tl"
        trendlit_helper.reads_file(
            COMPILED_CODE_DIR, OUR_TESTS_PATH + tl_file_to_compile
        )
        expected_file = TESTING_CODE_DIR + tl_file_to_compile + ".html.test"
        generated_file = COMPILED_CODE_DIR + tl_file_to_compile + ".html"
        result = filecmp.cmp(expected_file, generated_file)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)
