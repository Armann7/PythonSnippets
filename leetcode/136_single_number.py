from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        for i in range(1, len(nums), 2):
            if nums[i-1] != nums[i]:
                return nums[i - 1]
        return nums[-1]


if __name__ == "__main__":
    print(Solution().singleNumber([2, 2, 1]))
    print(Solution().singleNumber([4, 1, 2, 1, 2]))
    print(Solution().singleNumber([1]))
