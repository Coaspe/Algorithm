N = 10
P = [i for i in range(N)]
rank = [0]*N


def find(x):

    if P[x] != x:
        P[x] = find(P[x])

    return P[x]


def union(x, y):
    px = find(x)
    py = find(y)

    if rank[px] > rank[py]:
        P[py] = px
    elif rank[py] > rank[px]:
        P[px] = py
    else:
        P[py] = px
        rank[px] += 1
