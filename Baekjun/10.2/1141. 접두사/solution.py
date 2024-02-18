import sys

N = int(input())
words = [(sys.stdin.readline()).rstrip() for _ in range(N)]

words.sort(key=len)
src = 0
for i in range(N):
    nTrue = False
    for j in range(i + 1, N):
        if words[i] == words[j][: len(words[i])]:
            nTrue = True
            break
    if not nTrue:
        print(i)
        src += 1
print(src)
