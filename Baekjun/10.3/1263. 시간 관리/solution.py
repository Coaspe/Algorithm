N = int(input())
TS = [list(map(int, input().split())) for _ in range(N)]
TS.sort(key=lambda x: x[1])
ans = TS[0][1] - TS[0][0]
while ans >= 0:
    last = ans + TS[0][0]
    for idx, (t, s) in enumerate(TS[1:]):
        if t + last > s:
            break
        last += t
        if idx == N - 2:
            print(ans)
            exit(0)
    ans -= 1

print(-1)
