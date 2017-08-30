from piece import Piece

class Pawn(Piece):
    def __init__(self, position, colour, direction):
        self.directions = ()
        self.name = colour + '_pawn'
        Piece().__init__(self, position, colour, direction)

    # wierd movements
    def available_moves(self):
        pass
