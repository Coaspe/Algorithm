N = int(input())
# dp[0][i] i를 포함하지 않는 최대값
# dp[1][i] i를 포함하는 최대값
dp = [[0] * 2 for _ in range(N)]
arr = [int(input()) for _ in range(N)]

if N == 1:
    print(arr[0])
    exit(0)

dp[0][1] = arr[0]
dp[1][0] = arr[0]
dp[1][1] = arr[0] + arr[1]

for i in range(2, N):
    # i번째 요소를 포함하지 않는다면, 이전의 요소를 포함 또는 포함하지 않는 경우 중에 최대값을 가져간다.
    dp[i][0] = max(dp[i - 1])

    # i번째 요소를 포함한다면,
    # 1. i-1 번째 요소를 포함하지 않는 경우
    # 2. i-2 번째 요소를 포함하지 않는 경우에 i - 1번째 요소를 더한 경우
    # 위 두 경우에 i번째 요소를 더해서 할당한다.
    dp[i][1] = max(dp[i - 1][0], dp[i - 2][0] + arr[i - 1]) + arr[i]

print(max(dp[-1]))
