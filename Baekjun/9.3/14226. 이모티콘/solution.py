S = int(input())

# 클립보드로 저장
# 클립보드에 있는 거 복사
# 화면에 한 개 삭제

# dp[i][j] -> 클립 i개이고, 화면 j개 저장할떄까지 걸리는 최소 시간

dp = [[0] * (S + 1) for _ in range(S + 1)]
for i in range(1, S + 1):
    dp[0][i] = i

for i in range(1, S + 1):
    for j in range(1, S + 1):
        dp[i][j] = min(dp[i][j])
