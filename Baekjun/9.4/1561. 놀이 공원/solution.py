from functools import reduce

# N: 사람 수, M: 놀이기구 수
N, M = map(int, input().split())
A = list(map(int, input().split()))

if N <= M:
    print(N)
    exit(1)

l, r = 1, max(A) * N

tmp = r
while r > l + 1:
    time = (l + r) // 2
    if reduce(lambda acc, cur: acc + time // cur, A, M) >= N:
        r = time
        tmp = min(tmp, r)
    else:
        l = time

cnt = reduce(lambda acc, cur: acc + (tmp - 1) // cur, A, M)

for i in range(M):
    if not tmp % A[i]:
        cnt += 1
    if cnt == N:
        print(i + 1)
        break
