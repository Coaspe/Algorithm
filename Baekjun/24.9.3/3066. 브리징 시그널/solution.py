T = int(input())
from bisect import bisect_left

while T:
    T -= 1
    N = int(input())

    dp = []
    for _ in range(N):
        n = int(input())
        idx = bisect_left(dp, n)

        if idx == len(dp):
            dp.append(n)
        else:
            dp[idx] = n

    print(len(dp))
