w, n = map(int, input().split())

A = list(map(int, input().split()))

dp = [False] * w

for i in range(n):
    for j in range(i+1, n):
        if A[i] + A[j] < w and dp[w - A[i] - A[j]]:
            print("YES")
            exit(0)

    for j in range(i):
        if A[i] + A[j] < w:
            dp[A[i] + A[j]] = True

print("NO")
