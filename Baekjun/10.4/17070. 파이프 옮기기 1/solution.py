def solution():
    N = int(input())
    B = [list(map(int, input().split())) for _ in range(N)]
    # dp[i][j][k] = i,j에 파이프의 끝이 있고, k방향으로 놓을 수 있는 경우의 수
    dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
    dp[0][1][0] = 1

    for i in range(N):
        for j in range(2, N):
            if B[i][j] == 1:
                continue
            dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2]
            dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2]
            if B[i - 1][j] == 0 and B[i][j - 1] == 0:
                dp[i][j][2] = sum(dp[i - 1][j - 1])

    print(sum(dp[N - 1][N - 1]))


if __name__ == "__main__":
    solution()
