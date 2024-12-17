from sys import stdin

input = stdin.readline
N = int(input())

A = set()

for _ in range(N):
    _, a, b = map(int, input().split())
    A.add((a, b))

A = sorted(A, key=lambda x: (-x[0], x[1]))

from bisect import bisect_right

lis = []
for i in range(len(A)):
    idx = bisect_right(lis, A[i][1])

    if idx >= len(lis):
        lis.append(A[i][1])
    else:
        lis[idx] = A[i][1]

print(len(lis))
