import collections

A, B, C = map(int, input().split())
s = tuple(sorted([A, B, C]))
q = collections.deque([s])
visited = set([s])

while q:
    a, b, c = q.popleft()
    if a == b == c:
        print(1)
        break
    for x, y, z in (a, b, c), (a, c, b), (b, c, a):
        y -= x
        x += x
        s = tuple(sorted([x, y, z]))
        if s not in visited:
            visited.add(s)
            q.appendleft(s)
else:
    print(0)
