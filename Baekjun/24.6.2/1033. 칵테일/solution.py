N = int(input())
A = [[] for _ in range(N)]
P = [0] * N
lcm = 1


def gcd(a, b):
    if not b:
        return a
    else:
        return gcd(b, a % b)


for _ in range(N - 1):
    a, b, p, q = map(int, input().split())
    A[a].append((b, p, q))
    A[b].append((a, q, p))
    lcm *= (p * q) // (gcd(p, q))

V = [0] * N


def dfs(n):
    for a, p, q in A[n]:
        if not V[a]:
            V[a] = 1
            P[a] = P[n] * q // p
            dfs(a)


P[0] = lcm

V[0] = 1
dfs(0)

mgcd = P[0]

for i in range(1, N):
    mgcd = gcd(mgcd, P[i])

for i in range(N):
    P[i] //= mgcd

print(*P)
