import itertools
import pygame

'''
Class of the Player
'''
class Player():
    def __init__(self, colour, name):
        self.colour = colour
        self.name = name
        self.castle_long = False
        self.castle_short = False

    def __str__(self):
        return '{} as {}'.format(self.name, self.colour)

'''
Class of the board
'''
class Board():
    def __init__(self, current_player, board):
        self.current_player = current_player
        self.board = board

    def remove_piece():
        pass
    

'''
Class of the chess Pieces
'''
class Piece():
    def __init__(self, name, position, colour):
        self.name = name
        self.position = position
        self.colour = colour

'''
Classes for individual pieces derived from Piece class
'''
class Pawn(Piece):
    def __init__(self, name, position, colour):
        super().__init__()

class Knight(Piece):
    def __init__(self, name, position, colour):
        super().__init__()

class Rook(Piece):
    def __init__(self, name, position, colour):
        super().__init__()

class Bishop(Piece):
    def __init__(self, name, position, colour):
        super().__init__()

class Queen(Piece):
    def __init__(self, name, position, colour):
        super().__init__()

class King(Piece):
    def __init__(self, name, position, colour):
        super().__init__()
