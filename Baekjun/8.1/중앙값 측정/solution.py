from collections import deque
import math

N, K = map(int, input().split())
n = 2 ** math.ceil(math.log2(65536))
tree = [0] * 2 * n
dq = deque()
ans = 0

K -= 1
N -= K

for i in range(K):
    dq.append(int(input()))
    tree[n + dq[i]] += 1

for i in range(n - 1, 0, -1):
    tree[i] = tree[i * 2] + tree[i * 2 + 1]


def update(A):
    global tree

    while A > 1:
        A //= 2
        tree[A] = tree[A * 2] + tree[A * 2 + 1]


K = (K + 2) // 2

for _ in range(N):
    A = int(input())
    dq.append(A)
    A += n
    tree[A] += 1
    update(A)

    A = K
    B = 1

    while B < n:
        B *= 2

        if tree[B] < A:
            A -= tree[B]
            B += 1

    ans += B - n

    A = dq.popleft() + n
    tree[A] -= 1
    update(A)

print(ans)


"""
"""

import sys

input = sys.stdin.readline
from collections import deque


def op(a, b):
    return a + b


e = 0


def update(L_seg, l, b, c):
    i = (1 << l) + b
    L_seg[i] += c
    i //= 2
    while i > 0:
        L_seg[i] = op(L_seg[i * 2], L_seg[i * 2 + 1])
        i //= 2
    L_seg[0] = L_seg[1]
    return L_seg


def k_th(L_seg, l, k):
    i = 1
    while i < (1 << l):
        i *= 2
        if L_seg[i] >= k:
            pass
        else:
            k -= L_seg[i]
            i += 1
    return i - (1 << l)


n, k = map(int, input().split())

d = deque()

ans = 0

l = 16

L_seg = [e] * (2 * (1 << l))
for _ in range(k):
    temp = int(input())
    L_seg[(1 << l) + temp] += 1
    d.append(temp)
for i in range((1 << l) - 1, -1, -1):
    L_seg[i] = op(L_seg[i * 2], L_seg[i * 2 + 1])

ans += k_th(L_seg, l, (k + 1) // 2)

for _ in range(n - k):
    temp = int(input())
    L_seg = update(L_seg, l, temp, 1)
    d.append(temp)
    temp = d.popleft()
    L_seg = update(L_seg, l, temp, -1)

    ans += k_th(L_seg, l, (k + 1) // 2)

print(ans)
