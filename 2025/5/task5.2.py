def read_input(file='input.txt', delimiter='\n') -> list:
    with open(file, 'r') as f:
        data = f.read()
    arr = data.split(delimiter)

    return arr

def get_fresh_list(data: list) -> list:
    fresh = []
    for row in data:
        if '-' in row:
            fresh_range = row.split('-')
            fresh.append((int(fresh_range[0]), int(fresh_range[1])))

    return fresh

def merge_arr(arr: list) -> list:
    arr.sort()
    n = len(arr)
    res = []
    for i in range(n):
        start = arr[i][0]
        end = arr[i][1]

        if res and res[-1][1] >= end:
            continue

        for j in range(i + 1, n):
            if arr[j][0] <= end:
                if arr[j][1] > end:
                    end = arr[j][1]
            else:
                break
        res.append((start, end))
    
    return res

def count_ranges(arr: list) -> int:
    count = 0
    for r in arr:
        count += (r[1] - r[0] + 1)
    return count

def main():
    data = read_input()
    arr = get_fresh_list(data)

    merged = merge_arr(arr)
    result = count_ranges(merged)
    print(result)

if __name__ == '__main__':
    main()