import sys
import math

read = sys.stdin.readline

n = int(read())
A = list(map(int, read().split()))
B = list(map(int, read().split()))

arr = [[i, j] for i, j in zip(A, B)]

arr.sort(key=lambda x: (x[1], x[0]))

previous = arr[0][1]
cur_max = -1
answer = 0

for i in range(n):
    if previous > arr[i][0]:
        previous = max(previous, arr[i][1])

        cnt = math.ceil((previous - arr[i][0]) / 30)
        arr[i][0] += cnt * 30
        answer += cnt

    cur_max = max(cur_max, arr[i][0])

    if i + 1 < n and (arr[i][1] != arr[i + 1][1]):
        previous = cur_max


print(answer)
