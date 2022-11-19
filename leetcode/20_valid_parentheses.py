
pairs = {")": "(", "}": "{", "]": "["}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            elif ch in ")}]" and len(stack) > 0:
                if stack[-1] != pairs[ch]:
                    return False
                else:
                    stack.pop()
            else:
                return False

        return len(stack) == 0


if __name__ == "__main__":
    print(Solution().isValid("()"))
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid("(]"))
