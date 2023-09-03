N, K = map(int, input().split())
M = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
X -= 1
Y -= 1

T = 0
ll = N*N

virus = [[] for _ in range(K+1)]

for r in range(N):
    for c in range(N):
        if M[r][c] > 0:
            virus[M[r][c]].append((r, c))
            T += 1

while T < ll and S:
    for idx, arr in enumerate(virus):
        new_arr = []
        for r, c in arr:
            for row, col in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
                if 0 <= row < N and 0 <= col < N and M[row][col] == 0:
                    new_arr.append((row, col))
                    M[row][col] = idx
                    T += 1

                if M[X][Y] != 0:
                    print(M[X][Y])
                    exit(0)
        virus[idx] = new_arr
    S -= 1

print(M[X][Y])
