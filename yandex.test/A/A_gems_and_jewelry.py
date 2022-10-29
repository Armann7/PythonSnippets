import sys

J = sys.stdin.readline().strip()
S = sys.stdin.readline().strip()

res = [ch for ch in list(S) if ch in set(J)]
print(len(res))
