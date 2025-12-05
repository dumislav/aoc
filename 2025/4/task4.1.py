def read_input(delimiter='\n') -> list:
    with open('input.txt', 'r') as f:
        data = f.read()
    arr = data.split(delimiter)

    return arr

def rolls_around(x: int, y: int, matrix: list) -> int:
    count = 0
    for cx in range(x-1, x+2):
        for cy in range(y-1, y+2):
            if cx < 0 or cy < 0:
                continue
            if cy >= len(matrix):
                continue
            if cx >= len(matrix[cy]):
                continue
            if matrix[cy][cx] == '@':
                count += 1

    return count

def main():
    data = read_input()

    matrix = []
    result = 0
    for item in data:
        matrix.append(item)

    for y, row in enumerate(matrix):
        for x, ch in enumerate(row):
            if ch == '@':
                rolls = rolls_around(x, y, matrix)
                print(f"Cell ({x},{y}) has {rolls} rolls around it.")
                if rolls <= 4:
                    result += 1

    print(result)
if __name__ == '__main__':
    main()