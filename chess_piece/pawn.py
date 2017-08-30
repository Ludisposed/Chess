from chess_piece.piece import Piece

class Pawn(Piece):
    def __init__(self, position, colour, direction):
        super().__init__(position, colour, direction)
        self.directions = ()
        self.name = colour + '_pawn'


    # wierd movements
    def available_moves(self):
        pass
