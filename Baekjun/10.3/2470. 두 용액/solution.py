N = int(input())
A = list(map(int, input().split()))

A.sort()
ans = (0, N - 1, 2 * 10**9)

l, r = 0, N - 1

while l < r:
    val = A[l] + A[r]

    if abs(ans[2]) > abs(val):
        ans = min(ans, (l, r, val), key=lambda x: abs(x[2]))

    if val > 0:
        r -= 1
    elif val < 0:
        l += 1
    else:
        break

print(A[ans[0]], A[ans[1]])
