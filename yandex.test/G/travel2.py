from dataclasses import dataclass


def load(filename: str):
    towns = dict()
    with open(filename, 'r') as f:
        num_towns = int(f.readline().strip())
        for i in range(1, num_towns+1):
            (x, y) = f.readline().strip().split(sep=' ')
            towns[i] = (int(x), int(y))
        max_dist = int(f.readline().strip())
        (town_from, town_to) = f.readline().strip().split(sep=' ')

    return num_towns, towns, max_dist, int(town_from), int(town_to)


def calc_dist(towns: dict, max_dist: int) -> dict:
    dist = dict()
    for town1, coord1 in towns.items():
        for town2, coord2 in towns.items():
            if town1 != town2:
                distance = abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])
                if distance <= max_dist:
                    if town1 > town2:
                        town1, town2 = town2, town1
                    if (town1, town2) not in dist:
                        dist[(town1, town2)] = distance
    return dist


def find_path(towns: dict, dist: dict, town_from: int, town_to: int):
    visited = set()
    routes = list()
    route = list()
    route.append((town_from, 0))

    while True:
        for


    # for d in dist:
    #     if d[0] in (town_from, town_to) and d[1] in (town_from, town_to):
    #         return d[2]
    #     if town_from in (d[0], d[1]):


def main(filename: str) -> int:
    num_towns, towns, max_dist, town_from, town_to = load(filename)
    dist = calc_dist(towns, max_dist)
    if not len(dist):
        return -1

    print(dist)


main('input.txt')
