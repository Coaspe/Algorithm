S = input()
n = len(S)
# dp[i][j]
# i번째 문자까지 '('가 ')' 보다 j 개 많을 때, k <= i인 모든 k에 대해  '(' 수가 ')' 수보다 많도록 '?'를 '(' 또는 ')'로 대체하는 경우의 수
dp = [[0] * (n + 1) for _ in range(n + 1)]
MOD = 998244353
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if S[i] != ')':
            dp[i + 1][j + 1] += dp[i][j]
        if j != 0 and S[i] != '(':
            dp[i + 1][j - 1] += dp[i][j]

print(dp[n][0] % MOD)
