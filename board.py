class Board:
    def __init__(self, width=3, height=3):
        self.board = []
        for i in range(height):
            self.board.append([False] * width)

    def __str__(self):
        s = ''
        for row in self.board:
            s += ' '.join('.X'[i] for i in row)
            s += '\n'
        return s

    def place_cell(self, row, col):
        self.board[row][col] = True
