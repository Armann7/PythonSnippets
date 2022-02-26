import sys
from collections import defaultdict
from functools import reduce


def load_from_stdin() -> str:
    return sys.stdin.readline().strip()


def main():
    name = load_from_stdin()
    chars = list(name)
    chars_dict = defaultdict(int)
    for char in chars:
        chars_dict[char] += 1
    counts_dict = defaultdict(list)
    for k, v in chars_dict.items():
        counts_dict[v].append(k)
    for v in counts_dict.values():
        v.sort()
    data = sorted(counts_dict.items(), key=lambda x: x[0], reverse=True)

    out_line = 0
    for line in data:
        for char in line[1]:
            print(f"{char} {line[0]}")
            out_line += 1
            if out_line == 3:
                return


if __name__ == "__main__":
    main()
