# BOJ 1806. 부분합 (투 포인터)

import sys

input = sys.stdin.readline

N, S = list(map(int, input().split()))
arr = list(map(int, input().split()))
ans = float("inf")
start, end, s = 0, 0, 0

while end < N:
    if s >= S:
        ans = min(ans, end - start)
        s -= arr[start]
        start += 1
    elif end == N:
        break
    else:
        s += arr[end]
        end += 1

print(ans) if ans != float("inf") else print(0)
