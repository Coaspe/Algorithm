from collections import defaultdict
from heapq import heappop, heappush


def prime_factorization(n: int) -> dict[int, int]:
    factors = {}
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
        i += 2
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


num_elements = int(input())
numbers = list(map(int, input().split()))
batch_size = int(input())

factorizations = [prime_factorization(num) for num in numbers]

prime_to_indices = defaultdict(set)
for idx, factors in enumerate(factorizations):
    for prime in factors:
        prime_to_indices[prime].add(idx)

operations = []

for prime in sorted(prime_to_indices.keys()):
    candidates = []
    for idx in prime_to_indices[prime]:
        exponent = factorizations[idx][prime]
        heappush(candidates, [-exponent, idx])

    operations.append(f"ENTER {prime}")

    while candidates:
        selected_indices = []
        temp = []

        for _ in range(min(len(candidates), batch_size)):
            neg_exp, idx = heappop(candidates)
            temp.append([neg_exp, idx])
            selected_indices.append(idx + 1)

        for i in range(len(temp)):
            temp[i][0] += 1
            if temp[i][0] < 0:
                heappush(candidates, temp[i])

        operations.append(f"CLONE {' '.join(map(str, sorted(selected_indices)))}")

print("\n".join(operations))
