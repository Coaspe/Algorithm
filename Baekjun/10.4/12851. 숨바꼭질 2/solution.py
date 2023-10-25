from collections import deque

N, K = map(int, input().split())

D = [0] * 1000001


q = deque([N])
cnt = 0

while q:
    n = q.popleft()

    if n == K:
        cnt += 1
        continue

    for i in n - 1, n + 1, 2 * n:
        if 0 <= i <= 1000000 and (D[i] == 0 or D[i] == D[n] + 1):
            D[i] = D[n] + 1
            q.append(i)

print(D[K])
print(cnt)
