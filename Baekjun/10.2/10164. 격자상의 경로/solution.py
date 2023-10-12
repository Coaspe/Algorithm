N, M, K = map(int, input().split())

if K == 1:
    R, C = 0, 0
elif K == 0:
    R, C = N - 1, M - 1
else:
    K -= 1
    R, C = K // M, K % M

dp1 = [[0] * (C + 1) for _ in range(R + 1)]

dp1[0][0] = 1

for i in range(R + 1):
    for j in range(C + 1):
        if i >= 1:
            dp1[i][j] += dp1[i - 1][j]
        if j >= 1:
            dp1[i][j] += dp1[i][j - 1]

if N != R:
    dp2 = [[0] * (M - C) for _ in range(N - R)]
    dp2[0][0] = dp1[-1][-1]

    for i in range(N - R):
        for j in range(M - C):
            if i >= 1:
                dp2[i][j] += dp2[i - 1][j]
            if j >= 1:
                dp2[i][j] += dp2[i][j - 1]

    print(dp2[-1][-1])
else:
    print(dp1[-1][-1])
