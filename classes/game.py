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
        column_choice = input("what'll it be? ")
        print("your choice was...")
        print(column_choice)
        self.place_checker(column=column_choice)
        win = True if self.check_for_win() else False
        # win = True if column_choice=="bitch" else False
        if not win:
          self.toggle_players()
          self.make_move()

    def place_checker(self, column):
        print("you're putting the checker in column {}".format(column))

    def check_for_win(self):
        return False
        #pass

    def toggle_players(self):
        self.current_player = 'P2' if self.current_player == 'P1' else 'P1'
        # print(self.current_player+", you're up!")

    def whose_turn(self):
        return self.current_player
