
class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighborhoods = dict()


class Route:
    def __init__(self, current_town, distance, steps):
        self.current_town = current_town
        self.distance = distance
        self.steps = steps


def load(filename: str):
    towns = dict()
    with open(filename, 'r') as f:
        data = f.readlines()
    num_towns = int(data.pop(0).strip())
    for i in range(1, num_towns+1):
        (x, y) = data.pop(0).strip().split(sep=' ')
        towns[i] = City(int(x), int(y))
    max_dist = data.pop(0).strip()
    (town_from, town_to) = data.pop(0).strip().split(sep=' ')
    return num_towns, towns, int(max_dist), int(town_from), int(town_to)


def calc_dist(towns: dict, max_dist: int):
    for town1 in towns:
        for town2 in towns:
            if town1 != town2:
                distance = abs(float(towns[town1].x) - towns[town2].x) + abs(float(towns[town1].y) - towns[town2].y)
                if distance <= max_dist:
                    towns[town2].neighborhoods[town1] = distance
                    towns[town1].neighborhoods[town2] = distance


def find_path(towns: dict, town_from: int, town_to: int):
    visited = {town_from}
    route = Route(town_from, 0, 0)
    routes = list()
    routes.append(route)
    finish_routes = list()
    while routes:
        # Обходим роуты
        for route in routes:
            # Определяем следующие города, формируем новые роуты
            new_routes = list()
            for next_town, distance in towns[route.current_town].neighborhoods.items():
                if next_town not in visited:
                    new_route = Route(next_town, route.distance + distance, route.steps + 1)
                    if next_town == town_to:
                        finish_routes.append(new_route)
                    else:
                        new_routes.append(new_route)
            visited.update(towns[route.current_town].neighborhoods.keys())
        routes = new_routes
    return finish_routes


def main(filename: str) -> int:
    num_towns, towns, max_dist, town_from, town_to = load(filename)
    calc_dist(towns, max_dist)
    routes = find_path(towns, town_from, town_to)
    routes.sort(key=lambda r: r.steps)
    if routes:
        return routes[0].steps
    else:
        return -1


print(main('input.txt'))
