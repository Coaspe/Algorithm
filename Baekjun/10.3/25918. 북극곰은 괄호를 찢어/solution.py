N = int(input())
S = input()

n = 0
ans = 0

for i in range(N):
    if S[i] == "(":
        n += 1
    else:
        n -= 1
    ans = max(ans, abs(n))
if n:
    print(-1)
else:
    print(ans)
