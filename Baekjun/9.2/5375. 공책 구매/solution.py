import sys

T = int(sys.stdin.readline())
inf = 10**9

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())

    notes = []
    dp = [inf] * (N + 1)
    dp[0] = 0
    ans = inf

    for _ in range(M):
        notes.append(list(map(int, sys.stdin.readline().split())))

    # 단가가 가장 낮은 쇼핑몰부터
    notes.sort(key=lambda x: x[1])

    for s, p, o in notes:
        for j in range(N, -1, -1):
            if j + s >= N:
                ans = min(ans, dp[j] + (N - j) * p + o)
            if j >= s:
                dp[j] = min(dp[j], dp[j - s] + s * p + o)
        print(dp)

    print(ans)
