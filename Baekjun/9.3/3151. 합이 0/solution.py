from bisect import bisect_left, bisect_right

N = int(input())
A = list(map(int, input().split()))

A.sort()
ans = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        S = A[i] + A[j]

        l = bisect_left(A, -S, j + 1, N)
        r = bisect_right(A, -S, j + 1, N)

        ans += r - l

print(ans)
