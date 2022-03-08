import sys
from collections import Counter


def load_from_stdin() -> tuple[int, str]:
    s = sys.stdin.readline().strip()
    k = int(sys.stdin.readline().strip())
    return k, s


def substring(s: str, k: int) -> str:
    """
    Generator. Return a substring of s
    """
    for pos in range(0, len(s), k):
        # Reverse a substring
        substr = s[pos:pos + k]
        substr = substr[::-1]
        # Remove all chars except one
        for char, count in Counter(substr).items():
            if count > 1:
                substr = substr.replace(char, '', count-1)
        # Reverse back and return
        yield substr[::-1]


def merge_the_tools(string: str, k: int):
    [print(substr) for substr in substring(string, k)]


if __name__ == "__main__":
    k, string = load_from_stdin()
    merge_the_tools(string, k)
