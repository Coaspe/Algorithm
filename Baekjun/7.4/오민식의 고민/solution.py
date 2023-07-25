from collections import deque


N, S, E, M = map(int, input().split())
edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

earning = list(map(int, input().split()))

for i in range(M):
    edges[i] = (edges[i][0], edges[i][1], edges[i][2] - earning[edges[i][1]])


def bfs(start, end):
    q = deque()
    q.append(start)
    visited = [False]*(N)
    visited[start] = True
    while q:
        now = q.popleft()
        if now == end:
            return True
        for s, e, _ in edges:
            if s == now and not visited[e]:
                visited[e] = True
                q.append(e)

    return False


MAX = 10**9


def BF(start):
    money = [MAX] * N
    money[start] = -earning[start]
    last_node = N-1

    for v in range(N):
        for cur, next, cost in edges:
            if money[cur] != MAX and money[next] > money[cur] + cost:
                if v != last_node:
                    money[next] = money[cur] + cost
                # 사이클이 가는 길에 있는건지, 아닌지 확인해야한다.
                if v == last_node and money[cur] != MAX and bfs(cur, E):
                    print("Gee")
                    exit()

    return money


money = BF(S)

if money[E] != MAX:
    print(-money[E])
else:
    print("gg")
