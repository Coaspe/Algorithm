from sys import maxsize


def solution():
    N, M = map(int, input().split())

    dp = [[maxsize] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        dp[a][b] = 1

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if i != j and dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
    ans = 0
    for i in range(1, N + 1):
        for j, v in enumerate(dp[i]):
            if j == 0 or j == i:
                continue
            if v == maxsize and dp[j][i] == maxsize:
                break
        else:
            ans += 1
    print(ans)


if __name__ == "__main__":
    solution()
