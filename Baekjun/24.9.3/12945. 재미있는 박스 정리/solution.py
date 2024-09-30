N = int(input())
A = [int(input()) for _ in range(N)]
A.sort()

l, r = 0, N // 2

ans = 0

while l < N // 2 and r < N:
    if A[r] // A[l] >= 2:
        ans += 1
        l += 1
    r += 1
print(len(A) - ans)
