from piece import Piece

class Knight(Piece):
    def __init__(self, position, colour):
        self.name = colour + '_knight'
        self.directions = ()
        Piece().__init__(self, position, colour, direction)

    # wierd movements
    def available_moves(self):
        pass
