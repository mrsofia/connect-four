from classes import board, game, exceptions

b = board.Board()

# b.print_board()

g = game.Game(board=b)

#game loop
# as this is procedural logic I believe it ought to go here in the main class
# however I'm open to it eventually or potentially being handled by the game
# class for simpliciity's ske
#
# while not g.check_for_win():
#     print('game loop entered')
#     break
