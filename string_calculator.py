class StringCalculator:
    def Add(self, numbers):
        if not numbers:
            return 0
            
        # Check for custom delimiter(s)
        if numbers.startswith('//'):
            delimiter_part, numbers = numbers.split('\n', 1)
            delimiters = []
            # Handle multiple delimiters in format [delim1][delim2]...
            if '[' in delimiter_part:
                while '[' in delimiter_part:
                    start = delimiter_part.find('[') + 1
                    end = delimiter_part.find(']')
                    delimiters.append(delimiter_part[start:end])
                    delimiter_part = delimiter_part[end+1:]
            else:
                # Single delimiter
                delimiters = [delimiter_part[2:]]
        else:
            delimiters = [',']

            
        # Replace new lines with first delimiter and split
        numbers = numbers.replace('\n', delimiters[0])
        
        # Split by all delimiters
        for delimiter in delimiters:
            numbers = numbers.replace(delimiter, delimiters[0])
        num_list = [int(num) for num in numbers.split(delimiters[0])]

        
        # Filter out numbers greater than 1000
        num_list = [num for num in num_list if num <= 1000]
        
        # Check for negative numbers
        negatives = [num for num in num_list if num < 0]

        if negatives:
            raise Exception(f"negatives not allowed: {', '.join(map(str, negatives))}")
            
        return sum(num_list)
