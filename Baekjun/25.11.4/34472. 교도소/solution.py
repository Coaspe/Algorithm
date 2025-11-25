N = int(input())
A = list(map(int, input().split()))


T = sum(A) // N

S = 0
ans = 0

for i in list(range(N)) + list(range(N)):
    diff = A[i] - T

    prev_S = S
    S = max(0, S + diff)

    if S == 0:
        A[i] += prev_S
    else:
        A[i] = T

    ans += S

print(ans)
