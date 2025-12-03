
def read_input(delimiter='\n') -> list:
    with open('input.txt', 'r') as f:
        data = f.read()
    arr = data.split(delimiter)

    return arr

def main():
    data = read_input(',')
    print(data)

if __name__ == '__main__':
    main()