import sys


def find(now, before):
    # 남아있는 경로를 이미 방문한 적이 있음 (지금 있는곳과 켜진 경로와 꺼진 경로가 예전꺼랑 같으면)그냥 반환.
    if dp[now][before]:
        return dp[now][before]
    # 모두 방문한 경우 내가 있는 마을에서 1번 마을로 갈 길이 있다면(비용이 있다면) 그 비용에 대해 반환 -> 반환되면 cost에 path[now][i]와 합쳐저 최솟값을 찾아감.
    if before == (1 << n) - 1:
        if path[now][0] > 0:
            return path[now][0]
        else:
            # 못가면 무한대 반환. -> 결국 min연산에 의해 경로 삭제됨.
            return sys.maxsize
    # 현재 지점에서 이동할 수 있는 지점들을 탐색
    cost = sys.maxsize
    # 결국 모든 경로에 대해 조사하는 dfs 느낌이지만, 메모이제이션이나 dp를 사용해 메모리나 속도가 압도적.
    # 시작점에서 나오는 모든 dfs재귀순환 연산이 끝나면.cost에는 모든경로와 비교한 최솟값이 저장됨.
    for i in range(1, n):
        # 여기서 i로 가는 길이 있고 (before를 i만큼 땡겨서 i번째 마을을 1의 자리에 놓고 2로 나눈 나머지가 0일때) 즉 i번째 마을을 들리지 않은 상태였을때.
        if not before & (1 << i) and path[now][i]:
            # i부터 0까지 순회를 만든 최소 비용 i번 마을에 들러서 탐색을 시작한다.
            # before | (1<<i) == before + (1<<i)
            tmp = find(i, before | (1 << i))
            # (now~i), (i~0)의 합과 현재까지의 최소 비용과 비교
            # tmp는 i~0로 뒤쪽 순회한 비용 path[now][i]는 now에서 i까지의 이동비용.
            cost = min(cost, tmp + path[now][i])
    # 메모이제이션 그 자리에서 경로가 똑같을때의 cost저장.하고 이전으로 반환.
    dp[now][before] = cost
    return cost


n = int(sys.stdin.readline())
path = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# n개의 노드에 대해 00000000자릿수로 판별할것임.(00000000을 켜고끄는 모든 경우의 수 1<<n)
dp = [[0] * (1 << n) for _ in range(n)]
# 1번에서 시작.


def TSP(node, visited):
    if dp[node][visited]:
        return dp[node][visited]

    if visited == (1 << n) - 1:
        if path[node][0]:
            return path[node][0]
        else:
            return sys.maxsize
    cost = sys.maxsize
    for i in range(1, n):

        if not visited & (1 << i) and path[node][i]:
            tmp = TSP(i, visited | (1 << n))

            cost = min(cost, tmp + path[node][i])

    dp[node][visited] = cost
    return cost


print(TSP(0, 1))
