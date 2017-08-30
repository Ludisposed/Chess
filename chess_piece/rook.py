from chess_piece.piece import Piece

class Rook(Piece):
    def __init__(self, position, colour):
        self.name = colour + '_rook'
        self.direction = ((0, 1), (1, 0), (-1, 0), (0, -1))
        super(Rook, self).__init__(position, colour, self.direction, self.name)


    def available_moves(self):
        super().available_moves(self.directions)
