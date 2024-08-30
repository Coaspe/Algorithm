K, N, F = map(int, input().split())
G = [[] for _ in range(N)]

IF = [[0] * N for _ in range(N)]
for _ in range(F):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    IF[a][b] = 1
    IF[b][a] = 1


CL = []
CS = set()


def dfs(cur):
    for i in range(cur + 1, N):
        if i in CS:
            continue

        for node in CL:
            if not IF[node][i]:
                break
        else:
            CL.append(i)
            CS.add(i)
            if len(CL) == K:
                print("\n".join([str(i + 1) for i in sorted(CL)]))
                exit(0)
            dfs(i)
            CL.pop()
            CS.remove(i)


for i in range(N):
    CL.append(i)
    CS.add(i)
    dfs(i)
    CL.pop()
    CS.remove(i)

print(-1)
