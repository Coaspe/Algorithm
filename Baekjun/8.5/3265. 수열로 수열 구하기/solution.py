import sys

input = sys.stdin.readline
N, M = map(int, input().split())
B = [0] + list(map(int, input().split()))

A = [0] * (N + 1)
assgined = [0] * (N + 1)

for _ in range(M):
    x, y = map(int, input().split())
    A[x] = y
    assgined[y] = 1


def solve():
    current = 1
    prev = 0

    while current <= N:
        prev = current

        # 1 탐색
        while not B[current] and current <= N:
            current += 1

        if current > N:
            return 0

        w = prev

        for j in range(current, prev - 1, -1):
            if not assgined[j]:
                while A[w]:
                    w += 1
                A[w] = j

        current += 1

    return 1


def check():
    max_val = 0
    for i in range(1, N + 1):
        max_val = max(A[i], max_val)

        if B[i] and max_val != i:
            return 0

        if not B[i] and max_val == i:
            return 0

    return 1


if not solve():
    print(-1)
elif check():
    print(*A[1:])
else:
    print("-1")
