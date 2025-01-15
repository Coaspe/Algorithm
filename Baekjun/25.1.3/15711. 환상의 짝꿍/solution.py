import math
import sys

input = sys.stdin.readline


def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def power(x, y, p):
    res = 1

    x = x % p
    while y > 0:
        if y & 1:
            res = res * x % p

        y = y >> 1
        x = (x * x) % p

    return res


def miller_rabin(n, a):
    d = n - 1
    while d % 2 == 0:
        d //= 2

    x = pow(a, d, n)

    if x == 1 or x == n - 1:
        return True

    while d != n - 1:
        x = pow(x, 2, n)
        d *= 2

        if x == 1:
            return False
        if x == n - 1:
            return True

    return False


def isPrime(n):
    if n in [2, 7, 61]:
        return True

    if n == 1 or n % 2 == 0:
        return False

    for a in [2, 7, 61]:
        if not miller_rabin(n, a):
            return False

    return True


def check_sum_of_primes(a, b):
    total = a + b
    if total == 2:
        return "NO"
    if total % 2 == 0:
        return "YES"
    return "YES" if isPrime(total - 2) else "NO"


results = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    results.append(check_sum_of_primes(a, b))

print("\n".join(results))
