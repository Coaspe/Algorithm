from sys import stdin

input = stdin.readline

while 1:
    N, a, b = map(int, input().split())
    if N == a == b == 0:
        break
    teams = [list(map(int, input().split())) for _ in range(N)]

    teams.sort(key=lambda x: -abs(x[1] - x[2]))
    ans = 0

    for k, x, y in teams:
        if x <= y:
            val = min(k, a)
        else:
            val = k - min(k, b)
        ans += val * x + (k - val) * y
        a -= val
        b -= k - val

    print(ans)
