def solution(temperature, t1, t2, a, b, onboard):
    OFFSET = 10
    temperature += OFFSET
    t1 += OFFSET
    t2 += OFFSET

    INF = float("inf")
    T = len(onboard)
    dp = [[INF] * 53 for _ in range(T + 1)]

    dp[0][temperature] = 0
    temp_range_onboard = range(t1, t2 + 1)
    temp_range_not_onboard = range(51)

    for curr_time in range(T):
        temp = temp_range_not_onboard if not onboard[curr_time] else temp_range_onboard
        for t in temp:
            dp[curr_time + 1][t] = min(
                dp[curr_time][t - 1] if t - 1 < temperature else INF,
                dp[curr_time][t + 1] if t + 1 > temperature else INF,
                dp[curr_time][t] if t == temperature else INF,
                dp[curr_time][t] + b,
                dp[curr_time][t - 1] + a,
                dp[curr_time][t + 1] + a,
            )

    return min(dp[-1])
