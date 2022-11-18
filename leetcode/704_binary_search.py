from typing import List, Optional


class Solution:
    def search(self, nums: List[int], target: int, start_index: int = 0) -> Optional[int]:
        if nums[0] == target:
            return start_index

        if len(nums) == 1:
            return -1

        half_index = int(len(nums) / 2)
        if nums[half_index] == target:
            return start_index + half_index
        if nums[half_index] > target:
            return self.search(nums[:half_index], target, start_index)
        if nums[half_index] < target:
            return self.search(nums[half_index:], target, start_index + half_index)


if __name__ == "__main__":
    print(Solution().search([-1, 0, 3, 5, 9, 12], 9))
    print(Solution().search([-1, 0, 3, 5, 9, 12], 2))
