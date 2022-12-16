from collections import deque
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if s == "":
            return []
        # Отбросим ) слева и ( справа - они бесполезны
        s = s.lstrip(")").rstrip("(")

        result = set()
        max_len = -1
        # Генерируем варианты последовательностей и проверяем их
        for item in self.gen(s):
            if self.check(item):
                if max_len < 0:
                    max_len = len(item)
                if len(item) < max_len:
                    break
                result.add(item)

        if len(result) == 0:
            return [s.replace("(", '').replace(")", '')]
        return list(result)

    @staticmethod
    def gen(s: str) -> str:
        q = deque()
        q.append(s)
        if s.count("(") == s.count(")"):
            yield s
        try:
            while True:
                s = q.popleft()
                for pos, ch in enumerate(s):
                    if ch in "()":
                        if pos > 0 and s[pos-1] == ch:
                            continue
                        s1 = s[:pos] + s[pos + 1:]
                        delta_bracket = abs(s1.count("(") - s1.count(")"))
                        # if delta_bracket <= 1:
                        q.append(s1)
                        if delta_bracket == 0:
                            yield s1
        except IndexError:
            ...

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
            elif ch == ")" and len(stack) > 0:
                if stack[-1] != "(":
                    return False
                else:
                    stack.pop()
            else:
                return False
        return len(stack) == 0


if __name__ == "__main__":
    print(Solution().removeInvalidParentheses("()())()"))
    print(Solution().removeInvalidParentheses("(a)())()"))
    print(Solution().removeInvalidParentheses(")("))
    print(Solution().removeInvalidParentheses("()"))
    print(Solution().removeInvalidParentheses(")()("))
    print(Solution().removeInvalidParentheses(""))
    print(Solution().removeInvalidParentheses("))()()p"))
    print(Solution().removeInvalidParentheses("(j))("))
    print(Solution().removeInvalidParentheses("()(()(("))
    print(Solution().removeInvalidParentheses("()((((()"))
    print(Solution().removeInvalidParentheses("()(((((((()"))
    # print(Solution().removeInvalidParentheses(")k)))())()())))())"))
