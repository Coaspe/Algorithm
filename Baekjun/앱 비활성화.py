N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))  # byte
C = [0] + list(map(int, input().split()))  # cost
sCost = sum(C)
dp = [[0 for _ in range(sum(C)+1)] for _ in range(N+1)]  # 냅색알고리즘이 실행될 dp
result = sum(C)  # 열의 최댓값

for i in range(1, N+1):
    byte = A[i]
    cost = C[i]

    for j in range(1, sCost + 1):
        if cost > j:
            dp[i][j] = dp[i-1][j]
            continue
        dp[i][j] = max(dp[i-1][j], byte + dp[i-1][j-cost])

        if dp[i][j] >= M:
            result = min(result, j)
if M != 0:
    print(result)
else:
    print(0)
