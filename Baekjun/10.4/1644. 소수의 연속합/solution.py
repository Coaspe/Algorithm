N = int(input())
eratos = [True] * (N + 1)

for i in range(2, int(N**0.5) + 1):
    if eratos[i]:
        for j in range(i + i, N + 1, i):
            eratos[j] = False

primes = [i for i in range(2, N + 1) if eratos[i]]

l = r = current_sum = ans = 0

while r < len(primes):
    current_sum += primes[r]

    while current_sum > N:
        current_sum -= primes[l]
        l += 1

    if current_sum == N:
        ans += 1

    r += 1

print(ans if N != 1 else 0)
