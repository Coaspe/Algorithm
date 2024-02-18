from heapq import heapify, heappop, heappush

N = int(input())
T = int(input())
A = list(map(int, input().split()))
B = []


def check(target):
    for i in range(len(B)):
        _, _, node = B[i]
        if node == target:
            return i
    return -1


T = 0
for a in A:
    idx = check(a)
    if len(B) >= N:
        # exists
        if idx != -1:
            B[idx] = (B[idx][0] + 1, B[idx][1], a)
            heapify(B)
        else:
            heappop(B)
            heappush(B, (1, T, a))
    else:
        if idx != -1:
            B[idx] = (B[idx][0] + 1, B[idx][1], a)
            heapify(B)
        else:
            heappush(B, (1, T, a))

    T += 1

print(*[x[2] for x in sorted(B, key=lambda x: x[2])])
