import math

def read_input() -> list:
    with open('input1.1.txt', 'r') as f:
        data = f.read()
    arr = data.splitlines()

    return arr

def unlock_safe(start=int, data=list) -> int:
    found_zeros = 0
    total_clicks = 0
    for move in data:
        index, clicks = rotate_knob(start, move)
        start = index
        total_clicks += clicks

    return total_clicks

def rotate_knob(start=int, move=str) -> tuple:
    clicks = 0
    index = start
    direction, steps = str(move[0]), int(move[1:])
    if(steps > 100):
        clicks = math.floor(steps / 100)
    steps = steps % 100
    if(direction == 'L'):
        index = start - steps
        if(index < 0):
            if(start != 0):
                clicks += 1
            index = 100 + index
    elif(direction == 'R'):
        index = start + steps
        if(index >= 100):
            index = index - 100
            if(index != 0):
                clicks += 1

    if(index == 0):
        clicks += 1

    print(f"Start: {start}, Move: {move}, Index: {index}, Clicks: {clicks}")
    return index, clicks

def main():
    data = read_input()
    password = unlock_safe(50, data)
    print(password)

if __name__ == '__main__':
    main()