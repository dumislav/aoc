def map_processor(map, input_range):
    out = []
    x, y = input_range
    start = x
    for src, map_item in map.items():
        dst = map_item[0]
        range = map_item[1]
        diff = dst - src

        if x < src and len(out) == 0:
            start = x
            if y <= src:
                end = y
            else:
                x = end = src
            out.append((start, end))

        if x >= src and x < src+range:
            start = x + diff
            if y <= src+range:
                end = y + diff
            else:
                end = dst + range
                x = src + range
            out.append((start, end))

    if y > src + range or len(out) == 0:
        out.append((x, y))

    return out

def main():
    with open('input.txt', 'r') as f:
        data = f.read()

    rows = data.split('\n')
    br = -1
    all_maps = {}
    new_map = False
    seed_ranges = []
    for i, row in enumerate(rows):
        if i == 0:
            x = None
            for num in row.split(' '):
                if num.isdigit() == False:
                    continue
                if x is not None:
                    y = x + int(num)
                    seed_ranges.append((x, y))
                    x = None
                else:
                    x = int(num)
        else:
            rownums = [int(num) for num in row.split(' ') if num.isdigit()]
            if len(rownums) == 0:
                new_map = True
            else:
                if new_map:
                    br += 1
                    all_maps[br] = {}
                    new_map = False

                dst, src, myrange = rownums
                all_maps[br][src] = [dst, myrange]

    for key, curr_map in all_maps.items():
        all_maps[key] = dict(sorted(curr_map.items()))

    input_ranges = seed_ranges
    location_ranges = []

    for key, curr_map in all_maps.items():
        output_ranges = []
        # print(f'Input ranges: {input_ranges}')
        # print(f'Current map: {curr_map}')
        for input_range in input_ranges:
            output_range = map_processor(curr_map, input_range)
            output_ranges.extend(output_range)
        # print(f'Output ranges: {output_ranges}')
        input_ranges = output_ranges

    location_ranges.extend(output_ranges)

    location_ranges_min = [x for x, y in location_ranges]
    print(min(location_ranges_min))

if __name__ == '__main__':
    main()