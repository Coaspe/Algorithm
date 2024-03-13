from collections import deque
from sys import stdin

input = stdin.readline
N = int(input())

balls = [int(input()) for _ in range(N)]

ans = N

for i in range(1, N - 1):

    left, right = balls[: i + 1], deque(balls[i + 1 :])

    left[-1] = left[-2]
    while (left and color == left[-1]) or (right and color == right[0]):
        cnt = 0

        while left and color == left[-1]:
            left.pop()
            cnt += 1

        while right and color == right[0]:
            right.popleft()
            cnt += 1

        if cnt < 4:
            ans = min(ans, cnt + len(left) + len(right))
            break
        else:
            ans = min(ans, len(left) + len(right))

        if left:
            color = left[-1]
        elif right:
            color = right[0]

print(ans)
