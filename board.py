class Board:
    def __init__(self, width=3, height=3):
        self.board = [[False] * 3, [False] * 3, [False] * 3]

    def __str__(self):
        r = ''
        for row in self.board:
            r += ''.join('.O'[i] for i in row)
            r += '\n'
        return r
