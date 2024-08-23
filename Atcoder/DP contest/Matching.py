import sys

input = sys.stdin.readline

N = int(input())

MOD = 1e9 + 7
MAX_N = 21
compat = [[0] * MAX_N for _ in range(MAX_N)]

for i in range(N):
    for j, val in enumerate(list(map(int, input().split()))):
        compat[i][j] = val

# S에 속하는 여성들이 처음 부터 |S| 번째까지의 남성들과 매칭할 수 있는 경우의 수.
dp = [0] * (1 << MAX_N)

dp[0] = 1

for s in range(1 << N):
    pair_num = s.bit_count()
    for w in range(N):
        if (s & (1 << w)) or not compat[pair_num][w]:
            continue

        dp[s | (1 << w)] += dp[s]
        dp[s | (1 << w)] %= MOD

print(int(dp[(1 << N) - 1]))
