class Solution(object):
    def numIslands2(self, m, n, positions):
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            x, y = find(x), find(y)
            if x == y:
                return 0
            parent[y] = x
            return 1

        counts, count = [], 0
        for i, j in positions:
            if (i, j) not in parent:
                x = parent[x] = i, j
                count += 1
                for y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                    if y in parent:
                        count -= union(x, y)
                counts.append(count)
            else:
                counts.append(count)
        return counts
