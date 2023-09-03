import math

N = int(input())
A = list(map(int, input().split()))

ldp = [0] * N
rdp = [0] * N

for i in range(1, N):
    ldp[i] = ldp[i - 1] + max(0, A[i - 1] - A[i] + 1)
for i in range(N - 2, -1, -1):
    rdp[i] = rdp[i + 1] + max(0, A[i + 1] - A[i] + 1)

ans = math.inf

for i in range(N):
    ans = min(ans, max(ldp[i], rdp[i]))

print(ans)
