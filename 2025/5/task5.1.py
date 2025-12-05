def read_input(delimiter='\n') -> list:
    with open('input.txt', 'r') as f:
        data = f.read()
    arr = data.split(delimiter)

    return arr

def get_fresh(data: list) -> list:
    fresh = []
    for row in data:
        if '-' in row:
            fresh_range = row.split('-')
            fresh.append((int(fresh_range[0]), int(fresh_range[1])))

    return fresh

def get_ingredients(data: list) -> list:
    ingredients = []
    for row in data:
        if row.isnumeric():
            ingredients.append(int(row))

    return ingredients

def main():
    data = read_input()
    fresh_arr = get_fresh(data)
    ingredients = get_ingredients(data)
    fresh_count = 0

    for i in ingredients:
#        print(f"Checking ingredient: {i}")
        for fresh_range in fresh_arr:
            if i >= fresh_range[0] and i <= fresh_range[1]:
#                print(f"Ingredient {i} is fresh in range {fresh_range[0]}-{fresh_range[1]}")
                fresh_count += 1
                break

    print(fresh_count)
    
if __name__ == '__main__':
    main()