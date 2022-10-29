import sys


def main(n: int):
    count_bits = n * 2 - 2
    count_bits_half = n - 1

    number_start = '0b' + '0' * count_bits_half + '1' * count_bits_half
    number_start = int(number_start, 2)
    number_last = '0b' + '1' * count_bits_half + '0' * count_bits_half
    number_last = int(number_last, 2)
    result = list()

    for num in range(number_start, number_last + 1):
        numb = f"{num:b}"
        if numb.count('1') == count_bits_half:
            brackets = count_bits + 1 - len(numb)
            for ch in numb:
                brackets = brackets+1 if ch == '0' else brackets-1
                if brackets < 0:
                    break
            if brackets == 1:
                numb = f'({numb.zfill(count_bits)})'
                s = numb.translate(str.maketrans('01', '()'))
                result.append(s)
    # result.sort()
    return result


# count = int(sys.stdin.readline().strip())
count = 11

if count < 0:
    pass
elif count == 0:
    print("")
elif count == 1:
    print("()")
else:
    # res = main(count)
    for r in main(count):
        print(r)

