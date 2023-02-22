from collections import defaultdict, deque
import math
T = int(input())
while T:
    T -= 1
    # Computers, Dependencies, Hacked PC num
    n, d, c = map(int, input().split())
    time = [0] + [math.inf] * n
    time[c] = 0
    D = defaultdict(list)
    for _ in range(d):
        # a relies on b, a infected after s secends after b is infected.
        a, b, s = map(int, input().split())
        D[b].append((s, a))

    dp = [0] + [math.inf] * n
    dp[c] = 0
    q = deque([(0, c)])
    ans = []
    while q:
        cost, cur = q.popleft()
        for nextCost, nextNode in D[cur]:
            if dp[nextNode] > cost+nextCost:
                dp[nextNode] = cost+nextCost
                q.append((cost+nextCost, nextNode))
    for i in range(1, len(dp)):
        if dp[i] != math.inf:
            ans.append(dp[i])

    print(len(ans), max(ans))
