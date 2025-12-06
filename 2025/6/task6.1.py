import sys

def solve(matrix):
    total = 0
    rows = len(matrix)
    cols = len(matrix[0])

    for y in range(cols):
        operand = matrix[-1][y]
        col_res = 1 if operand == '*' else 0
        nums = []
        for x in range(rows -1):
            nums.append(int(matrix[x][y]))
        for num in nums:
            if operand == '+':
                col_res += num
            else:
                col_res *= num

        total += col_res

    return total

def main():
    data = sys.stdin.read().split('\n')
    matrix = [x.split() for x in data]
    res = solve(matrix)
    print(res)

if __name__ == '__main__':
    main()