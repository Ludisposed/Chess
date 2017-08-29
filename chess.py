

'''
Class of the board
'''
class Board():
    def __init__(self, current_player, board):
        self.current_player = current_player
        self.board = board

    def __new__(self):
        pass

'''
Class of the chess Pieces
'''
class Piece():
    def __init__(self):
        pass

    def move(self):
        pass

class Pawn(Piece):
    pass

class Knight(Piece):
    pass

class Rook(Piece):
    pass

class Bishop(Piece):
    pass

class Queen(Piece):
    pass

class King(Piece):
    pass
