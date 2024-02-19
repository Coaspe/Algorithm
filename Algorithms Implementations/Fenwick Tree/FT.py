class FT:
    def __init__(self, arr: list):
        self.arr = arr
        self.arr.insert(0, 0)
        self.makeFT()

    def makeFT(self):
        self.tree = [0] * len(self.arr)
        for i in range(1, len(self.arr)):
            self.update(i, self.arr[i])

    def sum(self, i):
        ans = 0
        while i > 0:
            ans += self.tree[i]
            i -= i & -i
        return ans

    def update(self, i, diff):
        while i < len(self.tree):
            self.tree[i] += diff
            i += i & -i


f = FT([1, 12, -5, -6, 50, 3])
print(f.tree)
# f.update(1, 1)
print(f.tree)
print(f.sum(2))
# ~ n-1
"""
Time: log(n)
"""
