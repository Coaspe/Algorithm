def q(x):
    for i in range(1, 9):
        if x in dp[i]:
            return i

    return "NO"


def monodigital(x):
    if x == 1:
        dp[x] = {K}
    elif len(dp[x]) == 0:
        tmp = set()
        tmp.add(int(str(K) * x))

        for k in range(1, x):
            left, right = dp[x - k], dp[k]

            for l in left:
                for r in right:
                    tmp.add(l + r)
                    tmp.add(l - r)
                    tmp.add(l * r)
                    if r:
                        tmp.add(l // r)
        dp[x] = tmp


K = int(input())
dp = [{} for _ in range(9)]

for x in range(1, 9):
    monodigital(x)
for _ in range(int(input())):
    print(q(int(input())))
