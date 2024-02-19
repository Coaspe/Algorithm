def solution():
    N = int(input())

    a, b = map(int, input().split())
    a -= 1
    b -= 1
    INF = 51
    dist = [[INF] * (N) for _ in range(N)]

    while a != -2:
        dist[a][b] = 1
        dist[b][a] = 1
        a, b = map(int, input().split())
        a -= 1
        b -= 1

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i != j:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    min_val = INF
    ans = []

    for i in range(N):
        tmp_max_val = -1
        cnt = 0
        for j in range(N):
            if i == j:
                continue

            if dist[i][j] == INF:
                break

            tmp_max_val = max(tmp_max_val, dist[i][j])
            cnt += 1

        if cnt == N - 1:
            if tmp_max_val < min_val:
                min_val = tmp_max_val
                ans = [i + 1]
            elif tmp_max_val == min_val:
                ans.append(i + 1)

    print(min_val, len(ans))
    print(*ans)


if __name__ == "__main__":
    solution()
