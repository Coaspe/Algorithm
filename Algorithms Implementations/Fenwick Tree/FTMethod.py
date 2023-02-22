arr = [0, 1, 2, 3, 4, 5, 6, 7]
tree = [0]*len(arr)


def makeFT():
    for i in range(1, len(arr)):
        update(i, arr[i])


def sum(i):
    ans = 0
    while i > 0:
        ans += tree[i]
        i -= (i & -i)
    return ans


def update(i, diff):
    while i < len(tree):
        tree[i] += diff
        i += (i & -i)


makeFT()
print(sum(3) - sum(1))
