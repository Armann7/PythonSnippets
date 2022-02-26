import sys


def load_from_stdin() -> tuple[int, int, int, int]:
    x = int(sys.stdin.readline().strip())
    y = int(sys.stdin.readline().strip())
    z = int(sys.stdin.readline().strip())
    n = int(sys.stdin.readline().strip())
    return x, y, z, n


def main():
    xc, yc, zc, n = load_from_stdin()
    result = [[x, y, z] for x in range(xc+1) for y in range(yc+1)
              for z in range(zc+1) if x+y+z != n]
    print(result)


if __name__ == "__main__":
    main()
