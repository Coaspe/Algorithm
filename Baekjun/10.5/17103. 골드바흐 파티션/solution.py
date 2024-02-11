from math import sqrt, ceil

T = int(input())
nums = [int(input()) for _ in range(T)]
max_N = max(nums)

eratos = [0, 0] + [1] * (max_N - 1)
primes = set()

for i in range(2, max_N + 1):
    if eratos[i]:
        primes.add(i)

    for j in range(2 * i, max_N + 1, i):
        eratos[j] = 0

for n in nums:
    ans = 0
    for p in primes:
        if n - p < n // 2:
            break
        ans += (n - p) in primes

    print(ans)
