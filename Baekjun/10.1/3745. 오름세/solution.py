from bisect import bisect_left
import sys

input = sys.stdin.readline

while True:
    N = input()
    if not N:
        break
    N = int(N)
    A = list(map(int, input().split()))
    dp = []

    for a in A:
        idx = bisect_left(dp, a)
        if idx == len(dp):
            dp.append(a)
        elif idx == 0 or dp[idx - 1] != a:
            dp[idx] = a

    print(len(dp))
