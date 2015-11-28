class Board:

    NONE = ' . '
    RED = ' R '
    BLUE = ' B '

    def __init__(self, cols = 6, rows = 7, required_to_win = 4):
        self.cols = cols
        self.rows = rows
        self.win = required_to_win
        self.board = [[self.NONE] * rows for col in range(cols)]

    def __str__(self):
        b = '\n'
        for row in self.board:
            b += ''.join(row) + '\n'
        b += " 0  1  2  3  4  5  6  \n"
        return b
