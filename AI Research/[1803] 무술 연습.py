from collections import deque

M, N = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

hit = [0] * (M + 1)

for a in B:
    hit[a] += 1

q = deque()
for i in range(1, M + 1):
    if hit[i] == 0:
        q.append(i)

AX = [0] * (M + 1)
BX = [1] * (N + 1)

while q:
    a = q.popleft()

    b = A[a - 1]

    AX[a] = 1

    if BX[b] == 1:
        next_a = B[b - 1]
        hit[next_a] -= 1
        if hit[next_a] == 0:
            q.append(next_a)

    BX[b] = 0

print(*AX[1:])
print(*BX[1:])
