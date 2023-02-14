N = int(input())
abc = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[0, 0, 0] for _ in range(N)]
dp[N-1] = abc[N-1][:]
for i in range(N-2, -1, -1):
    dp[i][0] = max(dp[i+1][1]+abc[i][0], dp[i+1][2]+abc[i][0])
    dp[i][1] = max(dp[i+1][2]+abc[i][1], dp[i+1][0]+abc[i][1])
    dp[i][2] = max(dp[i+1][1]+abc[i][2], dp[i+1][0]+abc[i][2])

print(max(dp[0]))
