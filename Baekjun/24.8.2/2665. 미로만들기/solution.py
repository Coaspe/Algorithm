from collections import deque

N = int(input())
B = [list(input()) for _ in range(N)]
C = [[-1] * N for _ in range(N)]
q = deque([(0, 0, 0)])
C[0][0] = 0

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
while q:
    r, c, cost = q.popleft()

    if r == c == N - 1:
        print(cost)
        break

    for i in range(4):
        row, col = r + dx[i], c + dy[i]

        if 0 <= row < N and 0 <= col < N:
            if B[row][col] == "0":
                new_cost = cost + 1
                if C[row][col] == -1 or C[row][col] > new_cost:
                    C[row][col] = new_cost
                    q.append((row, col, new_cost))
            elif C[row][col] == -1 or C[row][col] > cost:
                C[row][col] = cost
                q.appendleft((row, col, cost))
