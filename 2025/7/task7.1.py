import sys

def solve(matrix: list[list[str]]) -> int:
    laser_arr = set()
    splits = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            ch = matrix[row][col]
            if ch == 'S':
                laser_arr.add(col)
            if ch == '^' and col in laser_arr:
                splits += 1
                laser_arr.discard(col)
                laser_arr.update([col-1, col+1])

    return splits


def main():
    data = sys.stdin.read().split('\n')
    matrix = [list(x) for x in data]
    res = solve(matrix)
    print(res)

if __name__ == '__main__':
    main()