N = int(input())
arr = list(map(int, input().split()))

total = 0
sa = []
for i in arr:
    total += i
    sa.append(total)
print(sa)
if total % 4 != 0:
    print(0)
else:
    dp = [1, 0, 0, 0]
    quater = total // 4
    for i in range(N - 1):
        for j in range(3, 0, -1):
            if sa[i] == quater * j:
                dp[j] += dp[j - 1]
        print(dp, i, sa[i])
