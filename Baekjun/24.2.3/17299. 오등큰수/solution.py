import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))

frequency = Counter(A)

NGF = [-1] * N

stack = []
for i in range(N):
    while stack and frequency[A[stack[-1]]] < frequency[A[i]]:
        NGF[stack.pop()] = A[i]
    stack.append(i)
    print(stack)

print(" ".join(map(str, NGF)))
