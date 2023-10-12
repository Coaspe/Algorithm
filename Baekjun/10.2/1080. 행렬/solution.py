N, M = map(int, input().split())

A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(N)]


def inverse(r, c):
    for row in (r, r + 1, r + 2):
        for col in (c, c + 1, c + 2):
            A[row][col] = "0" if A[row][col] == "1" else "1"


ans = 0
for i in range(N - 2):
    for j in range(M - 2):
        if A[i][j] != B[i][j]:
            ans += 1
            inverse(i, j)

for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            print(-1)
            exit(0)
print(ans)
