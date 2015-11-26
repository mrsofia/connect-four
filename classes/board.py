class Board:

    NONE = ' . '
    RED = ' R '
    BLUE = ' B '

    def __init__(self, cols = 7, rows = 6, required_to_win = 4):
        self.board = []
        self.cols = cols
        self.rows = rows
        self.win = required_to_win
        self.board = [[self.NONE] * rows for col in range(cols)]

    def __str__(self):
        b = '\n'
        for row in self.board:
            b += ''.join(row) + '\n'
        return b

    def place_checker(self, column):
        pass
        # if the column is full, return false

        # if the column is not full, place the checker in the lowest possible space.
