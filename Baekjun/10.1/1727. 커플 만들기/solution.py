N, M = map(int, input().split())
man = list(map(int, input().split()))
woman = list(map(int, input().split()))

man.sort()
woman.sort()

d = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        d[i][j] = d[i - 1][j - 1] + abs(man[i - 1] - woman[j - 1])
        if i > j:
            d[i][j] = min(d[i][j], d[i - 1][j])
        elif i < j:
            d[i][j] = min(d[i][j], d[i][j - 1])

print(d[N][M])
