N = int(input())
A = list(map(int, input().split()))

dp = [0] * (max(A) + 1)

for a in A:
    dp[a] = max(dp[a], dp[a - 1] + 1, 1)

print(max(dp))
