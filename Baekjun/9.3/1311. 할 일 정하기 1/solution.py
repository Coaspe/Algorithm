N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (1 << 21) for _ in range(N)]
