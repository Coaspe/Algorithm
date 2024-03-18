for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    D = [0] * N
    p, q = 0, int(1e9)
    for i in range(N):
        D[C[i]] = i

    for i in range(N - 1):
        a, b = D[i], D[i + 1]

        if B[a] == B[b]:
            if A[a] <= A[b]:
                q = -1
                break
        elif B[a] < B[b]:
            if A[a] <= A[b]:
                q = -1
                break
            q = min(q, (A[a] - A[b]) / (B[b] - B[a]))
        elif A[a] < A[b]:
            p = max(p, (A[b] - A[a]) // (B[a] - B[b]) + 1)

    print(p if p < q else -1)
