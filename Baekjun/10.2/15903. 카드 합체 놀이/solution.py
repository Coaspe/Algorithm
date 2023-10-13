from bisect import insort

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

while M:
    M -= 1
    a, b = A.pop(), A.pop()
    insort(A, a + b, key=lambda x: -1 * x)
    insort(A, a + b, key=lambda x: -1 * x)

print(sum(A))
