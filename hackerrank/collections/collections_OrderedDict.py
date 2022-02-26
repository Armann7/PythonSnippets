import sys
from collections import OrderedDict


def load_from_stdin() -> OrderedDict:
    data = OrderedDict()
    lines = int(sys.stdin.readline().strip())
    for line in range(lines):
        name, price = sys.stdin.readline().strip().rsplit(maxsplit=1)
        name = name.strip()
        price = int(price.strip())
        if name in data.keys():
            data[name] += price
        else:
            data[name] = price
    return data


def main():
    data = load_from_stdin()
    for k, v in data.items():
        print(f"{k} {v}")


if __name__ == "__main__":
    main()
