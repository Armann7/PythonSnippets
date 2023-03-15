"""
Оптимизация пространства интервалов.
Возможные кейсы:
    - интервалы не пересекаются совсем
    - интервалы примыкают друг к другу
    - интервалы пересекаются
        - частный случай - интервал пересекает несколько интервалов
"""
from typing import Tuple


def split(interval, source: list) -> Tuple[list, list]:
    """Делим пространство интервалов - пересекающиеся с interval отдельно, не пересекающиеся отдельно"""
    intersect = []
    non_intersect = []
    A, B = interval[0], interval[1]
    for item in source:
        A1, B1 = item[0], item[1]
        # Если начало или конец одного из интервалов находится внутри другого - значит пересекаются
        if A1 <= A <= B1 or A1 <= B <= B1 or A <= A1 <= B or A <= B1 <= B:
            intersect.append(item)
        # Если интервалы встык - значит пересекаются
        elif abs(A-B1) == 1 or abs(A1-B) == 1:
            intersect.append(item)
        # Если ничего не подошло - значит не пересекаются
        else:
            non_intersect.append(item)

    return intersect, non_intersect


def merge_intersect_intervals(source: list) -> list:
    """Сливаем пересекающиеся интервалы, на выходе - один интервал. Проверки на корректность не выполняем"""
    points = []
    for item in source:
        points.append(item[0])
        points.append(item[1])
    points.sort()
    return [points[0], points[-1]]


def merge(interval, source: list) -> list:
    # Делим пространство интервалов - пересекающиеся отдельно, непересекающиеся отдельно
    intersect, non_intersect = split(interval, source)

    # Пересекающиеся сливаем в один
    if intersect:
        intersect.append(interval)
        interval = merge_intersect_intervals(intersect)

    non_intersect.append(interval)

    return non_intersect


def compress(source: list) -> list:
    """Подход - берем первый интервал и сливаем с ним по очереди остальные"""
    result = [source.pop(0)]
    for interval in source:
        result = merge(interval, result)
    return result


if __name__ == "__main__":
    A = [[1, 3], [4, 6], [5, 8], [12, 17], [20, 23], [6, 9], [22, 25], [13, 15], ]
    print(compress(A))
