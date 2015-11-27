class Game:

    P1 = 'P1'
    P2 = 'P2'

    def __init__(self, board):
        self.current_player = 'P1'
        self.board = board
        print("Welcome to connect four! ")
        self.make_move()

    def make_move(self):
        #returns true if the current player has won the game
        # print(self.board+'\n'+self.current_player+", you're up!")
        print(self.board)
        print(self.current_player+", you're up! ")
        column_choice = self.get_column_choice()
        if type(column_choice) != int:
            raise ValueError("custom error: column_choice returned by get_column_choice was not an int!! could be caused by recursion in origin method")
        print("your choice was...")
        print(column_choice)
        self.place_checker(column=column_choice)
        # win = True if self.check_for_win() else False

        # haxx for now
        win = True if column_choice=="exit" else False
        if not win:
          self.toggle_players()
          self.make_move()

    def get_column_choice(self):
        print("What column what you like to place your piece?\n")
        column_choice = input("Valid choices are columns 0 through 5: ")
        try:
            column_choice = int(column_choice)
            return column_choice if 0 <= column_choice <= 5 else self.get_column_choice()
        except ValueError:
            # print("{} is not a valid column choice. Please enter a value between 0 and 5".format(column_choice))
            return self.get_column_choice()

    def place_checker(self, column):
        print("you're putting the checker in column {}".format(column))

    def check_for_win(self):
        return False

    def toggle_players(self):
        self.current_player = 'P2' if self.current_player == 'P1' else 'P1'

    # helper method, not used in production
    def whose_turn(self):
        return self.current_player
