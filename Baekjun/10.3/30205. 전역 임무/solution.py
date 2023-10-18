import io, os, sys

input = sys.stdin.readline

n, m, p = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]

ip = True
for info in li:
    info.sort()
    item_c = 0
    for v in info:
        if v == -1:
            item_c += 1
        else:
            while p < v:
                if item_c:
                    item_c -= 1
                    p *= 2
                else:
                    ip = False
                    break

            if not ip:
                break
            p += v

    while item_c:
        item_c -= 1
        p *= 2

if ip:
    print(1)
else:
    print(0)
