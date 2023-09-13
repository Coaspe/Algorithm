S = input()
dp = [[0] * len(S) for _ in range(len(S))]
MOD = 10007


def solve(s, e):
    if s > e:
        return 0
    if s == e:
        return 1

    if dp[s][e]:
        return dp[s][e]

    dp[s][e] = (solve(s, e - 1) + solve(s + 1, e) - solve(s + 1, e - 1)) % MOD

    # 맨 왼, 오른쪽이 같으면 그 안에 포함되는 모든 펠린드롬을 사용하여 새로운 팰린드롬을 만들 수 있음
    # 거기에 맨 왼, 맨 오른쪽만 사용한 경우 => +1
    if S[s] == S[e]:
        dp[s][e] = (dp[s][e] + solve(s + 1, e - 1) + 1) % MOD

    return dp[s][e]


print(solve(0, len(S) - 1))

##################################################
s = input()
ll = len(s)

# dp[i] = i 이후로 존재하는 팰린드롬의 수
dp = [1]

"""
a b a b c c b
"""
for x in range(1, ll):
    c = 1
    for y in range(x - 1, -1, -1):
        if s[x] == s[y]:
            dp[y] += c
            dp[y] %= 10007
            c = dp[y]
        else:
            c += dp[y]
        # print(c, dp)

    dp.append(1)

print(dp)
print(sum(dp) % 10007)
