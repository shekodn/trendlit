import unittest  # Reference: https://docs.python.org/2/library/unittest.html
from semantic_cube.semantic_cube import Cube, type_int, type_error
from semantic_cube.semantic_cube_helper import token_to_code, type_to_code


class SemanticCubeTestCase(unittest.TestCase):
    # def test_is_in_cube(self):
    #     oracle = Cube()
    #     operType1 = type_int
    #     operType2 = type_int
    #     op = token_to_code.get("+")
    #     result = oracle.is_in_cube(operType1, operType2, op)
    #     print(f"\nTESTING: test_is_in_cube\n")
    #     self.assertEqual(result, True)
    #
    # def test_is_not_in_cube(self):
    #     oracle = Cube()
    #     operType1 = type_int
    #     operType2 = type_int
    #     # Inavlid op
    #     op = -12123
    #     result = oracle.is_in_cube(operType1, operType2, op)
    #     print(f"\nTESTING: test_is_not_in_cube\n")
    #     self.assertEqual(result, False)

    def test_nothiing(self):
        return None
