N, M, C = map(int, input().split())
earn = list(map(int, input().split()))
abj = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    abj[a].append(b)


"""
모든 경우에 얻을 수 있는 가장 큰 mooney는 1000t - t*t이다. (모든 도시의 earning이 1000일 때)
그 때 t가 1000 보다 커지면 값이 음수가 되기 때문에 많아도 1000일 까지만 탐색하면 된다.
"""
# dp[i][j] = i일에 j번째 도시에서 여행을 끝낼때 얻을 수 있는 mooney
dp = [[-1] * N for _ in range(1001)]

dp[0][0] = 0

ans = 0
for i in range(1000):
    for j in range(N):
        if dp[i][j] != -1:
            for k in abj[j]:
                dp[i + 1][k] = max(dp[i + 1][k], dp[i][j] + earn[k])
    ans = max(ans, dp[i][0] - (C * i * i))

print(ans)
