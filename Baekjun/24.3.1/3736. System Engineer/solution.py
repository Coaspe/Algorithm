from collections import deque


def dfs3(now):
    for next_node in G[now]:
        if B[next_node] == -1 or (
            level[B[next_node]] == level[now] + 2 and dfs3(B[next_node])
        ):
            A[now], B[next_node] = next_node, now
            return True
    return False


while True:
    try:
        N = int(input())
    except:
        break

    G = [[] for _ in range(N)]

    max_val = 0
    for _ in range(N):
        I = input()
        job = int(I.split(":")[0])
        servers = list(map(int, I.split()[2:]))
        G[job] = servers
        max_val = max(max_val, max(servers))

    A = [-1] * (N)
    B = [-1] * (max_val + 1)
    q = deque()
    ans = 0

    while True:
        level = [-1] * N
        for i in range(N):
            if A[i] == -1:
                level[i] = 0
                q.append(i)

        while q:
            now = q.popleft()

            for next_node in G[now]:
                if B[next_node] != -1 and level[B[next_node]] == -1:
                    level[B[next_node]] = level[now] + 2
                    q.append(B[next_node])

        temp = sum(1 for i in range(N) if A[i] == -1 and dfs3(i))
        if not temp:
            break

        ans += temp

    print(ans)
