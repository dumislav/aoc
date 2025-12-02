def read_input() -> list:
    with open('input1.1.txt', 'r') as f:
        data = f.read()
    arr = data.splitlines()

    return arr

def unlock_safe(start=int, data=list) -> int:
    found_zeros = 0
    for move in data:
        index = rotate_knob(start, move)
        start = index
        if(index == 0):
            found_zeros += 1
    return found_zeros

def rotate_knob(start=int, move=str) -> int:
    index = start
    direction, steps = str(move[0]), int(move[1:])
    steps = steps % 100
    if(direction == 'L'):
        index = start - steps
        if(index < 0):
            index = 100 + index
    elif(direction == 'R'):
        index = start + steps
        if(index >= 100):
            index = index - 100

    print(f"Start: {start}, Move: {move}, Index: {index}")
    return index

def main():
    data = read_input()
    password = unlock_safe(50, data)
    print(password)

if __name__ == '__main__':
    main()