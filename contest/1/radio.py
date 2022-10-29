from functools import reduce
from math import sqrt


def load(filename: str):
    towers1 = dict()
    towers2 = dict()
    with open(filename, 'r') as f:
        p, q = f.readline().strip().split(sep=' ')
        for line in range(8):
            x, y = f.readline().strip().split(sep=' ')
            towers1[line+1] = (int(x.strip()), int(y.strip()))
        for line in range(8):
            x, y = f.readline().strip().split(sep=' ')
            towers2[line+1] = (int(x.strip()), int(y.strip()))
    return int(p.strip()), int(q.strip()), towers1, towers2


# Поиск расстояний вышек и заодно минимального
def find_distance(p: int, q: int, towers: dict):
    dist = dict()
    minimal_distance = 999999
    for t in towers:
        distance = sqrt(towers[t][0]**2 + towers[t][1]**2)
        if distance <= p+q:     # Только вышки, покрывающие город
            dist[t] = distance
            if distance < minimal_distance:
                minimal_distance = distance
    return dist, minimal_distance


def main():
    p, q, towers1, towers2 = load('input3.txt')
    dist1, minimal1 = find_distance(p, q, towers1)
    dist2, minimal2 = find_distance(p, q, towers2)

    if minimal1 > p and minimal2 > p or minimal1 == minimal2:
        print(0)
        print(0)
    elif minimal1 < minimal2:
        print(1)
        score = int(reduce(lambda x, t: x + 1 if t < minimal2 else x, dist1.values()), 0)
        print(score)
    elif minimal1 > minimal2:
        print(2)
        score = int(reduce(lambda x, t: x + 1 if t < minimal1 else x + 0, dist2.values(), 0))
        print(score)


main()
