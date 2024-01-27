# Solution from LeetCode

class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


if __name__ == '__main__':
    s = Solution()
    assert s.largestNumber([10, 2]) == '210'
    assert s.largestNumber([3, 30, 34, 5, 9]) == '9534330'
    assert s.largestNumber([3]) == '3'
    assert s.largestNumber([0]) == '0'
    assert s.largestNumber([33, 18, 2]) == '33218'
    assert s.largestNumber([9, 1, 20, 15]) == '920151'
    assert s.largestNumber([111311, 1113]) == '1113111311'
    assert s.largestNumber([0, 0]) == '0'
    assert s.largestNumber([74, 21, 33, 51, 77, 51, 90, 60, 5, 56]) == '9077746056551513321'
    assert s.largestNumber([9, 1, 20, 20, 20, 20, 15]) == '920202020151'
    assert s.largestNumber([66,8,33,1,72,93,51,88,59,86,66,39,71,82,95,77,44,75,91,4,52,28,20,73,74,91,87,82,94,12,69,13,22,18,45,68,97,65,4,86,44,32,36,96,88,11,21,8,14,4,67,40,57,90,84,27,42,9,39,14,11,79,68,49,1,51,91,56,35,10,22,99,23,8,76,32,46,40,37,43,89,83,91,40,94,43,62,74,8,42,99,7,34,67,39,55,22,87,73,91]) == '999999796959494939191919191908988888888878786868483828279777767574747373727169686867676666656259575655525151494645444444443434242404040393939373635343332322827232222222120181414131211111110'
