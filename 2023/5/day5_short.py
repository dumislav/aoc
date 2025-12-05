
with open('input.txt', 'r') as f:
    data = f.read()



def part2_reverse(data):
    seeds = [*map(int, data[0].split(": ")[1].split())]
    maps = [[[*map(int, n.split())] for n in i.split("\n")[1:]] for i in "\n".join(data[2:]).split("\n\n")]

    location = 0
    seed_pairs = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]

    while True:
        result = location
        for _map in maps[::-1]:
            for dest, src, rng in _map:
                if dest <= result < dest + rng:
                    idx = result - dest
                    result = src + idx
                    break
        if any(pair[0] <= result <= pair[1] for pair in seed_pairs):
            return location
        location += 1

print(part2_reverse(data))