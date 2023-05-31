class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        counter = [0] * 10001

        for row in mat:
            for r in row:
                counter[r] += 1

        for k in range(1, 10001):
            if counter[k] == len(mat):
                return k

        return -1
