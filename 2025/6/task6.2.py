def solve(matrix: list[list[str]]) -> int:
    total = 0
    rows = len(matrix)
    cols = len(matrix[0])

    vertical_nums = []
    operand = None
    for x in range(cols):
        vertical_num = ''
        for y in range(rows):
            ch = matrix[y][x]
            if ch.isdigit():
                vertical_num = vertical_num + ch
            if ch in ['+', '*']:
                operand = ch

        if vertical_num:
            vertical_nums.append(int(vertical_num))

        if vertical_num == '' or (x == cols - 1 and y == rows - 1):
            if operand == '+':
                total += sum(vertical_nums)
            elif operand == '*':
                multi = 1
                for num in vertical_nums:
                    multi *= num
                total += multi
            vertical_nums = []

    return total

def main():
    with open('input.txt', 'r') as f:
        data = f.read().split('\n')

    matrix = [list(x) for x in data]
    res = solve(matrix)
    print(res)

if __name__ == '__main__':
    main()