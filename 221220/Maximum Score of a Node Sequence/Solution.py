class Solution:
    def maximumScore(self, A: List[int], E: List[List[int]]) -> int:
        n = len(A)

        # Store the top 3 neighbors of a node.
        top3 = collections.defaultdict(list)

        def func(a, b, e):
            bisect.insort_left(top3[a], [e, b])
            if len(top3[a]) > 3:
                top3[a].pop(0)

        # Update the information of top 3 neighbors of each node
        for a, b in E:
            func(a, b, A[b])
            func(b, a, A[a])

        ans = -1
        for a, b in E:
            # If there is less than 2 neighbors of a node, skip this pair.
            if len(top3[a]) < 2 or len(top3[b]) < 2:
                continue
            for c in top3[a]:
                for d in top3[b]:
                    # Find the maximum score of two non-duplicated neighbors of a and b.
                    if c[1] not in [a, b] and d[1] not in [a, b] and c[1] != d[1]:
                        ans = max(ans, A[a] + A[b] + c[0] + d[0])
        return ans
