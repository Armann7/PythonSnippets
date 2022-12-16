from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:  # no_qa
        if s == "":
            return []
        # Отбросим ) слева и ( справа - они бесполезны
        s = self.strip(s)

        left_p = s.count("(")
        right_p = s.count(")")

        # result = self.find(s)
        # return result

    @classmethod
    def check(cls, s: str) -> bool:
        if "(" not in s and ")" not in s:
            return False

        stack = []
        for ch in s:
            if ch not in "()":
                continue
            elif ch == "(":
                stack.append(ch)
            elif ch == ")" and stack:
                if stack[-1] != "(":
                    return False
                else:
                    stack.pop()
            else:
                return False
        return len(stack) == 0

    @classmethod
    def strip(cls, s: str) -> str:
        """Отбросим ) слева и ( справа - они бесполезны"""
        s = s.lstrip(")").rstrip("(")
        for num, ch in enumerate(s):
            if ch == "(":
                break
            if ch == ")":
                s[num] = " "
        for num in range(len(s)):
            ch = s[-num - 1]
            if ch == ")":
                break
            if ch == "(":
                s[-num - 1] = " "
        return s.replace(" ", "")


if __name__ == "__main__":
    print(Solution().removeInvalidParentheses("()())()"))
    # print(Solution().removeInvalidParentheses(")k)))())()())))())"))
