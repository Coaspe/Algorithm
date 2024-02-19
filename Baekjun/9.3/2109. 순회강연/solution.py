from sys import stdin

input = stdin.readline
N = int(input())

if N == 0:
    print(0)
    exit(0)

A = [list(map(int, input().split())) for _ in range(N)]

A.sort(key=lambda x: -x[0])
max_date = max(A, key=lambda x: x[1])[1]

assign = [0] * (max_date + 1)

ans = 0

for reward, limit in A:
    for i in range(limit, 0, -1):
        if not assign[i]:
            assign[i] = 1
            ans += reward
            break
print(ans)
