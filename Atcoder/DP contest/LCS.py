w1, w2 = input(), input()
l1, l2 = len(w1), len(w2)
dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]

for i in range(1, l1 + 1):
    for j in range(1, l2 + 1):
        if w1[i - 1] == w2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
i = l1
j = l2
ans = []

while i > 0 and j > 0:
    if w1[i - 1] == w2[j - 1]:
        ans.append(w1[i - 1])
        i -= 1
        j -= 1
    elif dp[i][j] == dp[i - 1][j]:
        i -= 1
    else:
        j -= 1

print(*ans[::-1], sep="")
