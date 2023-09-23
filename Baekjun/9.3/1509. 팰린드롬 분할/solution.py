text = input()
n = len(text)

table = [[0] * n for _ in range(n)]

for i in range(n):
    table[i][i] = 1

for i in range(1, n):
    if text[i - 1] == text[i]:
        table[i - 1][i] = 1

for i in range(3, n + 1):
    for start in range(n - i + 1):
        end = start + i - 1
        if text[start] == text[end] and table[start + 1][end - 1]:
            table[start][end] = 1

dp = [0] * n
dp[0] = 1

for i in range(1, n):
    dp[i] = dp[i - 1] + 1
    for j in range(i):
        if table[j][i]:
            dp[i] = min(dp[i], (dp[j - 1] if j >= 1 else 0) + 1)
print(dp[-1])
