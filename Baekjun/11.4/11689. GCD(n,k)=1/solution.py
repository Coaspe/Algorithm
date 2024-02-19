from collections import defaultdict


def factorization(x):
    d = 2
    factorization = defaultdict(int)
    while d * d <= x:
        while (x % d) == 0:
            factorization[d] += 1
            x //= d
        d += 1
    if x > 1:
        factorization[x] += 1
    return factorization


def euler_phi(n):
    primes = factorization(n)
    k = 1
    for p in primes.keys():
        power = p ** (primes[p] - 1)
        k *= power * (p - 1)
    return k


input_number = int(input())
print(euler_phi(input_number))
