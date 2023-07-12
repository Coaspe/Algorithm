from collections import deque


def solution():
    MAX_NUM = 500000
    N, K = map(int, input().split())

    check = [[-1] * (MAX_NUM+1) for _ in range(2)]

    def bfs():
        q = deque()
        q.append((N, 0))
        check[0][N] = 0

        while q:
            n, cnt = q.popleft()

            flag = cnt % 2
            cnt += 1
            for new_n in n+1, n-1, 2*n:
                if 0 <= new_n <= MAX_NUM and check[1-flag][new_n] == -1:
                    check[1-flag][new_n] = cnt
                    q.append((new_n, cnt))

    bfs()

    t = 0
    flag = 0
    while K <= MAX_NUM:
        if -1 < check[flag][K] <= t and t % 2 == check[flag][K] % 2:
            print(t)
            return
        flag = 1 - flag
        t += 1
        K += t

    print(-1)


solution()
