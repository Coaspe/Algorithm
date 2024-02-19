N, M, K = map(int, input().split())
char = [int(input()) for _ in range(N)]
char = sorted(char[:-K])
boss = [tuple(map(int, input().split())) for _ in range(K)]

for c in char:
    q = []

    while boss and boss[-1][0] > c * 15 * 60:
        pass
