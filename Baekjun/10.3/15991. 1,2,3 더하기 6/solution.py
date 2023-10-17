import sys

input = sys.stdin.readline

dp = [1, 1, 2, 2, 3, 3]
for i in range(6, 100001):
    dp.append((dp[i - 2] + dp[i - 4] + dp[i - 6]) % 1000000009)

for _ in range(int(input())):
    n = int(input())
    print(dp[n])
