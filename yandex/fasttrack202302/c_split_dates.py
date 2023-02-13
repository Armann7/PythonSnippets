import calendar
import sys

from dataclasses import dataclass
from datetime import date, timedelta


QUARTER_FINISH = {0: (3, 31), 1: (6, 30), 2: (9, 30), 3: (12, 31)}


@dataclass
class Data:
    type: str = ""
    start: date = None
    finish: date = None


def load() -> Data:
    data = Data()
    data.type = sys.stdin.readline().strip()
    date1, date2 = sys.stdin.readline().strip().split(" ")
    y, m, d = date1.strip().split("-")
    data.start = date(int(y), int(m), int(d))
    y, m, d = date2.strip().split("-")
    data.finish = date(int(y), int(m), int(d))
    return data


def output_date(dt: date) -> str:
    return "{:%Y-%m-%d}".format(dt)


def find_end_period(data: Data, dt: date) -> date:
    if data.type == "WEEK":
        day_diff = 6 - dt.weekday()
        result = dt + timedelta(days=day_diff)

    elif data.type == "MONTH":
        day = calendar.monthrange(dt.year, dt.month)[1]
        result = date(dt.year, dt.month, day)

    elif data.type == "QUARTER":
        q = (dt.month - 1) // 3
        result = date(dt.year, QUARTER_FINISH[q][0], QUARTER_FINISH[q][1])

    elif data.type == "YEAR":
        result = date(dt.year, 12, 31)

    elif data.type == "REVIEW":
        if 4 <= dt.month <= 9:
            result = date(dt.year, 9, 30)
        else:
            result = date(dt.year + 1, 3, 31)

    return result if result < data.finish else data.finish


def next_period(dt: date) -> date:
    return dt + timedelta(days=1)


def periods(data: Data) -> list:
    result = list()

    start_period = data.start
    while start_period <= data.finish:
        # Определяем конец периода
        end_period = find_end_period(data, start_period)
        # Добавляем в список периодов. Корректируем окончание для последнего периода
        result.append(f"{output_date(start_period)} {end_period}")
        # Определяем начало следующего периода
        start_period = next_period(end_period)
    return result


def main():
    data = load()
    dates = periods(data)
    print(len(dates))
    for line in dates:
        print(line)


if __name__ == "__main__":
    main()
