import sys
from collections import OrderedDict


def load_from_stdin() -> OrderedDict:
    data = OrderedDict()
    lines = int(sys.stdin.readline().strip())
    for line in range(lines):
        word = sys.stdin.readline().strip()
        if word in data.keys():
            data[word] += 1
        else:
            data[word] = 1
    return data


def main():
    data = load_from_stdin()
    print(len(data))
    for count in data.values():
        print(f"{count}", end=" ")


if __name__ == "__main__":
    main()
