from piece import Piece

class Bishop(Piece):
    def __init__(self, position, colour, direction):
        self.name = colour + '_bishop'
        self.directions = ((-1, -1), (1, 1), (-1, 1), (1, -1))
        Piece().__init__(self, position, colour, direction)

    def available_moves(self):
        super().available_moves(self.directions)
