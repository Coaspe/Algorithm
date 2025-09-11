from sys import stdin

input = stdin.readline

N = int(input())
A = list(map(int, input().split()))

tree = [0] * 2 * N


def update(p, value):
    p += N
    tree[p] += value
    while p > 1:
        tree[p >> 1] = tree[p] + tree[p ^ 1]
        p >>= 1


def query(left, right):
    res = 0
    left += N
    right += N
    while left < right:
        if left & 1:
            res += tree[left]
            left += 1
        if right & 1:
            right -= 1
            res += tree[right]

        left //= 2
        right //= 2

    return res


for i in range(N):
    update(i, A[i])

Q = int(input())
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        update(q[1] - 1, q[2])
    else:
        left, right = -1, N
        while right > left + 1:
            mid = (left + right) // 2
            if query(0, mid + 1) >= q[1]:
                right = mid
            else:
                left = mid
        print(right + 1)
