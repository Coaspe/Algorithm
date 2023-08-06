from typing import List


class Solution:
    def closestNode(
        self, n: int, edges: List[List[int]], query: List[List[int]]
    ) -> List[int]:
        LOG = 21
        parent = [[0] * LOG for _ in range(n)]
        d = [0] * n
        c = [0] * n
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node, depth):
            c[node] = True
            d[node] = depth
            for child in graph[node]:
                if c[child]:
                    continue
                parent[child][0] = node
                dfs(child, depth + 1)

        def set_parent():
            dfs(0, 0)
            for i in range(1, LOG):
                for j in range(0, n):
                    parent[j][i] = parent[parent[j][i - 1]][i - 1]

        def lca(a, b):
            if d[a] > d[b]:
                a, b = b, a
            for i in range(LOG - 1, -1, -1):
                if d[b] - d[a] >= (1 << i):
                    b = parent[b][i]
            if a == b:
                return a
            for i in range(LOG - 1, -1, -1):
                if parent[a][i] != parent[b][i]:
                    a = parent[a][i]
                    b = parent[b][i]
            return parent[a][0]

        set_parent()

        def find(v, parent):
            if parent[v] != v:
                parent[v] = find(parent[v], parent)
            return parent[v]

        def union_by_rank(v1, v2, parent):
            p1 = find(v1, parent)
            p2 = find(v2, parent)

            if rank[p1] > rank[p2]:
                parent[p2] = p1
            elif rank[p1] < rank[p2]:
                parent[p1] = p2
            else:
                parent[p2] = p1
                rank[p1] += 1

        ans = []

        for idx, (s, e, node) in enumerate(query):
            parent_u = [i for i in range(n)]
            rank = [0 for _ in range(n)]
            LCA = lca(s, e)

            if d[LCA] >= d[node]:
                ans.append(LCA)
                continue

            while s != LCA:
                next_node = parent[s][0]
                union_by_rank(s, next_node, parent_u)
                s = next_node

            while e != LCA:
                next_node = parent[e][0]
                union_by_rank(e, next_node, parent_u)
                e = next_node

            pp = find(LCA, parent_u)

            while find(node, parent_u) != pp:
                node = parent[node][0]
                if d[LCA] >= d[node]:
                    ans.append(LCA)
                    break

            if len(ans) != idx + 1:
                ans.append(node)

        return ans
