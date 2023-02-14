import sys

# 곱


def matrix_mul(mat_a, mat_b):
    length = len(mat_a)
    temp = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            for k in range(length):
                temp[i][j] += mat_a[i][k] * mat_b[k][j]
            temp[i][j] %= 1000
    return temp

# 제곱


def power(a, b):
    if b == 1:  # b의 값이 1이 될 때까지 재귀
        return a
    else:
        tmp = power(a, b // 2)  # a^(b // 2)
        if b % 2 == 0:
            return matrix_mul(tmp, tmp)  # b가 짝수인 경우
        else:
            return matrix_mul(matrix_mul(tmp, tmp), a)  # b가 홀수인 경우


read = sys.stdin.readline
N, M = map(int, read().split())
matrix = [list(map(int, read().split())) for _ in range(N)]
result = power(matrix, M)
for row in result:
    for num in row:
        print(num % 1000, end=' ')
    print()
