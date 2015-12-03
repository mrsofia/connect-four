from sys import exit

from . import winchecker

class Game:

    P1 = 'P1'
    P2 = 'P2'

    def __init__(self, board):
        self.current_player = self.P1
        self.board = board
        self.winchecker = winchecker.WinChecker(game=self, board=self.board)
        print("Welcome to connect four! ")
        self.make_move()

    def make_move(self):
        print("{}\n{}, you're up! ".format(self.board, self.current_player))
        column_choice = self.get_column_choice()

        valid_column = self.place_checker(column=column_choice)
        if not valid_column:
            print("That column is full. Please enter a non-full column. ")
            self.make_move()
            return False
        win = True if self.check_for_win() else False
        if not win:
            self.toggle_players()
            self.make_move()
        if win:
            print(self.board)
            print("\ncongratulations {}, you win!\n".format(self.current_player))

    def get_column_choice(self):
        print("What column what you like to place your piece?\n")
        column_choice = input("Valid choices are columns 0 through 6: ")
        try:
            if column_choice == "exit": exit()
            column_choice = int(column_choice)
            return column_choice if 0 <= column_choice <= 6 else self.get_column_choice()
        except ValueError:
            return self.get_column_choice()

    def place_checker(self, column):
        print("You've selected column {}".format(column))

        if(self.board.board[0][column] != ' . '):
            # column is full, force player to re-choose
            return False
        lowest_available_row = self.find_lowest_row_in_column(column=column)
        try:
            self.board.board[lowest_available_row][column] = self.players_piece()
            return True
        except IndexError:
            # this should never happen
            print("Array out of bounds error! Exiting...")
            exit()

    def find_lowest_row_in_column(self, column):
        column_as_list = []
        for row in self.board.board:
            column_as_list.append(row[column])

        try:
            first_red = column_as_list.index(self.board.RED) - 1
        except ValueError:
            first_red = None
        try:
            first_blue = column_as_list.index(self.board.BLUE) - 1
        except ValueError:
            first_blue = None

        if first_blue == None and first_red == None:
            return 5
        elif first_blue == None or first_red == None:
            return first_blue if first_blue != None else first_red
        else:
            return min(first_blue, first_red)

    def check_for_win(self):
        return self.winchecker.check_for_win()

    def toggle_players(self):
        self.current_player = 'P2' if self.current_player == 'P1' else 'P1'

    def players_piece(self):
        return self.board.RED if self.current_player == self.P1 else self.board.BLUE
