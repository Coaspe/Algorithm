import sys
S, T = list(input()), list(input())


def dfs(t):
    if t == S:
        print(1)
        sys.exit()
    if len(S) >= len(t):
        return 0
    if t[-1] == 'A':
        dfs(t[:-1])
    if t[0] == 'B':
        dfs(t[1:][::-1])


dfs(T)
print(0)
