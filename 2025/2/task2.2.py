def read_input(delimiter='\n') -> list:
    with open('input.txt', 'r') as f:
        data = f.read()
    arr = data.split(delimiter)

    return arr

def start_from(item=int, split=2) -> int:
    item_str = str(item)
    item_len = len(item_str)

    if(item_len == 1):
        return 1
    else:
        return int("1" * (item_len//split))

def get_invalid_items(item=str) -> list:
    invalid_items = ()
    begin = int(item.split('-')[0])
    end   = int(item.split('-')[1])
    end_len = len(str(end))

    split=2
    start= start_from(begin, split)
    start_str = str(start)
    start_len = len(str(start))
    
    print(f"Begin: {begin}, End: {end}, Start from: {start}")
    for length in range(1, start_len+1):
        for num_digits in range(2, end_len+1):
            check = int(start_str[:length])
            while(True):
                check_number = int(f"{check}" * num_digits)
#                print(f"Checking number: {check_number}")
                if(check_number < begin):
                    check += 1
                    continue
                elif(check_number > end):
                    break
                else:
                    if check_number not in invalid_items:
                        print(f"Found: {check_number}")
                        invalid_items += (check_number,)
                check += 1

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