S1 = input()
S2 = input()

l1, l2 = len(S1), len(S2)

# dp[i][j] => l1의 i 인덱스, l2의 j 인덱스로 끝나는
# 최장 부분 문자열의 길이.
dp = [[0] * 4001 for _ in range(4001)]

ans = 0

for i in range(l1):
    for j in range(l2):
        if S1[i] == S2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            ans = max(ans, dp[i][j])
print(ans)
