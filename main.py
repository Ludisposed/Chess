import itertools
from board import Board
from player import Player
if __name__ == '__main__':
    board = Board(Player('black','PvS'),Player('white','sVp'))
    board.on_execute()
