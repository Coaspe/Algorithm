import sys
N = int(input())
input = sys.stdin.readline


def solve():
    A, B, C = input().split()
    visited = set()

    def dfs(a, b, i):
        if a + b == len(C):
            return True
        retVal = False
        if (a, b+1, i+1) not in visited and b < len(B) and B[b] == C[i]:
            visited.add((a, b+1, i+1))
            retVal |= dfs(a, b+1, i+1)
        if retVal:
            return retVal
        if (a+1, b, i+1) not in visited and a < len(A) and A[a] == C[i]:
            visited.add((a+1, b, i+1))
            retVal |= dfs(a+1, b, i+1)

        return retVal

    return dfs(0, 0, 0)


for i in range(1, N+1):
    if solve():
        print(f"Data set {i}: yes")
    else:
        print(f"Data set {i}: no")
