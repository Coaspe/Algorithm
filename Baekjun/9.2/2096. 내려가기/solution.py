import sys

input = sys.stdin.readline

N = int(input())

B = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j] => i, j로 들어오는
MAX = sys.maxsize
min_dp, max_dp = [MAX] * 3, [0] * 3

for i in range(3):
    min_dp[i] = B[0][i]
    max_dp[i] = B[0][i]

for i in range(1, N):
    max_dp_cp, min_dp_cp = max_dp[:], min_dp[:]

    for j in range(3):
        max_val, min_val = 0, MAX

        for c in j, j - 1, j + 1:
            if 0 <= c < 3:
                max_val = max(max_val, max_dp_cp[c])
                min_val = min(min_val, min_dp_cp[c])

        max_dp[j] = max_val + B[i][j]
        min_dp[j] = min_val + B[i][j]

print(max(max_dp), min(min_dp))
