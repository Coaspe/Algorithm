N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

activated = 0
ans = 0

for a in A:
    ans += a * activated
    if activated < K:
        activated += 1
print(ans)
