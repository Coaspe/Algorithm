import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    f = list(map(int, input().split()))
    d = [[0]*(n+1) for _ in range(n+1)]

    for i in range(n-1):
        d[i][i+1] = f[i] + f[i+1]
        for j in range(i+2, n):
            d[i][j] = d[i][j-1] + f[j]

    for v in range(2, n):
        for i in range(n-v):
            d[i][i+v] += min([d[i][k] + d[k+1][i+v] for k in range(i, i+v)])

    print(d[0][n-1])
