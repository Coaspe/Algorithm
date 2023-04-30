import sys
from collections import defaultdict

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    ball = []
    for i in range(n):
        c, s = map(int, sys.stdin.readline().split())
        ball.append([c, s, i])

    ball.sort(key=lambda x: x[1])

    answer = defaultdict(int)
    ball_size_sum = defaultdict(int)

    total = 0
    i, j = 0, 0
    for i in range(n):
        while ball[j][1] < ball[i][1]:
            total += ball[j][1]
            ball_size_sum[ball[j][0]] += ball[j][1]
            j += 1
        answer[ball[i][2]] = total - ball_size_sum[ball[i][0]]
    for i in range(n):
        print(answer[i])
