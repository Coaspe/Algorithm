N, M = map(int, input().split())

truth = list(map(int, input().split()))[1:]
party = [list(map(int, input().split()))[1:] for _ in range(M)]

parent = [i for i in range(N + 1)]


def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x


for i in range(1, len(truth)):
    union(truth[i], truth[i - 1])

for p in party:
    for i in range(1, len(p)):
        union(p[i], p[i - 1])

ans = 0

for p in party:
    for i in range(len(p)):
        if truth and find(p[i]) == find(truth[0]):
            break
        if i == len(p) - 1:
            ans += 1

print(ans)
