import collections
N, K = map(int, input().split())
M = len(str(N))
q = collections.deque([(N, K)])
visited = set([(N, K)])
answer = 0

while q:
    n, k = q.pop()
    if k == 0:
        answer = max(answer, n)
        continue
    n = list(str(n))
    for i in range(M-1):
        for j in range(i+1, M):
            if i == 0 and n[j] == '0':
                continue
            n[i], n[j] = n[j], n[i]
            nn = int(''.join(n))
            n[i], n[j] = n[j], n[i]
            if (nn, k-1) not in visited:
                q.append((nn, k-1))
                visited.add((nn, k-1))
print(answer if answer else -1)
