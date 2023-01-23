arr = [1, 12, -5, -6, 50, 3]
arr.insert(0, 0)
tree = [0]*(len(arr))


def update(i, diff):
    while i < len(tree):
        tree[i] += diff
        i += (i & -i)


for i in range(1, len(arr)):
    update(i, arr[i])


def sum(i):
    ans = 0
    while i > 0:
        ans += tree[i]
        i -= (i & -i)
    return ans


print(tree)
print(sum(3))
