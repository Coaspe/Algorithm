from sys import stdin
from math import ceil

input = stdin.readline
N, M = map(int, input().split())

A = list(int(input()) for _ in range(M))

if M == N:
    print(max(A))
    exit(0)


def check(T):
    cnt = 0
    for a in A:
        cnt += ceil(a / T)
    return N >= cnt


maxA = max(A)
l, r = 1, maxA + 1

while r > l + 1:
    mid = (l + r) // 2

    if check(mid):
        r = mid
    else:
        l = mid

print(r)
