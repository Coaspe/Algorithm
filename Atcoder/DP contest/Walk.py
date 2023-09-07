# EDPC-Walk
import sys

input = sys.stdin.readline
mod = 10**9 + 7


# 행렬 곱셈
def mat_mul(a, b):
    I, J, K = len(a), len(b[0]), len(b)
    c = [[0] * J for _ in range(I)]
    for i in range(I):
        for j in range(J):
            for k in range(K):
                c[i][j] += a[i][k] * b[k][j]
            c[i][j] %= mod
    return c


# 행렬 제곱
def mat_pow(x, n):
    y = [[0] * len(x) for _ in range(len(x))]

    for i in range(len(x)):
        y[i][i] = 1

    while n > 0:
        if n & 1:
            y = mat_mul(x, y)
        x = mat_mul(x, x)
        n >>= 1

    return y


n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dp = mat_pow(a, k)
ans = 0
for i in range(n):
    for j in range(n):
        ans += dp[i][j]
        ans %= mod
print(ans)
