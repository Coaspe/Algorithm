from collections import deque
N, K = int(input()), int(input())
apples = [[0]*N for _ in range(N)]

for _ in range(K):
    x, y = map(int, input().split())
    apples[x-1][y-1] = 1

D = {}
move = {
    0: lambda x, y: (x, y+1),
    1: lambda x, y: (x+1, y),
    2: lambda x, y: (x, y-1),
    3: lambda x, y: (x-1, y),
}
body = set([(0, 0)])
bodyDeque = deque([(0, 0)])

L = int(input())

for _ in range(L):
    t, d = input().split()
    D[int(t)] = d

T = 1

d = 0
while 1:
    head = move[d](*bodyDeque[-1])
    if not (0 <= head[0] < N and 0 <= head[1] < N) or head in body:
        break

    body.add(head)
    bodyDeque.append(head)

    if not apples[head[0]][head[1]]:
        body.remove(bodyDeque.popleft())

    apples[head[0]][head[1]] = 0

    if D.get(T) == 'L':
        d -= 1
        if d == -1:
            d = 3
    elif D.get(T) == 'D':
        d += 1
        d %= 4

    T += 1

print(T)
