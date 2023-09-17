import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
dp = [[0] * N for _ in range(2)]

# dp[0][i] : 특정 원소를 제거하지 않은 경우
# dp[1][i] : 특정 원소를 제거한 경우 (현재 or 이전)
dp[0][0] = arr[0]  # 1개는 반드시 선택해야 한다.

ans = arr[0]
for i in range(1, N):
    dp[0][i] = max(dp[0][i - 1] + arr[i], arr[i])
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + arr[i])
    ans = max(ans, dp[0][i], dp[1][i])

print(ans)
