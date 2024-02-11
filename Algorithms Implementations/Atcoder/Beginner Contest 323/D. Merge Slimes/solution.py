from collections import defaultdict

N = int(input())
slimes = defaultdict(int)

S = []

for _ in range(N):
    s, c = map(int, input().split())
    S.append(s)
    slimes[s] = c

S.sort()
ans = 0

for s in S:
    while slimes[s]:
        m, d = divmod(slimes[s], 2)
        slimes[s] = 0
        ans += d
        s <<= 1
        slimes[s] += m
print(ans)
