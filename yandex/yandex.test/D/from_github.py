import sys
n = int(sys.stdin.readline().strip())
# n = 11

def foo(s, l, r, pairs):
    if l == pairs and r == pairs:
        print(s)
    else:
        if l < pairs:
            foo(s + '(', l + 1, r, pairs)
        if r < l:
            foo(s + ')', l, r + 1, pairs)


foo('', 0, 0, n)
