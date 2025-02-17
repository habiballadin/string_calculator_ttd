class StringCalculator:
    def Add(self, numbers):
        if not numbers:
            return 0
        if ',' in numbers:
            return sum(int(num) for num in numbers.split(','))
        return int(numbers)
