def solve():
    import sys

    input = sys.stdin.readline

    N = int(input().strip())

    adj = [[False] * N for _ in range(N)]

    while True:
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break
        adj[a - 1][b - 1] = True
        adj[b - 1][a - 1] = True

    colors = [-1] * N

    def bfs_check(start):
        from collections import deque

        queue = deque([start])
        colors[start] = 0

        while queue:
            v = queue.popleft()
            for w in range(N):
                if w == v:
                    continue
                if not adj[v][w]:
                    if colors[w] == -1:
                        colors[w] = 1 - colors[v]
                        queue.append(w)
                    elif colors[w] == colors[v]:
                        return False
        return True

    for i in range(N):
        if colors[i] == -1:
            if not bfs_check(i):
                print(-1)
                return

    first_color = colors[0]

    teamA = []
    teamB = []
    for i in range(N):
        if colors[i] == first_color:
            teamA.append(i + 1)
        else:
            teamB.append(i + 1)

    print(1)
    print(*sorted(teamA), -1)
    print(*sorted(teamB), -1)


solve()
