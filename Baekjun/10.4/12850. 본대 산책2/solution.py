N = 8


def matmul(a, b):
    c = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            tmp = 0
            for k in range(N):
                tmp += a[i][k] * b[k][j]
            tmp %= 1000000007
            c[i][j] = tmp

    return c


MT = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0],
]


def matpow(a, n):
    if n == 1:
        return a
    elif n % 2 == 0:
        return matpow(matmul(a, a), n // 2)
    else:
        return matmul(matpow(matmul(a, a), n // 2), a)


D = int(input())
print(matpow(MT, D)[0][0])
