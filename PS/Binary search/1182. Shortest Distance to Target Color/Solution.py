from typing import List
import collections
import bisect

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        hashmap = collections.defaultdict(list)
        answer = []
        for i, c in enumerate(colors):
            hashmap[c].append(i)

        for i, c in queries:
            if c not in hashmap:
                answer.append(-1)
                continue

            insert = bisect.bisect_left(hashmap[c], i)
            left = abs(hashmap[c][max(insert-1, 0)] - i)
            right = abs(hashmap[c][min(insert, len(hashmap[c])-1)] - i)
            answer.append(min(left, right))
            
        return answer
        
    def bi_left(self, arr: List[int], idx: int) -> int:
        l, r = 0, len(arr) - 1

        while r > l:
            mid = (l+r) // 2

            if arr[mid] > idx:
                r = mid
            elif arr[mid] < idx:
                l = mid + 1
            else:
                return mid

        return l