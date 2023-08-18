T, W = map(int, input().split())

# t초에 w번 위치를 바꾼 상태에서의 자두 최대값
dp = [[0] * (W + 1) for _ in range(T + 1)]


# W 짝수이면 1, 홀수이면 2
for t in range(1, T + 1):
    loc = int(input())
    for w in range(min(t + 1, W + 1)):
        if w == 0:
            dp[t][w] = dp[t - 1][w] + int(loc == 1)
            continue

        if (loc == 1 and w % 2 == 0) or (loc == 2 and w % 2 == 1):
            dp[t][w] = max(dp[t - 1][w - 1], dp[t - 1][w]) + 1
        else:
            dp[t][w] = max(dp[t - 1][w - 1], dp[t - 1][w])

print(max(dp[-1]))
