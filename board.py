class Board:
    def __init__(self, width=3, height=3):
        self.board = []
        for i in range(height):
            self.board.append([False] * width)

    def __str__(self):
        r = ''
        for row in self.board:
            r += ' '.join('.X'[i] for i in row)
            r += '\n'
        return r
