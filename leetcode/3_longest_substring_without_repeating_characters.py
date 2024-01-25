
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        for no in range(0, len(s)):
            while s[no] in s[left:no]:
                left += 1
            max_length = max(max_length, no - left + 1)
        return max_length


if __name__ == '__main__':
    s = Solution()
    assert s.lengthOfLongestSubstring('abcabcbb') == 3
    assert s.lengthOfLongestSubstring('bbbbb') == 1
    assert s.lengthOfLongestSubstring('pwwkew') == 3
    assert s.lengthOfLongestSubstring('b') == 1
    assert s.lengthOfLongestSubstring('ba') == 2
    assert s.lengthOfLongestSubstring('') == 0
    assert s.lengthOfLongestSubstring('bfw') == 3
    assert s.lengthOfLongestSubstring('aabbbanm') == 4
