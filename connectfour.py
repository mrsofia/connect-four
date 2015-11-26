from classes import board, game

b = board.Board()

# b.print_board()

g = game.Game(board=b)

#game loop
# perhaps this belongs in the game class
# while not g.check_for_win():
#     print('game loop entered')
#     break
