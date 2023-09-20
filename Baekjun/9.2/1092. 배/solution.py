import sys

input = sys.stdin.readline

N = int(input())
crains = list(map(int, input().split()))
crains.sort(reverse=True)

M = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)

ans = 0

while boxes:
    crains_tmp = []
    ans += 1

    while crains:
        if not boxes:
            break

        b = boxes.pop()

        while crains and crains[-1] < b:
            crains.pop()

        if not crains:
            print(-1)
            exit(0)

        crains_tmp.append(crains.pop())

    crains.extend(crains_tmp[::-1])
    print(crains, boxes)

print(ans)
