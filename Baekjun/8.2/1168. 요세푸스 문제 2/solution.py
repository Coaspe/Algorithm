# N, K = map(int, input().split())
# arr = list(range(1, N + 1))
# tree = [0] * 2 * N
# """
# 1,2,3,4,5,6,7
# 1,2,4,5,6,7
# 1,2,4,5,7
# 1,4,5,7
# 1,4,5
# 1,4
# """
# for i in range(N):
#     tree[i + N] = arr[i]

# for i in range(N - 1, 0, -1):
#     tree[i] = tree[2 * i] + tree[2 * i + 1]


# def update(p):
#     p += N

#     tree[p] -= 1

#     while p > 1:
#         tree[p >> 1] = tree[p] + tree[p ^ 1]
#         p >>= 1


# # [l, r)
# def query(l, r):
#     ans = 0

#     l += N
#     r += N

#     while r > l:
#         if l & 1:
#             ans += tree[l]
#             l += 1

#         if r & 1:
#             r -= 1
#             ans += tree[r]

#         l >>= 1
#         r >>= 1

#     return ans


# pointer = 0
# ans = []

# for _ in range(N):
#     # pointer to end
#     A = K
#     B = 1

#     while B < N:
#         B *= 2

#         if tree[B] < A:
#             A -= tree[B]
#             B += 1

#     p = B - N

#     left = query(0, pointer)

#     tree[A] -= 1
#     update(A)


import sys
import math

input = sys.stdin.readline


def update(node, diff):
    tree[node] += diff
    while node > 1:
        node //= 2
        tree[node] = tree[node * 2] + tree[node * 2 + 1]


def pop(node, index):
    while node < size:
        node *= 2

        if tree[node] < index:
            index -= tree[node]
            node += 1

    res.append(node - size + 1)
    update(node, -1)


# tree[size + i]
N, K = map(int, input().split())
# size = 2 ** math.ceil(math.log2(N))
size = N
tree = [0] * (2 * size)

for i in range(N):
    tree[size + i] += 1

for i in range(size - 1, 0, -1):
    tree[i] = tree[2 * i + 1] + tree[2 * i]

# 1,2,3,4,5,6,7
# 1,2,4,5,6,7
# 1,2,4,5,7
res = []
target = 1
while tree[1]:
    target += K - 1
    print(target)
    target = tree[1] if target % tree[1] == 0 else target % tree[1]
    print(tree, target)
    pop(1, target)
    print(tree)
print(tree)
print(f'<{(", ").join(map(str, res))}>')
