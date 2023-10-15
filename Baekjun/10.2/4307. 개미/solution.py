T = int(input())

while T:
    T -= 1
    L, N = map(int, input().split())
    min_v, max_v = 0, 0

    for _ in range(N):
        x = int(input())
        min_v = max(min_v, min(x, (L - x)))
        max_v = max(max_v, max(x, (L - x)))

    print(min_v, max_v)
