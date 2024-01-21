from typing import List


class Vertex:
    def __init__(self, no: int, money: int):
        self.no = no
        self.money = money
        self.neighbors: List[Vertex] = []
        self.max_money = money

    def __repr__(self):
        neighbors = '[' + ' '.join([str(n.no) for n in self.neighbors]) + ']'
        return f'{self.no} {neighbors} {self.money}  {self.max_money}'


class Solution:
    def rob(self, nums: List[int]) -> int:
        vertices: List[Vertex] = []
        for i, money in enumerate(nums):
            vertices.append(Vertex(i + 1, money))
        for i, v in enumerate(vertices):
            if i + 2 < len(vertices):
                v.neighbors.append(vertices[i + 2])
            else:
                break
            if i + 3 < len(vertices):
                v.neighbors.append(vertices[i + 3])
        for v in vertices:
            for n in v.neighbors:
                money = v.max_money + n.money
                if money > n.max_money:
                    n.max_money = money
        return max(vertices, key=lambda x: x.max_money).max_money


if __name__ == '__main__':
    s = Solution()
    assert s.rob([1, 2, 3, 1]) == 4
    assert s.rob([2, 7, 9, 3, 1]) == 12
