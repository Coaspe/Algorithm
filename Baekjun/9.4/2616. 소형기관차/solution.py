N = int(input())
A = list(map(int, input().split()))

for i in range(1, N):
    A[i] += A[i - 1]

A.insert(0, 0)
M = int(input())

# 길이가 M인 합이 가장 큰 연속된 수열 3개를 찾으면 된다.
dp = [[0] * (N + 1) for _ in range(4)]

for i in range(1, 4):
    for j in range(i * M, N + 1):
        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - M] + A[j] - A[j - M])

print(dp[-1][-1])
