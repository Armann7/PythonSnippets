from dataclasses import dataclass
from typing import Dict, List, Optional, Set

Grid = List[List[str]]
Vertices = Dict[int, Set]


@dataclass
class Point:
    x: int = -1
    y: int = -1


class Solution:
    def numIslands(self, grid: Grid) -> int:
        used_vertices: Vertices = {}
        width = len(grid[0])
        height = len(grid)
        all_islands = 0

        for y in range(height):
            for x in range(width):
                if (island := self.find_island(grid, x, y, used_vertices)) is not None:
                    all_islands += 1

        return all_islands

    def find_island(self, grid: Grid, x: int, y: int, used_vertices: Vertices) -> Optional[Vertices]:
        if y not in used_vertices:
            used_vertices[y] = set()
        if x in used_vertices[y]:
            return None
        used_vertices[y].add(x)
        if grid[y][x] == "0":
            return None

        island: Vertices = {}
        visited: List[Point] = []
        island[y] = {x}
        visited.append(Point(x, y))

        while len(visited) > 0:
            point = visited.pop(0)
            self.use_vertice(point.x + 1, point.y, grid, used_vertices, island, visited)
            self.use_vertice(point.x - 1, point.y, grid, used_vertices, island, visited)
            self.use_vertice(point.x, point.y + 1, grid, used_vertices, island, visited)
            self.use_vertice(point.x, point.y - 1, grid, used_vertices, island, visited)
        return island

    @staticmethod
    def use_vertice(x: int, y: int, grid: Grid, used_vertices: Vertices, island: Vertices, visited: List):
        if x >= len(grid[0]) or y >= len(grid) or x < 0 or y < 0:
            return
        if y not in used_vertices:
            used_vertices[y] = set()
        if y not in island:
            island[y] = set()
        if x in used_vertices[y]:
            return

        used_vertices[y].add(x)
        if grid[y][x] == "1":
            island[y].add(x)
            visited.append(Point(x, y))


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    print(Solution().numIslands(grid))

    grid = [
      ["1", "1", "0", "0", "0"],
      ["1", "1", "0", "0", "0"],
      ["0", "0", "1", "0", "0"],
      ["0", "0", "0", "1", "1"]
    ]
    print(Solution().numIslands(grid))
