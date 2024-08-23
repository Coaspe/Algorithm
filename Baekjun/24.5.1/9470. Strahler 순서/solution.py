from collections import deque
from sys import stdin

input = stdin.readline
T = int(input())

while T:
    T -= 1
    K, M, P = map(int, input().split())
    GO = [[] for _ in range(M)]
    GI = [[] for _ in range(M)]
    ans = [1] * M
    indegree = [0] * M

    for _ in range(P):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        GO[a].append(b)
        GI[b].append(a)
        indegree[b] += 1

    q = deque()

    for i in range(M):
        if indegree[i] == 0:
            q.append(i)

    while q:
        n = q.popleft()

        cnt = 0
        a = 1
        for i in GI[n]:
            if ans[i] > a:
                a = ans[i]
                cnt = 1
            elif ans[i] == a:
                cnt += 1

        if cnt >= 2:
            a += 1

        ans[n] = a

        for i in GO[n]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    print(K, max(ans))
