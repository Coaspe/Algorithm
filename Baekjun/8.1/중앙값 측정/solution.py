from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
n = 65536
tree = [0 for _ in range(n * 2)]
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

    while A >= 1:
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
