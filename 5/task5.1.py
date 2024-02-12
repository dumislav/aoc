def main():
    with open('input.txt', 'r') as f:
        data = f.read()

    rows = data.split('\n')
    br = -1
    map = {}
    restart = False
    for i, row in enumerate(rows):
        if i == 0:
            seeds = [int(num) for num in row.split(' ') if num.isdigit()]
        else:
            rownums = [int(num) for num in row.split(' ') if num.isdigit()]
            if len(rownums) == 0:
                restart = True
            else:
                if restart:
                    br += 1
                    map[br] = {}
                    restart = False

                dst = rownums[0]
                src = rownums[1]
                myrange = rownums[2]
                map[br][src] = [dst, myrange]

    for key, curr_map in map.items():
        map[key] = dict(sorted(curr_map.items()))

    locations = []
    for seed in seeds:
        next = None
        for key, curr_map in map.items():
            if next is not None:
                seed = next
            print(f'br: {key}, seed: {seed}, curr_map: {curr_map}')
            for src, items in curr_map.items():
                dst = items[0]
                myrange = items[1]
                print(f'seed: {seed}, src: {src}, dst: {dst}, myrange: {myrange}')
                if seed >= src and seed < src+myrange:
                    next = dst - src + seed
                    break
            if next is None:
                next = seed

        locations.append(next)
    print(sorted(locations)[0])

if __name__ == '__main__':
    main()