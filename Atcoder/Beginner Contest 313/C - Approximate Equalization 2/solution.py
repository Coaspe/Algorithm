n = int(input())
a = list(map(int, input().split()))
sum = sum(a)
a.sort()
b = [sum // n] * n
for i in range(0, sum % n):
    b[n - 1 - i] += 1
ans = 0
for i in range(0, n):
    ans += abs(a[i] - b[i])
print(ans // 2)
