import sys


def load_from_stdin() -> list[int]:
    n = int(sys.stdin.readline().strip())
    scores = sys.stdin.readline().strip().split()
    return [int(s) for s in scores]


def main():
    scores = load_from_stdin()
    scores = sorted(scores, reverse=True)
    max_score = scores[0]
    for score in scores:
        if score != max_score:
            print(score)
            return


if __name__ == "__main__":
    main()
