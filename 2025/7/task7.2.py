import sys

def solve(matrix: list[list[str]]) -> int:
    paths = {}
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            ch = matrix[row][col]
            if ch == 'S':
                paths[col] = 1
            if ch == '^' and col in paths:
                for i in [col-1, col+1]:
                    if i in paths:
                        paths[i] += paths.get(col)
                    else:
                        paths[i] = paths.get(col)
                del paths[col]

    return sum(paths.values())


def main():
    data = sys.stdin.read().split('\n')
    matrix = [list(x) for x in data]
    res = solve(matrix)
    print(res)

if __name__ == '__main__':
    main()