from collections import deque

dist = [0]*100001
move = [0]*100001

N, K = map(int, input().split())
q = deque([N])

while q:
    n = q.popleft()
    if n == K:
        print(dist[n])
        arr = [n]
        while n != N:
            n = move[n]
            arr.append(n)
        print(*arr[::-1])
        break
    for x in n-1, n+1, 2*n:
        if 0 <= x <= 100000 and dist[x] == 0:
            move[x] = n
            dist[x] = dist[n] + 1
            q.append(x)
