import math
import collections
import heapq


def solve():
    R, C = map(lambda x: int(x)+1, input().split())
    A1, A2, B1, B2 = [
        tuple(reversed(list(map(int, input().split())))) for _ in range(4)]
    aDist = abs(A1[0]-A2[0]) + abs(A1[1]-A2[1])
    bDist = abs(B1[0]-B2[0]) + abs(B1[1]-B2[1])
    # No problem
    if min(A1[1], A2[1]) > max(B1[1], B2[1]) or min(B1[1], B2[1]) > max(A1[1], A2[1]) or \
            min(A1[0], A2[0]) > max(B1[0], B2[0]) or min(B1[0], B2[0]) > max(A1[0], A2[0]):
        print(aDist + bDist)
        return
    # Exists
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    notAllowed = set()
    upA, downA = min(A1, A2, key=lambda x: x[0]), max(
        A1, A2, key=lambda x: x[0])
    leftA, rightA = min(A1, A2, key=lambda x: x[1]), max(
        A1, A2, key=lambda x: x[1])

    # Not allowed points
    for i in range(upA[0], downA[0]+1):
        notAllowed.add((i, upA[1]))
    for i in range(leftA[1], rightA[1]+1):
        notAllowed.add((downA[0], i))

    ans = math.inf
    check = [[math.inf]*C for _ in range(R)]
    check[B1[0]][B1[1]] = 0
    q = collections.deque([(0, B1)])

    while q:
        move, cur = q.popleft()
        if cur == B2:
            ans = min(ans, move)
            continue
        for i in range(4):
            nx, ny = cur[0]+dx[i], cur[1]+dy[i]
            if 0 <= nx < R and 0 <= ny < C and check[nx][ny] > move+1 and (nx, ny) not in notAllowed:
                check[nx][ny] = move+1
                q.append((move+1, (nx, ny)))
    print(ans + aDist if ans != math.inf else "IMPOSSIBLE")


solve()
