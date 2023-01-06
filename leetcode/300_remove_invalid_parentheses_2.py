from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:  # no_qa
        if s == "":
            return set()
        # Отбросим ) слева и ( справа - они бесполезны
        s = self.strip(s)

        # left_count, right_count = s.count("("), s.count(")")
        # char = "(" if left_count > right_count else ")"
        # # char = "" if count_p == 0 else char
        #
        # if left_count == 0 and right_count == 0:
        #     result = {s}
        # elif left_count == right_count:
        #     result = {s} if self.check(s) else set()
        # else:
        #     result = self.find(s, char, abs(left_count - right_count), set())
        result = self.find(s, set())
        return list(result) if result else [""]

    @classmethod
    def find(cls, s: str, strings: set) -> set:
        result_str = ""
        pos = 0
        while pos < len(s):
            if s[pos] == ")":
                pass
            elif s[pos] == "(":
                pos_r = s.find(")", pos)
                if pos_r > -1:
                    result_str = result_str + s[pos] + s[pos+1:pos_r+1].replace("(", "")
                    pos = pos_r
            else:
                result_str += s[pos]
            pos += 1
        if result_str and result_str not in strings:
            strings.add(result_str)
        return strings

    @classmethod
    def find_old(cls, s: str, char: str, count: int, strings: set) -> set:
        for pos, ch in enumerate(s):
            if ch == char:
                new_s = s[:pos] + s[pos+1:]
                if count == 1:
                    if cls.check(new_s) and new_s not in strings:
                        strings.add(new_s)
                else:
                    strings = cls.find_old(new_s, char, count - 1, strings)
        return strings

    @classmethod
    def check(cls, s: str) -> bool:
        if "(" not in s and ")" not in s:
            return True

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
        brackets = s[:s.find("(")].count(")")
        if brackets > 0:
            s = s.replace(")", "", brackets)
        pos = s.rfind(")")
        brackets = s[pos+1:].count("(")
        if brackets > 0:
            s = s[:pos+1] + s[pos+1:].replace("(", "", brackets)
        return s


if __name__ == "__main__":
    # print(Solution().removeInvalidParentheses("()())()"))
    # print(Solution().removeInvalidParentheses(")k)))())()())))())"))
    # print(Solution().removeInvalidParentheses("n"))
    # print(Solution().removeInvalidParentheses(")d))"))
    print(Solution().removeInvalidParentheses("())(((()m)("))
