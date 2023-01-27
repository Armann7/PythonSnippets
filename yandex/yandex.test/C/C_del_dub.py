import sys


count = int(sys.stdin.readline())
if count > 0:
    last_num = None
    for pos in range(count):
        current_num = int(sys.stdin.readline())
        if last_num is not None and last_num != current_num:
            print(last_num)
        last_num = current_num
    print(last_num)
