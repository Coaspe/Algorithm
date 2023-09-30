######## Bipartite Matching
T = int(input())
task = []
visit = []


def dfs(x):
    for i in task[x]:
        if not check[i]:
            check[i] = True
            if visit[i] == -1 or dfs(visit[i]):
                visit[i] = x
                return True
    return False


while T:
    T -= 1

    n, m = map(int, input().split())
    task = []
    visit = [-1] * n

    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        task.append(range(a, b + 1))

    result = 0

    for i in range(m):
        check = [False] * n
        if dfs(i):
            result += 1

    print(result)

######## Greedy

T = int(input())


while T:
    T -= 1

    n, m = map(int, input().split())
    task = []
    check = [0] * n

    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        task.append([b, a])

    task.sort()

    result = 0

    for b, a in task:
        for i in range(a, b + 1):
            if not check[i]:
                result += 1
                check[i] = 1
                break

    print(result)
