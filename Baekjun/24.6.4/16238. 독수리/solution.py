N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
ans = 0

acc = 0
acc_sub = 0

for i, a in enumerate(A):
    acc += a
    acc_sub += i
    ans = max(ans, acc - acc_sub)

print(ans)
