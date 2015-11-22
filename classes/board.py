class Board:

    NONE = '.'
    RED = 'R'
    BLUE = 'B'

    def __init__(self, cols = 7, rows = 6, required_to_win = 4):
        self.board = []
        self.cols = cols
        self.rows = rows
        self.win = required_to_win
        self.board = [[self.NONE] * rows for col in range(cols)]

    def create_board(self):
        board = []
        for i in range(6):
#            print(i)
            board.append('x')
#        print(board)
        board2 = []
        for i in range(7):
            board2.append(board)
        print(board2)

    def call_board(self):
        print("called the board!")
        print("self.board: ")
        print(self.board)
    # create other useful methods and shit.
