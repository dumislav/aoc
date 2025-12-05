def read_input(delimiter='\n') -> list:
    with open('input.txt', 'r') as f:
        data = f.read()
    arr = data.split(delimiter)

    return arr

def get_max(item: str, start: int, end_pos: int) -> tuple:
    max_digit = 0
    max_pos = 0
    for i, ch in enumerate(item):
        digit = int(ch)
        if digit > max_digit:
            if i > end_pos:
                continue
            if i < start:
                continue
            max_digit = digit
            max_pos = i

    return max_pos, max_digit

def main():
    #day1
    #cells = 2

    #day2
    cells = 12

    data = read_input()

    cell_size = 99
    total_joltage = 0
    for item in data:
        start = 0
        battery_pack = []
        for num in range(cells):
            battery = get_max(item, start, cell_size - (cells - num - 1))
            start = battery[0] + 1
            battery_pack.append(battery[1])

        joltage = int("".join(map(str, battery_pack)))
        print(f"Processing item: {item} => Joltage: {joltage}")
        total_joltage += joltage

    print(total_joltage)

if __name__ == '__main__':
    main()