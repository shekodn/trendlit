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
    def test_0_2_1_pass_uminus(self):
        tl_file_to_compile = "0_2_1_pass_uminus.tl"
        trendlit_helper.reads_file(COMPILED_CODE_DIR, OUR_TESTS_PATH + tl_file_to_compile)
        expected_file = TESTING_CODE_DIR + "0_2_1_pass_uminus.tl.html.test"
        generated_file = COMPILED_CODE_DIR + "generated_file.tl.html"
        result = filecmp.cmp(expected_file, expected_file)
        should_files_be_equal = True
        self.assertEqual(should_files_be_equal, result)
