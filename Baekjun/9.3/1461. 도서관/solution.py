N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
C = abs(A[0]) > abs(A[-1])
ns = M * int(C)
ps = N - 1 - M * int(not C)
ans = abs(A[0]) if C else abs(A[-1])

# 왼쪽에서 끝
if A[0] < 0:
    for i in range(ns, N, M):
        if A[i] * A[0] <= 0:
            break
        ans += abs(A[i]) * 2

if A[-1] > 0:
    for i in range(ps, -1, -M):
        if A[i] * A[-1] <= 0:
            break
        ans += abs(A[i]) * 2
print(ans)
