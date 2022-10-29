import sys


def main(s1: str, s2: str) -> str:
    result = '0'
    if len(s1) != len(s2):
        return result
    if s1 == s2:
        return '1'
    l1 = list(s1)
    l1.sort()
    l2 = list(s2)
    l2.sort()
    if l1 == l2:
        result = '1'
    return result


S1 = sys.stdin.readline().strip()
S2 = sys.stdin.readline().strip()
# S1 = 'ASDFFGSS'
# S2 = 'SGFSFDAS'
print(main(S1, S2))
