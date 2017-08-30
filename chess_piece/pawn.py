from chess_piece.piece import Piece

class Pawn(Piece):
    def __init__(self, position, colour):
        self.direction = ()
        self.name = colour + '_pawn'
        super(Pawn, self).__init__(position, colour, self.direction)


    # wierd movements
    def available_moves(self):
        pass
