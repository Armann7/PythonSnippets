import functools


def process(x, y):
    if 'current_ratio' not in process.__dict__:
        process.current_ratio = 0
        if x == 1:
            process.current_ratio = 1
        x = 0

    process.current_ratio = 0 if y != 1 else process.current_ratio+1
    x = process.current_ratio if process.current_ratio > x else x
    return x


with open("input.txt", "r") as f:
    data = f.readlines()

count = int(data[0])
if count > 0:
    data = [int(num) for num in data[1:count]]
    res = functools.reduce(process, data)

    with open("output.txt", "w") as f:
        f.write(str(res))
