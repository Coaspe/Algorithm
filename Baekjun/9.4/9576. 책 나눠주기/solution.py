from collections import deque


def solution(num_points, roads):
    adjacent_points = {i: set() for i in range(1, num_points + 1)}
    for a, b in roads:
        adjacent_points[a].add(b)

    scc_count = 0
    visit_order = [0] * (num_points + 1)
    scc_number = [0] * (num_points + 1)
    is_finished = [False] * (num_points + 1)
    order_count = 0
    stack = []

    # SCC 찾기
    def dfs_visit(current):
        nonlocal order_count
        visit_num = visit_order[current] = order_count + 1
        order_count += 1
        stack.append(current)

        for next_point in adjacent_points[current]:
            if not visit_order[next_point]:
                visit_num = min(visit_num, dfs_visit(next_point))
            elif not is_finished[next_point]:
                visit_num = min(visit_num, visit_order[next_point])

        if visit_num == visit_order[current]:
            nonlocal scc_count
            scc_count += 1
            while True:
                visited_point = stack.pop()
                is_finished[visited_point] = True
                scc_number[visited_point] = scc_count
                if visited_point == current:
                    break

        return visit_num

    for i in range(1, num_points + 1):
        if not visit_order[i]:
            dfs_visit(i)

    # SCC 끼리 그래프 따로 생성
    scc_adj = {i: set() for i in range(1, scc_count + 1)}
    for i in range(1, num_points + 1):
        u = scc_number[i]
        for x in adjacent_points[i]:
            v = scc_number[x]
            if u != v:
                scc_adj[u].add(v)

    # 한 SCC에서 갈 수 있는 SCC를 모두 찾기
    scc_adj_reachable = {i: set() for i in range(1, scc_count + 1)}
    visit = [False] * (scc_count + 1)

    def dfs2(start, now):
        visit[now] = True
        if start != now:
            scc_adj_reachable[start].add(now)
        for next_node in scc_adj[now]:
            if not visit[next_node]:
                dfs2(start, next_node)

    for i in range(1, scc_count + 1):
        dfs2(i, i)
        visit = [False] * (scc_count + 1)

    # Hopcraft-carp
    answer = scc_count - 1
    A = [0] * (scc_count + 1)
    B = [0] * (scc_count + 1)
    q = deque()

    def f(now):
        for next_node in scc_adj_reachable[now]:
            if not B[next_node] or (
                level[B[next_node]] == level[now] + 1 and f(B[next_node])
            ):
                A[now], B[next_node] = next_node, now
                return True
        return False

    while True:
        level = [-1] * (scc_count + 1)
        for i in range(1, scc_count + 1):
            if not A[i]:
                level[i] = 0
                q.append(i)

        while q:
            now = q.popleft()
            for next_node in scc_adj_reachable[now]:
                if B[next_node] and level[B[next_node]] == -1:
                    level[B[next_node]] = level[now] + 1
                    q.append(B[next_node])

        temp = sum(1 for i in range(1, scc_count + 1) if not A[i] and f(i))
        print(A, B, level)
        if not temp:
            break
        answer -= temp

    return max(answer, 0)
