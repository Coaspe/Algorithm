N, M = map(int, input().split())
# Index = worker
tasks = [list(map(int, input().split()))[1:] for _ in range(N)]

# Index = task
workers = [-1] * (M + 1)


def dfs(worker):
    for task in tasks[worker]:
        if not check[task]:
            check[task] = 1
            if workers[task] == -1 or dfs(workers[task]):
                workers[task] = worker
                return True
    return False


result = 0

for i in range(N):
    check = [0] * (M + 1)

    if dfs(i):
        result += 1

    check = [0] * (M + 1)

    if dfs(i):
        result += 1

print(result)
