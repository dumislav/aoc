import sys
import math

def distance(p1: tuple[int, int, int], p2: tuple[int, int, int]) -> float:
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)

def solve(items: list[tuple[int, int, int]]) -> int:
    key = 0
    distances = {}
    connected = {}
    for item, coord in enumerate(items):
        for item2, coord2 in enumerate(items):
            if item != item2:
                if (item2, item) not in distances:
                    distances[(item, item2)] = distance(coord, coord2)

    num = 0
    circuit_size = {}
    last_connected = ()
    for (item1, item2), _ in sorted(distances.items(), key=lambda x: x[1]):
        if item1 not in connected and item2 not in connected:
            connected[item1] = key
            connected[item2] = key
            print(f"Connecting {items[item1]} and {items[item2]} into NEW circuit {key}")
            key += 1
        elif item1 not in connected and item2 in connected:
            last_connected = (item2, item1)
            connected[item1] = connected[item2]
            print(f"Connecting {items[item1]} to {items[item2]} ({connected[item2]})")
        elif item1 in connected and item2 not in connected:
            last_connected = (item2, item1)
            connected[item2] = connected[item1]
            print(f"Connecting {items[item2]} to {items[item1]} ({connected[item1]})")
        elif item1 in connected and item2 in connected:
            if connected[item1] != connected[item2]:
                last_connected = (item2, item1)
                old_circuit = connected[item2]
                new_circuit = connected[item1]
                for k, v in connected.items():
                    if v == old_circuit:
                        connected[k] = new_circuit
                print(f"Merging circuits {old_circuit} and {new_circuit} by connecting {items[item1]} and {items[item2]}")
        num += 1
#        if num == 1000:
#            break

    print(f"Number of connections made: {num}")
    circuit_size = {}
    for item, circuit in connected.items():
        circuit_size[circuit] = circuit_size.get(circuit, 0) + 1

    circuit_size = sorted(circuit_size.values(), reverse=True)[:3]
    print(circuit_size)
    res = 1
    for i in circuit_size:
        res *= i

    print(res)
    print(f"Last connected pair: {last_connected} with coordinates {items[last_connected[0]]} and {items[last_connected[1]]}")
    res2 =items[last_connected[0]][0]*items[last_connected[1]][0]
    print(res2)

def main():
    data = sys.stdin.read().split('\n')
    items = [tuple(map(int, x.split(','))) for x in data if x]
    solve(items)

if __name__ == '__main__':
    main()