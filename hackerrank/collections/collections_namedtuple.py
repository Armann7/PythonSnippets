import sys


def load_from_stdin() -> float:
    marks_sum = 0.0
    students = int(sys.stdin.readline().strip())
    header = sys.stdin.readline().strip().split()
    marks_index = header.index("MARKS")
    for line in range(students):
        vals = sys.stdin.readline().strip().split()
        marks_sum += float(vals[marks_index])
    return marks_sum / students


def main():
    mean = load_from_stdin()
    print(f"{mean:.2f}")


if __name__ == "__main__":
    main()
