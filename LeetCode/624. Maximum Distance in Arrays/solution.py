class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_v, max_v = min(arrays[0]), max(arrays[0])
        ans = 0

        for i in range(1, len(arrays)):
            arr = arrays[i]

            tmp_min = min(arr)
            tmp_max = max(arr)

            ans = max(ans, max_v - tmp_min, tmp_max - min_v)
            
            max_v = max(max_v, tmp_max)
            min_v = min(min_v, tmp_min)

        return ans