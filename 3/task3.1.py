import re

def findSpecialAroundNumber(number, row, matrix):
    for x in range(row-1, row+2):
        for y in range(number.start()-1, number.end()+1):
            if x < 0 or y < 0:
                continue
            if x == row and y >= number.start() and y < number.end():
                continue
            try:
                el = matrix[(x, y)]
            except KeyError:
                el = None

            if el != None and el != '.':
                return True
    return False

def main(data):
    rows = data.split('\n')

    matrix = {}
    x = 0
    for row in rows:
        y = 0
        for char in row:
            matrix[(x, y)] = char
            y+=1
        x+=1

    x = 0
    founded = []
    for row in rows:
        # find all numbers in row with ther start and end index
        numbers = re.finditer(r'\d+', row)
        for number in numbers:
            if(findSpecialAroundNumber(number, x, matrix)):
                founded.append(int(number.group()))
                print(number.group(), end=' ')
        x+=1
        print()

    print(sum(founded))


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        data = f.read()
        main(data)