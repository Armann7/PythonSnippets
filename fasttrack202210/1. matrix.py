def is_white(line: int, col: int, columns: int) -> bool:
    if (line*columns + col) % 2 == 1:
        return True
    return False


def generate(size: int) -> None:
    black = 0
    for line in range(size):
        for col in range(size):
            if line == col:
                print(0, end=' ')
            elif is_white(line, col, size):
                white_no = int((line * size + col + 1) / 2)
                print(white_no, end=' ')
            else:
                compensator = col - 1 if line < col else col
                black_no = -int((col * size + line) / 2 - compensator)
                print(black_no, end=' ')
        print('')


def main():
    n = int(input())
    generate(n * 2 + 1)


if __name__ == "__main__":
    main()
