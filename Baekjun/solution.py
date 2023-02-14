N, K, D = map(int, input().split())
# dp (i, j, k) a1 ~ ai 까지의 요소들을 D로 나눈 나머지들 중 j개를 골라서 합친 값이 k인 것중에 최대
A = list(map(int, input().split()))

dp = [[[-1] * D for _ in range(K+1)] for _ in range(N+1)]

dp[0][0][0] = 0

for i in range(N):
    for j in range(K+1):
        for k in range(D):
            if dp[i][j][k] == -1:
                continue
            dp[i+1][j][k] = max(dp[i+1][j][k], dp[i][j][k])

            if j != K:
                dp[i+1][j+1][(k+A[i]) % D] = max(dp[i+1][j+1]
                                                 [(k+A[i]) % D], dp[i][j][k] + A[i])

print(dp[N][K][0])
