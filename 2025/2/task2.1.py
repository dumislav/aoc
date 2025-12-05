def read_input(delimiter='\n') -> list:
    with open('input.txt', 'r') as f:
        data = f.read()
    arr = data.split(delimiter)

    return arr

def start_from(item=int) -> int:
    item_str = str(item)
    item_len = len(item_str)

    if(item_len == 1):
        return 1
    else:
        return int(item_str[0:item_len//2])

def get_invalid_items(item=str) -> list:
    invalid_items = []
    begin = int(item.split('-')[0])
    end   = int(item.split('-')[1])

    check = start_from(begin)

    print(f"Begin: {begin}, End: {end}, Start from: {check}")
    while(True):
        check_number = int(f"{check}" * 2)
        if(check_number < begin):
            check += 1
            continue
        elif(check_number > end):
            break
        else:
            print(f"Found: {check_number}")
            invalid_items.append(check_number)
        check += 1

    invalid_items = list(set(invalid_items)) 
    return invalid_items

def main():
    data = read_input(',')
    invalid_items = []
    for item in data:
        print(f"--- Processing item: {item}")
        invalid_items.extend(get_invalid_items(item))
    invalid_items_sum = sum(invalid_items)
    print(invalid_items_sum)

if __name__ == '__main__':
    main()