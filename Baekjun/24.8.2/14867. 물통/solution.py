from collections import deque

A, B, TA, TB = map(int, input().split())

C = set()


C.add((0, 0))
q = deque([(0, 0, 0)])


def add(a, b):
    if (a, b) not in C:
        C.add((a, b))
        q.append((a, b, c + 1))


while q:
    a, b, c = q.popleft()
    if a == TA and b == TB:
        print(c)
        exit(0)

    add(0, b)
    add(a, 0)
    add(A, b)
    add(a, B)
    add(min(A, a + b), max(0, b - (A - a)))
    add(max(0, a - (B - b)), min(B, a + b))
print(-1)
