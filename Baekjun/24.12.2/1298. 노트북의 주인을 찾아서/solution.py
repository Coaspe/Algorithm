N, M = map(int, input().split())

G = [[] for _ in range(N + 1)]

for _ in range(M):
    p, l = map(int, input().split())

    G[p].append(l)

assigned = [-1] * (N + 1)


def dfs(cow):
    for cnr in G[cow]:
        if not check[cnr]:
            check[cnr] = 1
            if assigned[cnr] == -1 or dfs(assigned[cnr]):
                assigned[cnr] = cow
                return True

    return False


result = 0

for i in range(N + 1):
    check = [0] * (N + 1)
    result += int(dfs(i))

print(result)
