n, k = map(int, input().split())
s = [0] + list(map(int, input().split()))

# dp[i][j] = i 번째 인덱스 이전에 짝수 숫자로 끝나는
# 가장 긴 짝수 부분 수열 중 j 개의 홀수를 지운 것의 길이
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    s2 = s[i] % 2
    for j in range(k + 1):
        if s2 == 0:  # 짝수일 때
            dp[i][j] = dp[i - 1][j] + 1
        elif j != 0:  # 홀수일 때
            dp[i][j] = dp[i - 1][j - 1]

print(max([i[k] for i in dp]))
