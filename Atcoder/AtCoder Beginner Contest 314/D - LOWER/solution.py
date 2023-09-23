import sys

input = sys.stdin.readline

N = int(input())
S = list(input())
Q = int(input())

query = []

last_invert = -1

for idx in range(Q):
    a, b, c = input().split()
    a, b = int(a), int(b)

    if a != 1:
        last_invert = idx

    query.append((a, b, c))

for idx, (a, b, c) in enumerate(query):
    if a == 1:
        S[b - 1] = c
    elif idx == last_invert:
        for i in range(N):
            S[i] = S[i].lower() if query[last_invert][0] == 2 else S[i].upper()

print("".join(S))
