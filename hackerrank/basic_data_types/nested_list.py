import sys
# from functools import filter


def load_from_stdin() -> list[tuple[str, float]]:
    data: list[tuple[str, float]] = []
    lines = int(sys.stdin.readline().strip())
    for line in range(lines):
        name = sys.stdin.readline().strip()
        score = float(sys.stdin.readline().strip())
        data.append((name, score))
    return data


def main():
    data = load_from_stdin()
    data.sort()
    scores = list(set([line[1] for line in data]))
    scores.sort()
    for line in data:
        if line[1] == scores[1]:
            print(line[0])


if __name__ == "__main__":
    main()
