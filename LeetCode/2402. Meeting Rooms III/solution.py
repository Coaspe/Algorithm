from heapq import heapify, heappop, heappush


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        not_used = list(range(n))
        used = []
        cnt = [0] * n
        heapify(not_used)

        for s, e in sorted(meetings):
            while used and used[0][0] <= s:
                _, room = heappop(used)
                heappush(not_used, room)

            if len(used) < n:
                r = heappop(not_used)
                heappush(used, (e, r))
            else:
                ue, r = heappop(used)
                heappush(used, (ue + e - s, r))

            cnt[r] += 1

        return cnt.index(max(cnt))
