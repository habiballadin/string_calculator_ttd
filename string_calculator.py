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
        num_list = [int(num) for num in numbers.split(delimiter)]
        
        # Check for negative numbers
        negatives = [num for num in num_list if num < 0]
        if negatives:
            raise Exception(f"negatives not allowed: {', '.join(map(str, negatives))}")
            
        return sum(num_list)
