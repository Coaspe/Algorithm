from heapq import heapify, heappop
import sys

input = sys.stdin.readline
N = int(input())


X = []
for _ in range(N):
    a, b = map(int, input().split())
    X.append((-b, a))

heapify(X)

ans = 0
C = [0] * (N + 1)
while X:
    b, a = heappop(X)
    for i in range(a, 0, -1):
        if not C[i]:
            C[i] = 1
            ans -= b
            break

print(ans)
