import sys


def load_from_stdin() -> list[list]:
    data = list()
    cases = int(sys.stdin.readline().strip())
    for c in range(cases):
        numbers = int(sys.stdin.readline().strip())
        cubes = sys.stdin.readline().strip().split()
        cubes = list(map(lambda x: int(x.strip()), cubes))
        data.append(cubes)
    return data


def main():
    data = load_from_stdin()
    for line in data:
        top_cube = 2**31
        for num in range(len(line)):
            if line[0] >= line[-1] and top_cube > 0:
                if line[0] <= top_cube:
                    top_cube = line.pop(0)
                else:
                    top_cube = -1
            elif line[-1] > line[0] and top_cube > 0:
                if line[-1] <= top_cube:
                    top_cube = line.pop(-1)
                else:
                    top_cube = -1
            if top_cube < 0:
                print("No")
                break
        if top_cube >= 0:
            print("Yes")


if __name__ == "__main__":
    main()
