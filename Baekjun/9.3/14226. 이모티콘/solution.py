n = int(input())
MAX = 1e9
q = [(1, 0, 0)]
check = [MAX for _ in range(2001)]
visited = [False for _ in range(1001)]

while q:
    now, time, cpy = q.pop(0)
    check[now] = time

    if now == n:
        print(int(time))
        break

    # 1. - 1
    if now > 0 and time < check[now]:
        q.append((now - 1, time + 1, cpy))
    # 2. +cpy
    if now + cpy <= 1000 and time < check[now + cpy]:
        q.append((now + cpy, time + 1, cpy))
    # 3. execute copy
    if now <= 500 and not visited[now]:
        visited[now] = True
        q.append((now, time + 1, now))
