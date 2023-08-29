N, M = map(int, input().split())
B = [input() for _ in range(N)]

for i in range(len(B)):
    B[i] = [int(bit) for bit in B[i]]

ans = max(B[0])

for i in range(N):
    ans = max(ans, B[i][0])

for i in range(1, N):
    for j in range(1, M):
        if B[i][j]:
            B[i][j] = min(B[i - 1][j - 1], B[i - 1][j], B[i][j - 1]) + 1
            ans = max(ans, B[i][j])

print(ans**2)
