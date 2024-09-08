T = int(input())

while T:
    T -= 1
    N = int(input())
    a = list(map(int, input().split()))
    A = [(a[i], a[i + 1]) for i in range(0, len(a), 2)]

    A.sort()
    ans = 0

    while A:
        ans += 1
        candid = []
        prev = None
        for i in range(len(A)):
            if not prev:
                prev = A[i]
                continue

            if prev[1] > A[i][1]:
                candid.append(A[i])
            else:
                prev = A[i]
        A = candid[:]
    print(ans)
