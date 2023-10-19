N, L = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

A.sort(reverse=True)
ans = 0
l = 0

while A:
    x, y = A.pop()
    if l < x:
        l = x
    while y > l:
        l += L
        ans += 1

print(ans)
