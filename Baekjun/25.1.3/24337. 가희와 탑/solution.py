N, A, B = map(int, input().split())

ans = [1]

A -= 1
B -= 1
flag = B > A

if flag:
    A, B = B, A

for _ in range(A):
    if not ans:
        ans.append(1)
    else:
        ans.append(ans[-1] + 1)

while B:
    ans.append(B)
    B -= 1


if flag:
    ans = ans[::-1]

left = N - len(ans)
if left > 0:
    if ans[0] == 1:
        ans = [1] * left + ans
    else:
        ans = [ans[0]] + [1] * left + ans[1:]

if len(ans) == N:
    print(*ans)
else:
    print(-1)
