N, K = map(int, input().split())
A = list(map(int, input().split()))

B = [[0, 0] for _ in range(N)]


l, r = 0, 0
s = A[0]

while r < N:
    if s < K:
        r += 1
        if r < N:
            s += A[r]
    elif s >= K:
        B[l][0] = r
        B[l][1] = s
        s -= A[l]
        l += 1
        if l > r:
            r = l
            if r < N:
                s = A[r]

dp = [0] * (N + 1)


for i in range(N - 1, -1, -1):
    r, s = B[i]
    dp[i] = max(dp[i + 1], dp[r + 1] + s - K)

print(dp[0])
