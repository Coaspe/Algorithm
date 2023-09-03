from collections import deque
import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

# 본인이 얼리 어답터 [일 때, 아닐 때]


def dfs(node):
    visited[node] = 1
    dp[node][0] = 1

    for child in tree[node]:
        if not visited[child]:
            dfs(child)
            dp[node][0] += min(dp[child][0], dp[child][1])
            dp[node][1] += dp[child][0]


N = int(input())
tree = [[] for _ in range(N + 1)]
dp = [[0, 0] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(1)
answer = min(dp[1][0], dp[1][1])
print(answer)


'''
BFS
'''

N = int(sys.stdin.readline())
G = [[] for _ in range(N+1)]
ans = 0

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    G[a].append(b)
    G[b].append(a)

visited = [False]*(N+1)
num = [len(G[i]) for i in range(N+1)]

Q = deque()
for i in range(1, N+1):
    if num[i] == 1:
        Q.append(i)
while Q:
    tar = Q.popleft()
    if num[tar] != 1 or visited[tar]:
        continue
    for v in G[tar]:
        if not visited[v]:
            tmp = v
            break

    visited[tmp] = True
    ans += 1
    for v in G[tmp]:
        if visited[v]:
            continue
        num[v] -= 1
        if num[v] == 1:
            Q.append(v)
print(ans)
