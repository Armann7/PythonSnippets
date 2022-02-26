import sys
from functools import reduce


def load_from_stdin() -> tuple[dict[str: list[float]], str]:
    data = dict()
    lines = int(sys.stdin.readline().strip())
    for line in range(lines):
        vals = sys.stdin.readline().strip().split()
        name = vals.pop(0)
        data[name] = [float(v) for v in vals]
    name_main = sys.stdin.readline().strip()
    return data, name_main


def main():
    data, name = load_from_stdin()
    mean = reduce(lambda a, b: a + b, data[name]) / 3
    print(f"{mean:.2f}")


if __name__ == "__main__":
    main()
