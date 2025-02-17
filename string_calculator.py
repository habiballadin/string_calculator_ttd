class StringCalculator:
    def Add(self, numbers):
        if not numbers:
            return 0
            
        # Check for custom delimiter
        if numbers.startswith('//'):
            delimiter, numbers = numbers.split('\n', 1)
            delimiter = delimiter[2:]  # Remove the '//'
        else:
            delimiter = ','
            
        # Replace new lines with delimiter and split
        numbers = numbers.replace('\n', delimiter)
        return sum(int(num) for num in numbers.split(delimiter))
