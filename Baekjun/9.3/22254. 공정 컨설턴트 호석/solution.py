from heapq import heappop, heappush

N, X = map(int, input().split())

A = list(map(int, input().split()))


def bs(line_num):
    lines = [0] * line_num
    for a in A:
        next_val = a + heappop(lines)

        if next_val > X:
            return False

        heappush(lines, next_val)

    return True


l, r = 1, N
ans = r

while r > l + 1:
    mid = (r + l) // 2
    if bs(mid):
        r = mid
        ans = min(ans, r)
    else:
        l = mid

if bs(l):
    ans = min(ans, l)

print(ans)
