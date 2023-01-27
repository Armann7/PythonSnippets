import sys


def process(x, y):
    if 'current_ratio' not in process.__dict__:
        process.current_ratio = 0
        if x == 1:
            process.current_ratio = 1
        x = 0

    process.current_ratio = 0 if y != 1 else process.current_ratio+1
    x = process.current_ratio if process.current_ratio > x else x
    return x


count = int(sys.stdin.readline())
maxnum = 0
for num in range(count):
    line = int(sys.stdin.readline())
    maxnum = process(maxnum, line)
print(maxnum)
