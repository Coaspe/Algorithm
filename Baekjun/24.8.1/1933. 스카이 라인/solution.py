from heapq import *

hq = []

max_r = 0
for _ in range(int(input())):
    l, h, r = map(int, input().split())
    max_r = max(max_r, r)
    heappush(hq, (l, -h, r))

prev = None
ans = []
while hq:
    cl, ch, cr = heappop(hq)
    if prev == None:
        prev = (cl, ch, cr)
        ans.extend([cl, -ch])
        continue

    pl, ph, pr = prev

    if pr < cl:
        prev = (cl, ch, cr)
        ans.extend([pr, 0, cl, -ch])
        continue

    if pr <= cl:
        if pr != cl or -ch != ans[-1]:
            ans.extend([cl, -ch])
        prev = (cl, ch, cr)
    elif -ph >= -ch and cr > pr:
        heappush(hq, (pr, ch, cr))
    elif -ph < -ch:
        ans.extend([cl, -ch])
        if cl < pr:
            heappush(hq, (cl, ph, pr))
        prev = (cl, ch, cr)

ans.extend([max_r, 0])

print(" ".join(map(str, ans)))
