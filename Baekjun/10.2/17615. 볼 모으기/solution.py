N = int(input())
S = input()
R = 0

for s in S:
    R += s == "R"

B = N - R

M = {"B": B, "R": R}

f = 0

for i in range(N):
    if S[i] == S[0]:
        f += 1
    else:
        break

ans = min(M[S[0]] - f, M[S[i]])

e = 0
for i in range(N - 1, -1, -1):
    if S[i] == S[-1]:
        e += 1
    else:
        break
ans = min(ans, M[S[-1]] - e, M[S[i]])

print(ans)
