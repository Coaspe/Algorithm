class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        capital = [(capital[i], i) for i in range(len(capital))]
        capital.sort()
        i = 0

        q = []

        while k:
            while i < len(capital) and capital[i][0] <= w:
                heappush(q, -profits[capital[i][1]])
                i += 1

            if not q:
                break

            k -= 1
            w -= heappop(q)

        return w
