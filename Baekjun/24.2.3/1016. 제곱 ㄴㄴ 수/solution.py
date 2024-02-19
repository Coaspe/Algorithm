import math

MIN, MAX = map(int, input().split())
N = math.ceil(math.sqrt(MAX))
prime = [True] * (N + 1)
prime[1] = False

sq = []

for i in range(2, N + 1):
    if prime[i] == True:
        sq.append(i * i)
        j = 2
        while i * j <= N:
            prime[i * j] = False
            j += 1

prime = [True] * (MAX - MIN + 1)

for i in sq:
    j = 1

    if i * j < MIN:
        j = math.ceil(MIN / i)

    while i * j <= MAX:
        prime[i * j - MIN] = False
        j += 1

print(prime.count(True))
