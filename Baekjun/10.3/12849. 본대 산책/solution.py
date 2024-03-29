D = int(input())

DP = [[0] * (D + 1) for _ in range(8)]
DP[0][0] = 1
for i in range(1, D + 1):
    DP[0][i] = (DP[1][i - 1] + DP[2][i - 1]) % 1000000007
    DP[1][i] = (DP[0][i - 1] + DP[2][i - 1] + DP[3][i - 1]) % 1000000007
    DP[2][i] = (DP[0][i - 1] + DP[1][i - 1] + DP[3][i - 1] + DP[4][i - 1]) % 1000000007
    DP[3][i] = (DP[1][i - 1] + DP[2][i - 1] + DP[4][i - 1] + DP[5][i - 1]) % 1000000007
    DP[4][i] = (DP[2][i - 1] + DP[3][i - 1] + DP[5][i - 1] + DP[6][i - 1]) % 1000000007
    DP[5][i] = (DP[3][i - 1] + DP[4][i - 1] + DP[7][i - 1]) % 1000000007
    DP[6][i] = (DP[4][i - 1] + DP[7][i - 1]) % 1000000007
    DP[7][i] = (DP[5][i - 1] + DP[6][i - 1]) % 1000000007

print(DP[0][D])
