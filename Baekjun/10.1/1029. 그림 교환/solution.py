N = int(input())
B = [list(map(int, list(input()))) for _ in range(N)]
dp = [[[0] * 10 for _ in range(1 << N)] for _ in range(N)]


def dfs(cur, visited, pre_price):
    if dp[cur][visited][pre_price]:
        return dp[cur][visited][pre_price]

    dp[cur][visited][pre_price] = 1

    if visited == (1 << N) - 1:
        return 1

    for i in range(N):
        if not (visited & (1 << i)) and B[cur][i] >= pre_price and i != cur:
            dp[cur][visited][pre_price] = max(
                dp[cur][visited][pre_price], dfs(i, visited | (1 << i), B[cur][i]) + 1
            )

    return dp[cur][visited][pre_price]


print(dfs(0, 1, 0))
