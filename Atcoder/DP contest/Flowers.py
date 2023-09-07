N = int(input()) + 1
H = [0] + list(map(int, input().split()))
A = [0] + list(map(int, input().split()))

tree = [0] * N


def update(i, val):
    while i < N:
        tree[i] = max(tree[i], val)
        i += i & -i


def query(i):
    val = 0
    while i > 0:
        val = max(val, tree[i])
        i -= i & -i
    return val


for i in range(1, N):
    update(H[i], query(H[i] - 1) + A[i])

print(query(N - 1))
