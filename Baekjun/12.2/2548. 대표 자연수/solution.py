N = int(input())
A = list(map(int, input().split()))

if N == 1:
    print(A[0])
    exit(0)

A.sort()
A1 = A[N // 2]

if N % 2 == 0:
    tmp = 0

    for a in A:
        tmp += abs(A1 - a)

    A2 = A[N // 2 - 1]
    tmp2 = 0

    for a in A:
        tmp2 += abs(A2 - a)

    if tmp2 <= tmp:
        A1 = A2

print(A1)
