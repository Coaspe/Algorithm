from collections import defaultdict

T = int(input())
len_a = int(input())
A = list(map(int, input().split()))
len_b = int(input())
B = list(map(int, input().split()))

p_a = [A[0]]
p_b = [B[0]]

for i in range(1, len_a):
    p_a.append(p_a[-1] + A[i])
for i in range(1, len_b):
    p_b.append(p_b[-1] + B[i])

d_a = defaultdict(int)
for i in range(len_a):
    d_a[p_a[i]] += 1
    for j in range(i):
        d_a[p_a[i] - p_a[j]] += 1

ans = 0

d_b = defaultdict(int)
for i in range(len_b):
    if T - p_b[i] in d_a:
        ans += d_a[T - p_b[i]]
    for j in range(i):
        if T - (p_b[i] - p_b[j]) in d_a:
            ans += d_a[T - (p_b[i] - p_b[j])]

print(ans)
