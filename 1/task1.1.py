import re

def sumOfDigits(data):
    total_sum = 0
    for row in data.split('\n'):
        digits = re.findall(r'\d', row)
        if len(digits) == 0:
            continue
        sum = int(digits[0] + digits[-1])
        total_sum += sum
    return total_sum

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        data = f.read()
        print(sumOfDigits(data))