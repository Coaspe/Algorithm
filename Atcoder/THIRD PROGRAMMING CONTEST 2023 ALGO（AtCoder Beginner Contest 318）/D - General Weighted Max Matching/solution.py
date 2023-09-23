N = int(input())
D = [[0] * N for _ in range(N)]

for i in range(N - 1):
    row = list(map(int, input().split()))
    for j in range(i + 1, N):
        D[i][j] = row[j - (i + 1)]


dp = [0] * (1 << N)

for b in range(1 << N):
    for i in range(N):
        l = -1
        if not b & (1 << i):
            l = i
            break

    for i in range(N):
        if i != l and not b & (1 << i):
            nb = b | (1 << l)
            nb |= 1 << i

            dp[nb] = max(dp[nb], dp[b] + D[l][i])

print(dp[-1])
