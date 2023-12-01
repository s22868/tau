import unittest

from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):

    def test_correct_addition(self):
        num1, num2 = 3, 7
        self.assertEqual(add(num1, num2), 10)

    def test_correct_division_with_fraction(self):
        num1, num2 = 21, 37
        self.assertEqual(divide(num1, num2),0.5675675675675675)

    def test_division_by_zero(self):
        num1, num2 = 42, 0
        self.assertRaises(ValueError, divide, num1, num2)

    def test_addition_result_greater_than_zero(self):
        num1, num2 = 5, 3
        self.assertTrue(add(num1, num2) > 0)

    def test_correct_large_division_result(self):
        num1, num2 = 1, 1000000
        self.assertAlmostEqual(0.000001, divide(num1, num2), places=6)

    def test_divide_is_not_equal(self):
        num1, num2 = 12, 6
        self.assertNotEqual(1, subtract(num1, num2))

    def test_correct_addition_with_negatives_values(self):
        num1, num2 = -30, 21
        self.assertEqual(-9, add(num1, num2))

    def test_doesnt_return_wrong_type(self):
        num1, num2 = 21.37, 6.9
        self.assertIsNot(type('a'), type(add(num1, num2)))

    def test_correct_return_type(self):
        num1, num2 = 6.9, 42.0
        self.assertIs(type(48.9), type(add(num1, num2)))

    def test_correct_multiplication_with_float(self):
        num1, num2 = 21.37, 69.0
        self.assertAlmostEqual(1474.53, multiply(num1, num2), places=1)



if __name__ == '__main__':
    unittest.main()