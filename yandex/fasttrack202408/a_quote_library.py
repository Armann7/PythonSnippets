import sys


class Gate:

    def __init__(self, max_rate: int):
        self._max_rate = max_rate
        self._users = {}

    def add_request(self, timestamp: int, token: str) -> bool:
        if token not in self._users:
            self._users[token] = [timestamp]
            return True
        while True:
            if self._users[token] and timestamp - self._users[token][0] >= 1000:
                self._users[token].pop(0)
            else:
                break
        if len(self._users[token]) + 1 > self._max_rate:
            return False
        self._users[token].append(timestamp)
        return True


def load_params() -> tuple[int, int]:
    header_data = sys.stdin.readline().strip().split()
    max_rate = int(header_data[0].strip())
    count_lines = int(header_data[1].strip())
    return max_rate, count_lines


def feed(count_lines: int):
    for _ in range(count_lines):
        data = sys.stdin.readline().strip().split()
        timestamp = int(data[0].strip())
        token = data[1].strip()
        yield timestamp, token


def main():
    max_rate, count_lines = load_params()
    gate = Gate(max_rate)
    for timestamp, token in feed(count_lines):
        if gate.add_request(timestamp, token):
            print(timestamp, token)


if __name__ == "__main__":
    main()
