MOD = 1000000007


def countKMultiples(N, M, K, chosen_digits):
    dp = [[0] * K for _ in range(M + 1)]
    # dp[i][j]는 i 자리 양의 정수를 만들 때, 나머지가 j인 경우의 수를 나타냅니다.

    # 맨 앞 자리를 제외한 숫자로 1자리 양의 정수를 만드는 경우
    for i in range(N):
        if chosen_digits[i] != 0:
            dp[1][chosen_digits[i] % K] += 1

    # M자리 양의 정수를 만들기 위해
    # 이전 자리의 나머지에 따라 경우의 수를 누적합니다.
    for i in range(2, M + 1):
        for j in range(N):
            for k in range(K):
                dp[i][(k * 10 + chosen_digits[j]) % K] += dp[i - 1][k]
                dp[i][(k * 10 + chosen_digits[j]) % K] %= MOD

    return dp[M - 1][0]


# ab % K = k
# (ab*10 + c) % K
#  ab = z * K + k
# (10*K*z+k*10 + c) % K
# (K*10 + c) % K
N, M, K = map(int, input().split())
chosen_digits = list(map(int, input().split()))

result = countKMultiples(N, M, K, chosen_digits)
print(result)
