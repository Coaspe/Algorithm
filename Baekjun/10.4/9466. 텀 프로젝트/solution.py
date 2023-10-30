from sys import stdin, setrecursionlimit

input = stdin.readline

setrecursionlimit(10**5)

T = int(input())
while T:
    T -= 1
    N = int(input())
    A = [0] + list(map(int, input().split()))
    ans = N

    dead = [0] * (N + 1)

    def dfs(n):
        global ans
        if n in students:
            while stack[-1] != n:
                dead[stack.pop()] = -1
                ans -= 1

            dead[stack.pop()] = -1
            ans -= 1

            while stack:
                dead[stack.pop()] = 1

            return

        if dead[n] != 0:
            while stack:
                dead[stack.pop()] = 1
            return

        stack.append(n)
        students.add(n)
        dfs(A[n])

    for i in range(1, N + 1):
        if dead[i] == 0:
            stack = []
            students = set()
            dfs(i)

    print(ans)
