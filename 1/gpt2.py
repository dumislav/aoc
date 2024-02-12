import re

# Create a dictionary for word to digit mapping
word_to_digit = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

# Initialize a variable to keep the sum of the calibration values
calibration_sum = 0

# Prepare a regex pattern for finding worded digits
digit_words_pattern = re.compile('|'.join(word_to_digit.keys()))

# Open the file input.txt in read mode
with open('input.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Remove any leading/trailing whitespaces
        line = line.strip()
        
        # Replace worded digits with actual digits
        line = digit_words_pattern.sub(lambda x: word_to_digit[x.group()], line)
        
        # Using regex to extract all digits from the processed line
        digits_in_line = re.findall(r'\d', line)
        
        # Check if we have at least two digits to form a two-digit number
        if len(digits_in_line) >= 2:
            # Get the first and last digits
            first_digit = digits_in_line[0]
            last_digit = digits_in_line[-1]
            
            # Combine the first and the last digit to make a two-digit number
            calibration_value = int(first_digit + last_digit)
            
            # Add the calibration value to the sum
            calibration_sum += calibration_value

# Print the total sum of the calibration values
print(f"The sum of all calibration values is: {calibration_sum}")