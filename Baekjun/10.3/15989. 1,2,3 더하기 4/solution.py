T = int(input())
# dp[i][j] = 더해준 수를 비오름차순으로 정렬 하고 i를 만들 때 j로 시작하는 경우의 수
dp = [[0] * 4 for _ in range(10001)]

dp[0][1] = 1
dp[1][1] = 1

for i in range(2, 10001):
    dp[i][1] = dp[i - 1][1]
    dp[i][2] = dp[i - 2][1] + dp[i - 2][2]

    if i >= 3:
        dp[i][3] = sum(dp[i - 3])

while T:
    T -= 1
    N = int(input())
    print(sum(dp[N]))
