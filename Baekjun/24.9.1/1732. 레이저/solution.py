from collections import deque
from sys import stdin

input = stdin.readline


def scope(x, y):
    if x == 0:
        return float("inf")
    return y / x


def find_highest_points(arr):
    if not arr:
        return

    highest = arr[0][2]
    for i in range(1, len(arr)):
        if scope(arr[i - 1][0], arr[i - 1][1]) != scope(arr[i][0], arr[i][1]):
            highest = arr[i][2]
        else:
            if highest >= arr[i][2]:
                ans.add((arr[i][0], arr[i][1]))
            highest = max(highest, arr[i][2])


N = int(input())
points = deque([tuple(map(int, input().split())) for _ in range(N)])
x_zero = []
s_zero = []
left = []
ans = set()
xyz = None

while points:
    x, y, z = points.popleft()
    if x == y == 0:
        xyz = (x, y, z)
    elif x == 0:
        x_zero.append((x, y, z))
    elif scope(x, y) == 0:
        s_zero.append((x, y, z))
    else:
        left.append((x, y, z))

left.sort(key=lambda p: (scope(p[0], p[1]), abs(p[0]), abs(p[1])))
find_highest_points(left)

x_zero.sort(key=lambda p: p[1])
find_highest_points(x_zero)

negatives = [p for p in s_zero if p[0] < 0]
positives = [p for p in s_zero if p[0] > 0]
negatives.sort(key=lambda p: abs(p[0]))
positives.sort(key=lambda p: abs(p[0]))
find_highest_points(negatives)
find_highest_points(positives)

if xyz:
    for x, y, z in x_zero + s_zero + left:
        if x == y == 0:
            continue
        if xyz[2] >= z:
            ans.add((x, y))

ans = sorted(ans)
print("\n".join(f"{x} {y}" for x, y in ans))
