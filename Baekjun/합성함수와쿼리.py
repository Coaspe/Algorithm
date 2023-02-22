import sys
m = int(sys.stdin.readline())
f = [0]+list(map(int, sys.stdin.readline().split()))

# 1 < m <= 200000 logm = 17.609...

DP = [[f[i]] for i in range(m+1)]
for j in range(1, 19):
    for i in range(1, m+1):
        DP[i].append(DP[DP[i][j-1]][j-1])

Q = int(sys.stdin.readline())

for _ in range(Q):
    n, x = map(int, sys.stdin.readline().split())
    for j in range(18, -1, -1):
        if n >= 1 << j:  # 2^j 보다 크다면
            n -= 1 << j  # 2^j 을 빼주고 나머지를 계산해준다.
            x = DP[x][j]  # 0이 될때까지 반복
    print(x)
