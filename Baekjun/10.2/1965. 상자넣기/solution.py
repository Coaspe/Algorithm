from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
dp = []

for a in A:
    idx = bisect_left(dp, a)
    if idx == len(dp):
        dp.append(a)
    else:
        dp[idx] = a

print(len(dp))
