from collections import deque
import sys

input = sys.stdin.readline
R, C = map(int, input().split())
B = [input() for _ in range(R)]
check = [[[0, 0] for _ in range(C)] for _ in range(R)]
q = deque([(0, 0, 0, 1)])


while q:
    r, c, K, cnt = q.popleft()

    if check[r][c][K]:
        continue

    check[r][c][K] = 1

    if r == R - 1 and c == C - 1:
        print(cnt)
        exit(0)

    for row, col in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
        if 0 <= row < R and 0 <= col < C and not all(check[row][col]):
            if B[row][col] == "0" and not check[row][col][K]:
                q.append((row, col, K, cnt + 1))
            elif not K and not check[row][col][1]:
                q.append((row, col, 1, cnt + 1))
print(-1)
