from collections import deque


def solution(n, path, order):
    prerequisites = {}  # Maps a node to its prerequisite
    dependents = {}  # Maps a node to its dependent

    for prereq, dependent in order:
        prerequisites[dependent] = prereq
        dependents[prereq] = dependent

    graph = [[] for _ in range(n)]
    for start, end in path:
        graph[start].append(end)
        graph[end].append(start)

    visited = [False] * n

    waiting_for_prereq = set()

    prereqs_completed = set()

    def can_visit(node):
        return node not in prerequisites or prerequisites[node] in prereqs_completed

    def process_dependents(prereq_node):
        if prereq_node in dependents:
            dependent = dependents[prereq_node]
            if dependent in waiting_for_prereq and can_visit(dependent):
                queue.append(dependent)
                waiting_for_prereq.remove(dependent)

    queue = deque()

    visited[0] = True

    if 0 in prerequisites and prerequisites[0] not in prereqs_completed:
        waiting_for_prereq.add(0)
    else:
        queue.append(0)

    if 0 in dependents:
        prereqs_completed.add(0)
        process_dependents(0)

    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if visited[neighbor]:
                continue

            visited[neighbor] = True

            if can_visit(neighbor):
                queue.append(neighbor)
            else:
                waiting_for_prereq.add(neighbor)

            if neighbor in dependents:
                prereqs_completed.add(neighbor)
                process_dependents(neighbor)

    return len(waiting_for_prereq) == 0
