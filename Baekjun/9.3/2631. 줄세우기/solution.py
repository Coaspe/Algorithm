import bisect

N = int(input())
A = [int(input()) for _ in range(N)]

dp = []

for a in A:
    if not dp:
        dp.append(a)
    else:
        idx = bisect.bisect_left(dp, a)
        if idx == len(dp):
            dp.append(a)
        else:
            dp[idx] = a

print(N - len(dp))
