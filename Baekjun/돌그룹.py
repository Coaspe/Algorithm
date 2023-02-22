import collections
A, B, C = map(int, input().split())
s = tuple(sorted([A,B,C]))
q = collections.deque([s])
visited = set([s])
while q:
    a, b, c = q.popleft()
    if a == b == c:
        print(1)
        break
    for x, y, z in (a, b, c), (a, c, b), (b ,c, a):
        y -= x
        x += x
        s = tuple(sorted([x,y,z]))
        if s not in visited:
            visited.add(s)
            q.appendleft(s)
else:
    print(0)
# visited = set()
# def dfs(a, b, c):
#     if a == b == c:
#         return 1
    
#     newC, a = c - a, 2*a

#     s = tuple(sorted([a,b,newC]))
    
#     if c-a > s[2]-s[0] and s not in visited:
#         visited.add(s)
#         r = dfs(*s)
#         if r:
#             return r
#     return 0
# print(dfs(*sorted([A, B, C])))
