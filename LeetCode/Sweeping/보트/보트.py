arr = []
N, M = map(int, input().split())
answer = M

for _ in range(N):
    a, b = map(int, input().split())
    if a > b:
        arr.append((b, a))
arr.sort()

lo, hi = arr[0]

for a, b in arr:
    if a > hi:
        answer += 2*(hi-lo)
        lo, hi = a, b
    hi = max(hi, b)
answer += 2*(hi-lo)

print(answer)
