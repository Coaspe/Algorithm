N = int(input())
A = list(map(int, input().split()))
dp = [[A[i]] for i in range(N)]

for i in range(len(A)-1, -1, -1):
    for j in range(i+1, len(A)):
        if A[j] > A[i] and len(dp[j]) + 1 > len(dp[i]):
            dp[i] = [A[i], *dp[j]]

x = max(dp, key=len)
print(len(x))
print(*x)
