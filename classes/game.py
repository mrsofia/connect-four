from sys import exit

class Game:

    P1 = 'P1'
    P2 = 'P2'

    def __init__(self, board):
        self.current_player = self.P1
        self.board = board
        print("Welcome to connect four! ")
        self.make_move()

    def make_move(self):
        #returns true if the current player has won the game
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
            print("congratulations, you win!")


    def get_column_choice(self):
        print("What column what you like to place your piece?\n")
        column_choice = input("Valid choices are columns 0 through 6: ")
        try:
            if column_choice == "exit": exit()
            column_choice = int(column_choice)
            return column_choice if 0 <= column_choice <= 6 else self.get_column_choice()
        except ValueError:
            # print("{} is not a valid column choice. Please enter a value between 0 and 5".format(column_choice))
            return self.get_column_choice()

    # how to resolve issue of calling board.place_checker without current_player?
    def place_checker(self, column):
        print("You've selected column {}".format(column))
        #1. force player to re-input if column is full

        if(self.board.board[0][column] != ' . '):
            # column is full, force player to re-choose
            return False
        lowest_available_row = self.find_lowest_row_in_column(column=column)
        try:
            self.board.board[lowest_available_row][column] = self.players_piece()
            return True
        except IndexError:
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
        win = False
        # c1 et al represent column numbers
        row = 5
        cols = [0, 1, 2, 3]
        while not win:
            try:
                seq = []
                # print("cols is {}".format(cols))
                # print("row is {}".format(row))
                # print(self.board.board)
                # print("self.board.board[5][5] is {}".format(self.board.board[5][5]))
                # print("cols before for loop is {}".format(cols))
                for i in range(len(cols)):
                    # print("i in this iter is {}".format(i))
                    # get current 4 values this iteration into seq list
                    # print("cols[i] in this iter is {}".format(cols[i]))
                    seq.append(self.board.board[row][cols[i]])
                    # print("row is {}".format(row))
                    # print("cols[i] is {}".format(cols[i]))
                    # print("self.board.board[rows][cols[i]] is {}".format(self.board.board[row][cols[i]]))
                # for checker in seq:
                print("seq at beginning of check is now {}".format(seq))
                # print('check for win called')
                if self.check_equal(seq):
                    print("self.check_equal came back true")
                    return True
                else:
                    for i in range(len(cols)):
                        cols[i] += 1
                    # print("cols changed to {} in else block of try".format(cols))
                    # print("cols is {}".format(cols))
                    continue
            except IndexError as inst:
                # print(type(inst))
                # print(inst.args)
                # print(inst)
                print('IndexError, it broke')
                break
            # win = True
            # break
        if (win == False): print('reached end of check_for_win function')
        return win

    def check_equal(self, lst):
        return lst[1:] == lst[:-1] if lst[0] != self.board.NONE else False

    def toggle_players(self):
        self.current_player = 'P2' if self.current_player == 'P1' else 'P1'

    def players_piece(self):
        return self.board.RED if self.current_player == self.P1 else self.board.BLUE
