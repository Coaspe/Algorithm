import sys
from collections import deque

input = sys.stdin.readline


def solution():
    K = int(input())
    C, R = map(int, input().split())

    B = [list(map(int, input().split())) for _ in range(R)]

    MAX = R * C + 1
    visited = [[MAX] * C for _ in range(R)]

    q = deque([(0, 0, 0, K)])
    visited[0][0] = 0

    while q:
        r, c, k, n = q.popleft()

        if r == R - 1 and c == C - 1:
            print(k)
            return

        if n:
            for row, col in (
                (r - 1, c - 2),
                (r - 2, c - 1),
                (r + 1, c - 2),
                (r + 2, c - 1),
                (r - 1, c + 2),
                (r - 2, c + 1),
                (r + 1, c + 2),
                (r + 2, c + 1),
            ):
                if (
                    0 <= row < R
                    and 0 <= col < C
                    and not B[row][col]
                    and visited[row][col] > n - 1
                ):
                    visited[row][col] = n - 1
                    q.append((row, col, k + 1, n - 1))

        for row, col in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
            if (
                0 <= row < R
                and 0 <= col < C
                and not B[row][col]
                and visited[row][col] > n
            ):
                visited[row][col] = n
                q.append((row, col, k + 1, n))

    print(-1)


if __name__ == "__main__":
    solution()
