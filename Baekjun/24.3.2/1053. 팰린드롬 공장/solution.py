from itertools import combinations

S = list(input())

inf = len(S)


def palin():
    dp = [[0] * len(S) for _ in range(len(S))]
    for i in range(len(S) - 1):
        dp[i][i + 1] = int(S[i] != S[i + 1])

    for j in range(2, len(S)):
        for i in range(len(S) - j):
            dp[i][i + j] = dp[i + 1][i + j - 1] + int(S[i] != S[i + j])
            dp[i][i + j] = min(dp[i][i + j], dp[i + 1][i + j] + 1)
            dp[i][i + j] = min(dp[i][i + j], dp[i][i + j - 1] + 1)

    return dp[0][-1]


ans = palin()

for x, y in combinations(range(len(S)), 2):
    if S[x] != S[y]:
        S[x], S[y] = S[y], S[x]
        ans = min(palin() + 1, ans)
        S[x], S[y] = S[y], S[x]

print(ans)
