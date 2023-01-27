import sys

from bisect import bisect_right
from dataclasses import dataclass

@dataclass
class Params:
    user_limit = 0
    service_limit = 0
    duration = 0


class Journal:

    def __init__(self, params: Params):
        self.users = {}  # {Пользователь: список экспираций}
        self.params = params
        self.total_requests = 0

    def _compress_and_refresh_count(self, time: int):
        self.total_requests = 0
        for user_id, records in self.users.items():
            self.users[user_id] = list(filter(lambda a: a > time, records))
            self.total_requests += len(self.users[user_id])
            # pos = bisect_right(records, time)
            # if pos < len(records):
            #     self.users[user_id] = records[pos:]
            #     self.total_requests += len(self.users[user_id])
            # else:
            #     self.users[user_id].clear()

    def _user_rate(self, user_id: int) -> int:
        records = self.users.get(user_id)
        if records is None:
            return 0
        else:
            return len(records)

    def _user_count(self, time: int, user_id: int):
        record = self.users.get(user_id, [])
        record.append(time + self.params.duration)
        self.users[user_id] = record

    def check(self, time: int, user_id: int) -> int:
        if self._user_rate(user_id) >= self.params.user_limit:
            result = 429
        elif self.total_requests >= self.params.service_limit:
            result = 503
        else:
            self._user_count(time, user_id)
            result = 200

        self._compress_and_refresh_count(time)
        return result


def load_params() -> Params:
    data = Params()
    temp = sys.stdin.readline().strip().split()
    data.user_limit = int(temp[0])
    data.service_limit = int(temp[1])
    data.duration = int(temp[2])
    return data


def load_request():
    temp = sys.stdin.readline().strip()
    if temp == "-1":
        return None
    temp = temp.split()
    return int(temp[0]), int(temp[1])

def main():
    params = load_params()
    journal = Journal(params)

    while True:
        request = load_request()
        if request is None:
            break
        print(journal.check(request[0], request[1]))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
