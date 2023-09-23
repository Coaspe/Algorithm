from sys import stdin
from heapq import heappush, heappop, heapify

input = stdin.readline
T = int(input())

while T:
    T -= 1

    N = int(input())
    A = list(map(int, input().split()))
    heapify(A)

    ans = 0

    while len(A) > 1:
        x = heappop(A)
        y = heappop(A)
        ans += x + y
        heappush(A, x + y)

    print(ans)
