from bisect import bisect_left
from sys import stdin

input = stdin.readline
T = int(input())

while T:
    T -= 1

    N = int(input())
    dp = [0, 1, 1]

    while True:
        if dp[-1] >= N:
            if dp[-1] > N:
                dp.pop()
            break
        dp.append(dp[-1] + dp[-2])

    ans = []

    while N:
        idx = bisect_left(dp, N)
        if idx == len(dp) or dp[idx] > N:
            idx -= 1
        N -= dp[idx]
        ans.append(dp[idx])

    print(*ans[::-1])
