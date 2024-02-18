N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 1e9 + 7
# dp[i][j] = i번째 사람까지 봤을 떄, 총 j개의 사탕을 나누어줄수 있는 경우의 수
dp = [[0] * (K + 1) for _ in range(N)]
# P[i] = sum(dp[i-1][j-k]) 1 <= k <= A[i]
P = [0] * (K + 2)

for i in range(N):
    if i == 0:
        for j in range(K + 1):
            dp[i][j] = int(A[i] >= j)
    else:
        for j in range(K + 1):
            dp[i][j] = (P[j + 1] - P[max(j - A[i], 0)] + MOD) % MOD

    for j in range(K + 1):
        P[j + 1] = (P[j] + dp[i][j]) % MOD

print(int(dp[N - 1][K]))
