import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def test_empty_string_returns_zero(self):
        calculator = StringCalculator()
        self.assertEqual(calculator.Add(""), 0)

    def test_single_number_returns_same_number(self):
        calculator = StringCalculator()
        self.assertEqual(calculator.Add("1"), 1)

    def test_two_numbers_returns_sum(self):
        calculator = StringCalculator()
        self.assertEqual(calculator.Add("1,2"), 3)

    def test_multiple_numbers_returns_sum(self):
        calculator = StringCalculator()
        self.assertEqual(calculator.Add("1,2,3,4,5"), 15)

    def test_new_line_delimiter_returns_sum(self):
        calculator = StringCalculator()
        self.assertEqual(calculator.Add("1\n2,3"), 6)

if __name__ == '__main__':




    unittest.main()
