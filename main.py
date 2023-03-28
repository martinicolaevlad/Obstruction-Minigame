from src.obstruction.board import Board
from src.obstruction.game import Game
from src.ui import Ui

board = Board()
game = Game(board)
ui = Ui(game)

ui.start_game()
