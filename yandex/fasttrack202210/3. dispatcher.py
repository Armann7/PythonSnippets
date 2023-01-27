import sys

from dataclasses import dataclass
from functools import reduce
from typing import Any, List, Optional


class Queue:
    def __init__(self, number: int):
        self.number = number
        self.elements = []
        self.last_pop_time = 0

    def put(self, element):
        self.elements.append(element)

    def pop(self, time_current: int) -> Any:
        if len(self.elements) > 0:
            self.last_pop_time = time_current
            return self.elements.pop(0)
        else:
            return None

    def is_empty(self) -> bool:
        return len(self.elements) == 0


@dataclass
class Task:
    number: int = 0
    time_start: int = 0
    queue_num: int = 0
    time_work: int = 0
    time_started: int = 0
    worker_num: int = 0


@dataclass
class Worker:
    number: int = 0
    busy_to_time: int = 0
    task: Task = None


@dataclass
class Data:
    queues: List[Queue] = None
    workers: List[Worker] = None
    tasks: List[Task] = None
    pipeline: List[Task] = None


def load() -> Data:
    n, m, k = sys.stdin.readline().strip().split(' ')
    data = Data()
    data.tasks = []
    data.workers = []
    data.queues = []
    for w in range(int(m)):
        data.workers.append(Worker(w + 1))
    for q in range(int(k)):
        data.queues.append(Queue(q + 1))

    tasks = sys.stdin.readlines()
    for num, t in enumerate(tasks):
        time_start, queue_num, time_work = t.strip().split(' ')
        task = Task(num + 1, int(time_start), int(queue_num), int(time_work))
        data.tasks.append(task)

    data.pipeline = data.tasks.copy()
    return data


def dispatch(data: Data, time_current: int) -> bool:
    # Взяли задачу, добавили в очередь
    while len(data.pipeline) > 0 and data.pipeline[0].time_start == time_current:
        task = data.pipeline.pop(0)
        data.queues[task.queue_num - 1].put(task)

    # Ищем исполнителя
    worker = find_worker(data)

    # Ищем очередь откуда взять задачу и загружаем исполнителя
    if worker is not None:
        queues = sorted(data.queues, key=lambda q: (q.is_empty(), q.last_pop_time, q.number))
        task = queues[0].pop(time_current)
        if task is not None:
            worker.task = task
            worker.busy_to_time = time_current + task.time_work - 1  # Занят до ...
            task.worker_num = worker.number
            task.time_started = time_current

    # Пробегаем по исполнителям, ставим статусы
    for w in data.workers:
        if w.busy_to_time == time_current:
            w.busy_to_time = 0
            w.task = None

    # Все очереди пусты?
    if all(map(lambda q: q.is_empty(), data.queues)):
        return False

    return True


def find_worker(data: Data) -> Optional[Worker]:
    for w in data.workers:
        if w.busy_to_time == 0:
            return w
    return None


def main():
    data = load()

    # Стартуем диспетчер
    time_current = 1
    while dispatch(data, time_current):
        time_current += 1

    # Пробегаем по задачам, выводим данные
    for t in data.tasks:
        print(t.worker_num, t.time_started)


if __name__ == "__main__":
    main()
