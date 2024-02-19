# import sys

# T = int(sys.stdin.readline())
# inf = 10**9

# for _ in range(T):
#     N, M = map(int, sys.stdin.readline().split())

#     notes = []
#     dp = [inf] * (N + 1)
#     dp[0] = 0
#     ans = inf

#     for _ in range(M):
#         s, p, o = map(int, sys.stdin.readline().split())
#         notes.append([s, p, o])

#     notes.sort(key=lambda x: x[1])

#     for i in range(M):
#         s, p, o = notes[i][0], notes[i][1], notes[i][2]

#         for j in range(N, -1, -1):
#             if j + s >= N:
#                 ans = min(ans, dp[j] + (N - j) * p + o)
#             if j >= s:
#                 dp[j] = min(dp[j], dp[j - s] + s * p + o)

#     print(ans)


import sys

inf = 1000

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    dp = [inf] * (N + 1)

    info = [list(map(int, input().split())) for _ in range(M)]

    info.sort(key=lambda x: x[1])

    dp[0] = 0

    for s, p, o in info:
        for j in range(N - 1, -1, -1):
            num = min(N, j + s)
            dp[num] = min(dp[num], dp[j] + o + (num - j) * p)
            print(dp)

    print(dp[N])
