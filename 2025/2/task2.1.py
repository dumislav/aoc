def read_input(delimiter='\n') -> list:
    with open('input.txt', 'r') as f:
        data = f.read()
    arr = data.split(delimiter)

    return arr

def get_invalid_items(item=str) -> list:
    invalid = [1, 2]
    return invalid

def main():
    data = read_input(',')
    invalid_items = []
    for item in data:
        invalid_items.extend(get_invalid_items(item))

    invalid_items_sum = sum(invalid_items)
    print(invalid_items_sum)

if __name__ == '__main__':
    main()