"""
Задача fast track от Яндекса.
Не укладывается по времени - на одном из каких то примеров работает более 1 сек
"""

class Stack:
    def __init__(self):
        self._data = []
        self._elements = {}                 # Элементы и их количества
        self._sorted = None                 # Отсортированный список элементов

    def push(self, v: int):
        self._data.append(v)
        self._elements[v] = self._elements[v] + 1 if v in self._elements else 1
        if self._sorted is None:
            self._sorted = [v]
        elif v > self._sorted[0]:
            self._sorted.insert(0, v)

    def pop(self) -> int:
        v = self._data.pop()
        self._elements[v] = self._elements[v] - 1
        # Если это был последний - выкидываем его
        if v == self._sorted[0] and self._elements[v] == 0:
            self._sorted.pop(0)
        return v

    def max(self) -> int:
        return self._sorted[0]


def load(filename: str) -> list:
    with open(filename, mode="rt", buffering=10000000) as f:
        return f.readlines()


def main(filename: str):
    stack = Stack()
    data = load(filename)
    output = []
    for line in data[1:]:
        # line = line.strip()
        if line[1] == "u":
            value = int(line.strip()[5:])
            stack.push(value)
        elif line[1] == "o":
            stack.pop()
        else: # ops == "max":
            output.append(f"{stack.max()}\n")
    return output


def print_output(data: list):
    for line in data:
        print(line, flush=False)


def output(data: list):
    with open("output.txt", mode="wt", buffering=10000000) as f:
        f.writelines(data)


def test():
    data = main("data/a.input1.txt")
    print_output(data)
    data = main("data/a.input2.txt")
    print_output(data)
    data = main("data/a.input3.txt")
    print_output(data)


# test()
output(main("data/a.input.txt"))
# output(main("input.txt"))
