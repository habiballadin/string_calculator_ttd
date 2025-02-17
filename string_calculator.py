class StringCalculator:
    def Add(self, numbers):
        if not numbers:
            return 0
        # Replace new lines with commas and split
        numbers = numbers.replace('\n', ',')
        return sum(int(num) for num in numbers.split(','))
