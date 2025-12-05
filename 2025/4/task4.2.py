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
    total_removed = 0
    for item in data:
        matrix.append(item)

    while True:
        removed = 0
        remapped_matrix = []
        for y, row in enumerate(matrix):
            remapped_matrix.append(list(row))
            for x, ch in enumerate(row):
                matrix[y] = list(matrix[y])
                if ch == '@':
                    rolls = rolls_around(x, y, matrix)
                    print(f"Cell ({x},{y}) has {rolls} rolls around it.")
                    if rolls <= 4:
                        remapped_matrix[y][x] = '.'
                        removed += 1
        total_removed += removed
        matrix = remapped_matrix
        if removed == 0:
            break

    print(total_removed)
if __name__ == '__main__':
    main()