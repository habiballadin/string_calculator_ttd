# String Calculator

A Python implementation of the String Calculator with comprehensive test coverage.

## Features

1. **Empty String Handling**: Returns 0 for empty strings
2. **Single Number**: Returns the number itself
3. **Multiple Numbers**: Returns the sum of numbers
4. **New Line Delimiters**: Handles new lines between numbers
5. **Custom Delimiters**: Supports custom delimiters using //[delimiter]\n format
6. **Negative Numbers**: Throws exception for negative numbers
7. **Large Numbers**: Ignores numbers greater than 1000
8. **Multiple Delimiters**: Supports multiple delimiters
9. **Variable Length Delimiters**: Handles delimiters of any length

## Test Cases

1. `test_empty_string_returns_zero`: Verifies empty string returns 0
2. `test_single_number_returns_same_number`: Verifies single number returns itself
3. `test_two_numbers_returns_sum`: Verifies sum of two numbers
4. `test_multiple_numbers_returns_sum`: Verifies sum of multiple numbers
5. `test_new_line_delimiter_returns_sum`: Verifies handling of new line delimiters
6. `test_custom_delimiter_returns_sum`: Verifies custom delimiter support
7. `test_negative_number_throws_exception`: Verifies exception for negative numbers
8. `test_numbers_greater_than_1000_are_ignored`: Verifies numbers > 1000 are ignored
9. `test_multiple_delimiters_of_any_length`: Verifies multiple delimiters support
10. `test_delimiters_of_varying_lengths`: Verifies delimiters of varying lengths
11. `test_multiple_delimiters_with_varying_lengths`: Verifies multiple delimiters with varying lengths

## Usage

```python
from string_calculator import StringCalculator

calculator = StringCalculator()

# Basic usage
print(calculator.Add("1,2,3"))  # Output: 6

# Custom delimiter
print(calculator.Add("//;\n1;2"))  # Output: 3

# Multiple delimiters
print(calculator.Add("//[*][%]\n1*2%3"))  # Output: 6

# Negative numbers (throws exception)
try:
    calculator.Add("1,-2,3")
except Exception as e:
    print(e)  # Output: negatives not allowed: -2
```

## Running Tests

To run all test cases:

```bash
python -m unittest test_string_calculator.py
