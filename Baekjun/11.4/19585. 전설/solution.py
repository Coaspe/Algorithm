import sys

input = sys.stdin.readline


def check(word):
    now = colors
    for i in range(len(word)):
        if now.get(0) and word[i:] in names:
            return 1
        if not now.get(word[i]):
            return 0
        now = now[word[i]]


C, N = map(int, input().split())
colors = {}
for _ in range(C):
    now = colors
    for c in input().strip():
        if not now.get(c):
            now[c] = {}
        now = now[c]
    now[0] = 1

names = {input().strip() for _ in range(N)}

for _ in range(int(input())):
    print("Yes" if check(input().strip()) else "No")
