import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def solve():
    v, e = map(int, input().split())
    stack, scc, cnt = [], [], [0]  # cnt를 내부함수 전역변수로 쓰기 위해
    visited, finished = [0 for _ in range(v+1)], [False for _ in range(v+1)]
    edge = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        edge[b].append(a)
        edge[a].append(b)

    def dfs(now):
        cnt[0] += 1
        visited[now] = cnt[0]
        stack.append(now)
        result = visited[now]

        for nxt in edge[now]:
            if visited[nxt] == 0:
                result = min(result, dfs(nxt))
            elif not finished[nxt]:
                result = min(result, visited[nxt])

        if result == visited[now]:
            group = []
            while True:
                top = stack.pop()
                group.append(top)
                finished[top] = True
                if top == now:
                    break
            scc.append(group)

        return result

    for i in range(1, v+1):
        if visited[i] == 0:
            dfs(i)

    for r in scc:
        e = 0
        for n in r:
            e += len(edge[n])
        e /= 2
        if e != len(r):
            print("No")
            return
    print("Yes")


solve()
