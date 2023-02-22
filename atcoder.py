import math
t = int(input())


def gcd(a, b):
    return math.gcd(a, b)


for i in range(t):
    # 4 2 1
    N, D, K = map(int, input().split())
    cycle_len = N // gcd(N, D)
    c = (K-1) // cycle_len
    idx = (c + (K-1) * D) % N
    print(idx)
