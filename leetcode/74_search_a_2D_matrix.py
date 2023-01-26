"""74. Search a 2D Matrix"""
from bisect import bisect_left
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target in (first_col := [line[0] for line in matrix]):
            return True
        line_num = bisect_left(first_col, target) - 1
        pos = bisect_left(matrix[line_num], target)
        if len(matrix[line_num]) <= pos:
            return False
        return matrix[line_num][pos] == target


if __name__ == "__main__":
    assert Solution().searchMatrix([[1,3,5,7], [10,11,16,20],[23,30,34,60]], 3) == True
    assert Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13) == False
    assert Solution().searchMatrix([[1]], 2) == False
    assert Solution().searchMatrix([[1, 1]], 2) == False
