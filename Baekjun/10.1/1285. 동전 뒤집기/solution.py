N = int(input())
A = [list(input()) for _ in range(N)]
ans = N * N

for bit in range(1 << N):
    tmp = [A[i][:] for i in range(N)]

    for i in range(N):
        if bit & (1 << i):
            for j in range(N):
                if tmp[i][j] == "H":
                    tmp[i][j] = "T"
                else:
                    tmp[i][j] = "H"

    tsum = 0

    for i in range(N):
        cnt = 0
        for j in range(N):
            if tmp[j][i] == "T":
                cnt += 1

        tsum += min(cnt, N - cnt)

    ans = min(ans, tsum)
print(ans)


import sys

input = sys.stdin.readline


def turn(n):
    for i in range(N):
        board[i][n] = abs(board[i][n] - 1)


N = int(input())

board = []
for i in range(N):
    board.append([*map(lambda x: 1 if x == "T" else 0, input().strip())])

result = N**2
bitlast = 0
for bit in range(1 << N):
    for n in range(N):
        if (bit ^ bitlast) & (1 << n):
            turn(n)
    result = min(result, sum(map(lambda x: min(sum(x), N - sum(x)), board)))
    bitlast = bit

print(result)
