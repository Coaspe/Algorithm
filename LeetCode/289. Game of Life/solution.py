class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        neighbors = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
        ]
        transition_map = {(0, 0): 0, (0, 1): 2, (1, 0): 3, (1, 1): 1}

        def n_cnt(r, c):
            cnt = 0

            for dx, dy in neighbors:
                row, col = r + dx, c + dy

                if (
                    0 <= row < m
                    and 0 <= col < n
                    and (board[row][col] == 1 or board[row][col] == 3)
                ):
                    cnt += 1
            return cnt

        def life(r, c):
            cur = board[r][c]
            n_c = n_cnt(r, c)
            next_state = 0

            if (cur == 1 and 1 < n_c < 4) or (cur == 0 and n_c == 3):
                next_state = 1

            board[r][c] = transition_map[(cur, next_state)]

        for i in range(m):
            for j in range(n):
                life(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 1 or board[i][j] == 2:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
