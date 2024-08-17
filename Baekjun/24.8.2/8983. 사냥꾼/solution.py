from bisect import bisect_left

M, N, L = map(int, input().split())

A = sorted(map(int, input().split()))
ans = 0
for _ in range(N):
    x, y = map(int, input().split())
    idx = bisect_left(A, x)
    idxn = idx - 1

    if idx < M and (abs(x - A[idx]) + y) <= L:
        ans += 1
        continue

    if idxn >= 0:
        ans += int((abs(x - A[idxn]) + y) <= L)

print(ans)
