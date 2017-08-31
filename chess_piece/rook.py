from chess_piece.piece import Piece

class Rook(Piece):
    def __init__(self, position, colour):
        super(Rook, self).__init__(position, colour)
        self.name = colour + '_rook'


    def available_moves(self):
        direction = ((0, 1), (1, 0), (-1, 0), (0, -1))
        return super(Rook, self).available_moves(direction)
