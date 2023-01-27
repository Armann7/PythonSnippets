import math
import sys

from dataclasses import dataclass
from functools import reduce


@dataclass
class Data:
    width: int = 0
    count_photos: int = 0
    feed_photos: int = 0
    photos: list = None


def load() -> Data:
    data = Data()
    data.width = int(sys.stdin.readline().strip())
    n, k = sys.stdin.readline().strip().split(' ')
    data.count_photos = int(n)
    data.feed_photos = int(k)
    data.photos = []
    photos = sys.stdin.readlines()
    for p in photos:
        w, h = p.strip().split('x')
        data.photos.append((int(w), int(h)))
    return data


def main():
    data = load()
    heights = []
    for w, h in data.photos:
        h_new = math.ceil(h * data.width / w)
        heights.append(h_new)

    heights.sort()
    min_height = reduce(lambda h1, h2: h1 + h2, heights[0:data.feed_photos])
    print(min_height)
    heights.sort(reverse=True)
    max_height = reduce(lambda h1, h2: h1 + h2, heights[0:data.feed_photos])
    print(max_height)


if __name__ == "__main__":
    main()
