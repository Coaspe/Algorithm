def solution(commands):
    answer = []
    parent = [[(i, j) for j in range(51)] for i in range(51)]
    board = [[""] * 51 for _ in range(51)]

    def find(r, c):
        if parent[r][c] != (r, c):
            parent[r][c] = find(*parent[r][c])
        return parent[r][c]

    def union(p1, p2):
        r1, c1 = find(*p1)
        r2, c2 = find(*p2)

        if [r1, c1] == [r2, c2]:
            return

        parent[r2][c2] = (r1, c1)
        v = board[r1][c1] if board[r1][c1] else board[r2][c2]
        for i in range(51):
            for j in range(51):
                if find(i, j) == (r1, c1):
                    board[i][j] = v

    for command in commands:
        command = command.split(" ")
        if command[0] == "UPDATE":
            if len(command) == 4:
                r, c, s = int(command[1]), int(command[2]), command[3]
                r1, c1 = find(r, c)
                board[r1][c1] = s
            else:
                s1, s2 = command[1:]
                for i in range(1, 51):
                    for j in range(1, 51):
                        if board[i][j] == s1:
                            board[i][j] = s2
        elif command[0] == "MERGE":
            r1, c1, r2, c2 = map(int, command[1:])
            union((r1, c1), (r2, c2))
        elif command[0] == 'PRINT':
            r, c = find(*map(int, command[1:]))
            answer.append(board[r][c] if board[r][c] else "EMPTY")
        elif command[0] == 'UNMERGE':
            r, c = map(int, command[1:])
            gp = find(r, c)
            tmp = board[gp[0]][gp[1]]
            for i in range(1, 51):
                for j in range(1, 51):
                    p = find(i, j)
                    if p == gp:
                        parent[i][j] = (i, j)
                        board[i][j] = ""
            board[r][c] = tmp
    return answer


C = ["UPDATE 1 1 A", "UPDATE 2 2 B", "UPDATE 3 3 C", "UPDATE 4 4 D", "MERGE 1 1 2 2",
     "MERGE 3 3 4 4", "MERGE 1 1 4 4", "UNMERGE 3 3", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3", "PRINT 4 4"]
print(solution(C))
