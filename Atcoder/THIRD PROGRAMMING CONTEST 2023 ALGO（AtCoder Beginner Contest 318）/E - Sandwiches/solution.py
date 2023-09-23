N = int(input())
A = list(map(int, input().split()))

cnt = [0] * (N + 1)

for a in A:
    cnt[a] += 1

left = [0] * (N + 1)
total = 0
ans = 0

for a in A:
    ans += total - left[a] * (cnt[a] - left[a])
    total -= left[a] * (cnt[a] - left[a])
    left[a] += 1
    total += left[a] * (cnt[a] - left[a])

print(ans)
