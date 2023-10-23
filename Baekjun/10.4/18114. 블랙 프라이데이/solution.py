from bisect import bisect_left

N, C = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
l, r = 0, N - 1

while r > l:
    if A[r] == C or A[l] == C or A[r] + A[l] == C:
        print(1)
        exit(0)

    if A[r] + A[l] > C:
        r -= 1
        continue

    idx = bisect_left(A, C - A[l] - A[r])

    if idx == N:
        l += 1
        continue

    S = A[idx] + A[l] + A[r]

    if S < C or A[idx] == A[r]:
        l += 1
    elif S > C or A[idx] == A[l]:
        r -= 1
    elif S == C:
        print(1)
        exit(0)

print(0)
