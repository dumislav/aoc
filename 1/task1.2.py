import re
from my1 import sumOfDigits

numbersAsWordAssoc = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

digitAndWord = list(map(str, numbersAsWordAssoc.keys())) + list(map(str, numbersAsWordAssoc.values()))

def numToDigit(num):
    if str(num) in numbersAsWordAssoc:
        return int(numbersAsWordAssoc[num])
    else:
        return int(num)

def sumOfWordDigits(data):
    sum = 0
    rows = data.split('\n')
    for row in rows:
        foundNumbersInRow = []
        for word in digitAndWord:
            word = str(word)
            for m in re.finditer(word, row):
                foundNumbersInRow.append((word, m.start()))

        firstFound = numToDigit(min(foundNumbersInRow, key=lambda x: x[1])[0])
        lastFound = numToDigit(max(foundNumbersInRow, key=lambda x: x[1])[0])

        rowNumber = str(firstFound) + str(lastFound)

        sum += int(rowNumber)

    return sum

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        data = f.read()
        print(sumOfWordDigits(data))