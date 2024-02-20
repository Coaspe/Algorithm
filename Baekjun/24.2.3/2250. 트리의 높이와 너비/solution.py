from sys import stdin
from collections import defaultdict


def dfs(tree, root, level):
    if root == -1:
        return

    global coldict, col
    dfs(tree, tree[root][0], level + 1)
    coldict[level].append(col)
    col += 1
    dfs(tree, tree[root][1], level + 1)
    return


N = int(stdin.readline())
tree = {}
set_all = set(range(1, N + 1))
for i in range(N):
    n, l, r = map(int, stdin.readline().split())
    tree[n] = (l, r)
    set_all.discard(l)
    set_all.discard(r)

root = list(set_all)[0]

coldict = defaultdict(list)
col = 1
dfs(tree, root, 1)

maxwidth = 0
maxlevel = 1
for level, cols in sorted(coldict.items()):
    width = cols[-1] - cols[0]
    if width > maxwidth:
        maxwidth = width
        maxlevel = level

print(maxlevel, maxwidth + 1)
