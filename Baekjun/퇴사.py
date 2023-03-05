N = int(input())

works = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * N

for i in range(N-1, -1, -1):
    t, p = works[i]

    if t + i <= N:
        dp[i] = max(p + (max(dp[t + i:]) if t + i != N else 0),
                    max(dp[i + 1:]) if i + 1 != N else 0)
    else:
        dp[i] = max(dp[i + 1:]) if i + 1 < N else 0
print(dp[0])
