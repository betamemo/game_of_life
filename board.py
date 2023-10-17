class Board:
    def __init__(self, width=3, height=3):
        self.board = []
        self.width = width
        self.height = height
        for i in range(height):
            self.board.append([False] * width)

    def __str__(self):
        s = ''
        for row in self.board:
            s += ' '.join('.0'[i] for i in row)
            s += '\n'
        return s

    def place_cell(self, row, col):
        self.board[row][col] = True

    def remove_cell(self, row, col):
        self.board[row][col] = False

    def start(self):
        for row in range(self.width):
            tmp = ''
            for col in range(self.height):
                n = self.get_num_neighbors(row, col)
                tmp = tmp + str(n) + ' '
            print(tmp)

    def get_num_neighbors(self, row, col):
        counter = 0
        for r in (-1, 0, 1):
            for c in (-1, 0, 1):
                if r == c and r == 0:
                    continue
                if self.get_cell(row + r, col + c):
                    counter += 1
        return counter

    def get_cell(self, row, col):
        if 0 <= row < self.height:
            if 0 <= col < self.width:
                return self.board[row][col]
        return False
