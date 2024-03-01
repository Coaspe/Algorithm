# Binary search, Tree traversal
from sys import setrecursionlimit

setrecursionlimit(10**5 + 1)


def solution(k, num, links):
    N = len(num)
    G = [[] for _ in range(N)]
    kk = 0

    all_nodes = set(range(N))
    for idx, (a, b) in enumerate(links):
        all_nodes.discard(a)
        all_nodes.discard(b)
        G[idx] = [a, b]

    root = list(all_nodes)[0]

    def dfs(node, mid):
        if node == -1:
            return 0

        left = dfs(G[node][0], mid)
        right = dfs(G[node][1], mid)

        if left == None or right == None:
            return None

        val = num[node]

        min_val = min(left, right)
        max_val = max(left, right)

        nonlocal kk

        if val > mid:
            return None
        elif val + min_val + max_val <= mid:
            return val + min_val + max_val
        elif val + min_val <= mid:
            kk -= 1
            if kk < 0:
                return None
            return val + min_val
        else:
            kk -= 2
            if kk < 0:
                return None
            return val

    k -= 1

    l, r = min(num) - 1, 10000 * 10000 + 1

    while r > l + 1:
        mid = (l + r) // 2
        kk = k
        if dfs(root, mid) != None:
            r = mid
        else:
            l = mid

    return r
