import sys

from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Params:
    user_limit = 0
    service_limit = 0
    duration = 0


class Gate:
    """
    Сохраняем записи в журнал, для каждого запроса проставляем время экспирации
    В конце каждого шага уплотняем журнал, выкидывая просроченные запросы
    """

    def __init__(self, params: Params):
        """
        {Пользователь:  {Время экспирации: количество запросов}}
                        {0: количество запросов от пользователя всего}
        """
        self.users = {}
        self.params = params
        self.total_requests = 0

    def _compress_and_refresh_total(self, time: int):
        for user_id, requests in self.users.items():
            # Удалим просроченные записи
            if time in requests:
                self.total_requests = self.total_requests - requests[time]
                requests[0] = requests[0] - requests[time]
                requests[time] = 0

    def _user_rate(self, user_id: int) -> int:
        records = self.users.get(user_id)
        return records[0] if records is not None else 0

    def _user_count(self, time: int, user_id: int):
        if user_id not in self.users:
            self.users[user_id] = defaultdict(int)
        self.users[user_id][time + self.params.duration] += 1
        self.users[user_id][0] += 1
        self.total_requests += 1

    def check(self, time: int, user_id: int) -> int:
        if self._user_rate(user_id) >= self.params.user_limit:
            result = 429
        elif self.total_requests >= self.params.service_limit:
            result = 503
        else:
            self._user_count(time, user_id)
            result = 200

        self._compress_and_refresh_total(time)
        return result


def load_params() -> Params:
    data = Params()
    temp = sys.stdin.readline().strip().split()
    data.user_limit = int(temp[0].strip())
    data.service_limit = int(temp[1].strip())
    data.duration = int(temp[2].strip())
    return data


def load_request():
    temp = sys.stdin.readline().strip()
    if temp == "-1":
        return None
    temp = temp.split()
    return int(temp[0]), int(temp[1])


def main():
    params = load_params()
    journal = Gate(params)
    while True:
        request = load_request()
        if request is None:
            break
        print(journal.check(request[0], request[1]))
        sys.stdout.flush()


if __name__ == "__main__":
    main()
