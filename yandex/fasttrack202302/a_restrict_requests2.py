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
    Сохраняем записи в журнал, для каждого запроса проставляем время прибытия
    В конце каждого шага уплотняем журнал, выкидывая просроченные запросы
    """
    def __init__(self, params: Params):
        """
        {Пользователь:  {Время поступления: количество запросов}}
                        {0: количество запросов от пользователя всего}
        """
        self.users = {}
        self.time = {}
        self.params = params
        self.total_requests = 0
        self.last_handled_expire_time = 0
        self.lifecycle_clear = 0

    def _compress_and_refresh_total(self, time: int) -> None:
        self.lifecycle_clear += 1

        current_expire_time = time - self.params.duration - 1
        if current_expire_time <= 0:
            return

        expired_records = {t: u for t, u in self.time.items() if self.last_handled_expire_time < t <= current_expire_time}

        # Посчитаем рейты
        for expired_time, users in expired_records.items():
            for user in users:
                self.total_requests = self.total_requests - self.users[user][expired_time]
                self.users[user][0] = self.users[user][0] - self.users[user][expired_time]

        # Зачистим просроченные записи
        # if self.lifecycle_clear >= 100:
        #     expired_records2 = {t: u for t, u in self.time.items() if t <= self.last_handled_expire_time}
        #     for expired_time, users in expired_records.items():
        #         del self.time[expired_time]
        #         for user in users:
        #             del self.users[user][expired_time]
        #     for expired_time, users in expired_records2.items():
        #         del self.time[expired_time]
        #         for user in users:
        #             del self.users[user][expired_time]
        #     self.lifecycle_clear = 0

        # Пометим время обработки
        self.last_handled_expire_time = current_expire_time

    def _user_requests(self, user_id: int) -> int:
        requests = self.users.get(user_id)
        return requests[0] if requests is not None else 0

    def _add_request(self, time: int, user_id: int) -> None:
        if user_id not in self.users:
            self.users[user_id] = defaultdict(int)
        self.users[user_id][time] += 1
        self.users[user_id][0] += 1
        self.total_requests += 1

        if time not in self.time:
            self.time[time] = {user_id}
        else:
            self.time[time].add(user_id)

    def check(self, time: int, user_id: int) -> int:
        self._compress_and_refresh_total(time)

        if self._user_requests(user_id) >= self.params.user_limit:
            result = 429
        elif self.total_requests >= self.params.service_limit:
            result = 503
        else:
            self._add_request(time, user_id)
            result = 200

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
    gate = Gate(params)
    while True:
        request = load_request()
        if request is None:
            break
        print(gate.check(request[0], request[1]))
        sys.stdout.flush()


if __name__ == "__main__":
    main()
