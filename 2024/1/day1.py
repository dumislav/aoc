def main():
    with open('input.txt', 'r') as f:
        data = f.read()

    rows = data.split('\n')

    arr1 = []
    arr2 = []
    for row in rows:
        # split columns by whitespace
        cols = row.split()
        if len(cols) != 2:
            continue

        if (cols[0] not in arr1):
            arr1.append(cols[0])
        if (cols[1] not in arr2):
            arr2.append(cols[1])

    # sort num arrays bu number
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)

    total = 0
    for i in range(len(arr1)):
        if i >= len(arr2):
            break

        diff = (int(arr2[i]) - int(arr1[i]))
        print(arr1[i], arr2[i], diff)
        if diff > 0:
            total += diff

    print(total)
if __name__ == '__main__':
    main()