
def load(filename: str):
    with open(filename, 'r') as f:
        count_books = int(f.readline().strip())
        times = f.readline().strip().split(' ')
        times = list(map(int, times))
    return count_books, times


def min_max(count_books: int, times: list):
    all_time = 0
    neg = 0
    for t in times:
        if t < 0:
            neg += 1
        all_time += abs(t)

    if neg > 0:
        neg -= 1
    v = (count_books - neg) / float(count_books)
    return all_time, v


def main():
    count_books, times = load('input2.txt')
    all_time, v = min_max(count_books, times)
    mo = 0
    for t in times:
        mo += abs(t) * v
    # mo = mo / count_books
    print(mo)


main()
