N = int(input())
A = [int(input()) for _ in range(N)]
A.sort(reverse=True)


score = 0
ans = 0

for i in range(N):
    if A[i] + N >= score:
        ans += 1

    score = max(score, A[i] + i + 1)

print(ans)
