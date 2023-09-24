N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
i = 1 << 19

while i:
    tmp_A = [A[j] for j in range(len(A)) if A[j] & i]

    if len(tmp_A) == K:
        A = tmp_A
        break
    elif len(tmp_A) > K:
        A = tmp_A

    i >>= 1

ans = A[0]

for i in A:
    ans &= i

print(ans)
