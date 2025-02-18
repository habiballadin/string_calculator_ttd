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

    def test_custom_delimiter_returns_sum(self):
        calculator = StringCalculator()
        self.assertEqual(calculator.Add("//;\n1;2"), 3)

    def test_negative_number_throws_exception(self):
        calculator = StringCalculator()
        with self.assertRaises(Exception) as context:
            calculator.Add("1,-2,3")
        self.assertEqual(str(context.exception), "negatives not allowed: -2")

    def test_numbers_greater_than_1000_are_ignored(self):
        calculator = StringCalculator()
        self.assertEqual(calculator.Add("2,1001"), 2)

    def test_multiple_delimiters_of_any_length(self):
        calculator = StringCalculator()
        self.assertEqual(calculator.Add("//[*][%]\n1*2%3"), 6)

    def test_delimiters_of_varying_lengths(self):
        calculator = StringCalculator()
        self.assertEqual(calculator.Add("//[***][%%]\n1***2%%3"), 6)

    def test_multiple_delimiters_with_varying_lengths(self):
        calculator = StringCalculator()
        self.assertEqual(calculator.Add("//[**][%%][$$$]\n1**2%%3$$$4"), 10)

if __name__ == '__main__':

    unittest.main()
