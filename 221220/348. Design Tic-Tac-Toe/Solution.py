class TicTacToe(object):
    def __init__(self, n):
        count = collections.Counter()

        def move(row, col, player):
            for i, x in enumerate((row, col, row+col, row-col)):
                print(i, x)
                count[i, x, player] += 1
                if count[i, x, player] == n:
                    return player
            return 0
        self.move = move
