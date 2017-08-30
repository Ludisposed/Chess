from piece import Piece

class Rook(Piece):
    def __init__(self, position, colour, direction):
        self.name = colour + '_rook'
        self.directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
        Piece().__init__(self, position, colour, direction)

    def available_moves(self):
        super().available_moves(self.directions)
