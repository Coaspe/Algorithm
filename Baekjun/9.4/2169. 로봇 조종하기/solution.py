N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]


for i in range(1, M):
    B[0][i] += B[0][i - 1]

for i in range(1, N):
    lr = B[i][:]
    rl = B[i][:]

    # Left to Right
    for j in range(M):
        if j:
            lr[j] += max(B[i - 1][j], lr[j - 1])
        else:
            lr[j] += B[i - 1][j]

    for j in range(M - 1, -1, -1):
        if j != M - 1:
            rl[j] += max(B[i - 1][j], rl[j + 1])
        else:
            rl[j] += B[i - 1][j]

    for j in range(M):
        B[i][j] = max(lr[j], rl[j])

print(B[-1][-1])
