N, K = map(int, input().split())
A = list(map(int, input().split()))
# dp[i][j] = i번째 사람까지 봤을 떄, 총 j개의 사탕을 나누어줄수 있는 경우의 수
MOD = 1e9 + 7
dp = [[0] * (K + 1) for _ in range(N)]
P = [0] * (K + 2)


def Add(a, b):
    return a + b if a + b < MOD else a + b - MOD


def Sub(a, b):
    return a - b + MOD if a - b < 0 else a - b


for i in range(N):
    if i == 0:
        for j in range(K + 1):
            dp[i][j] = int(A[i] >= j)
    else:
        for j in range(K + 1):
            dp[i][j] = Sub(P[j + 1], P[max(j - A[i], 0)])

    for j in range(K + 1):
        P[j + 1] = Add(P[j], dp[i][j])

print(int(dp[N - 1][K]))
