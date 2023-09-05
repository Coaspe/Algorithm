N, K = map(int, input().split())
a = list(map(int, input().split()))
dp = [2] * (K + 1)


for i in range(1, K + 1):
    for m in a:
        if m > i:
            continue
        if dp[i - m] == 2:
            dp[i] = 1

# 4 -> 3 2 1

print("First" if dp[K] == 1 else "Second")
