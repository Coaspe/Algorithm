from sys import stdin

input = stdin.readline
d, n, m = map(int, input().split())

A = sorted([int(input()) for _ in range(n)])


def check(gap):
    lm = m
    s = 0
    removed = set()

    for a in A:
        if a - s < gap:
            lm -= 1
            if lm < 0:
                return False
            removed.add(a)
        else:
            s = a

    s = d
    for i in range(len(A) - 1, -1, -1):
        if A[i] in removed:
            continue

        if s - A[i] < gap:
            lm -= 1
            if lm < 0:
                return False
        else:
            return True


l, r = -1, d + 1

while r > l + 1:
    mid = (l + r) // 2
    if check(mid):
        l = mid
    else:
        r = mid

if m == n:
    l = d

print(l)
