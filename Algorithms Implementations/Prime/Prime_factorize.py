import math


def prime_factorize(n, k):
    i = 2

    while i ** k <= n:
        if n % i == 0:
            n //= i
            return i, n
        i += 1

    return 1, n


t = int(input())

for _ in range(t):
    n = int(input())
    prime, n_dash = prime_factorize(n, 2)
    if n_dash % prime == 0:
        print(prime, n_dash // prime)
    else:
        print(round(math.sqrt(n_dash)), prime)
