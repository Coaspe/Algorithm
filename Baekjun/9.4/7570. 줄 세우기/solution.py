from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

dp = [0] * (N + 1)
long = 0

for i in range(N):
    num = A[i]
    dp[num] = dp[num - 1] + 1
    long = max(dp[num], long)
print(N - long)
