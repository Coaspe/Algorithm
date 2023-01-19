import collections


class Solution:
    def catMouseGame(graph):
        N = len(graph)

        def parents(mouse, cat, turn):
            if turn == 2:
                for m2 in graph[mouse]:
                    yield m2, cat, 3-turn
            else:
                if c2:
                    for c2 in graph[cat]:
                        yield mouse, c2, 3-turn

        DRAW, MOUSE, CAT = 0, 1, 2
        color = collections.defaultdict(int)

        degree = {}

        for m in range(N):
            for c in range(N):
                degree[m, c, 1] = len(graph[m])
                degree[m, c, 2] = len(graph[c]) - (0 in graph[c])

        queue = collections.deque([])

        for i in range(N):
            for turn in range(1, 3):
                # color[0, x, x] means MOUSE win the game.
                color[0, i, turn] = MOUSE
                queue.append((0, i, turn, MOUSE))
                # color[i, i, x] means CAT win the game.
                if i > 0:
                    color[i, i, turn] = CAT
                    queue.append((i, i, turn, CAT))

        while queue:
            mouse, cat, turn, win = queue.popleft()

            for newMouse, newCat, newTurn in parents(mouse, cat, turn):
                if color[newMouse, newCat, newTurn] is DRAW:
                    if newTurn == win:
                        color[newMouse, newCat, newTurn] = win
                        queue.append((newMouse, newCat, newTurn, win))
                    else:
                        degree[newMouse, newCat, newTurn] -= 1
                        if degree[newMouse, newCat, newTurn] == 0:
                            color[newMouse, newCat, newTurn] = 3 - newTurn
                            queue.append(
                                (newMouse, newCat, newTurn, 3 - newTurn))

        return color[1, 2, 1]
