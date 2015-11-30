from classes import board, game, exceptions

play_again = "yes"

# game loop
while play_again == "yes":
    b = board.Board()
    g = game.Game(board=b)
    play_again = input("Would you like to play again? Enter yes to replay: ").lower().strip()
