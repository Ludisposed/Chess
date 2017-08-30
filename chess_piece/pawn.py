from chess_piece.piece import Piece

class Pawn(Piece):
    def __init__(self, position, colour):
        super(Pawn, self).__init__(position, colour)
        self.direction = ()
        self.name = colour + '_pawn'



    # wierd movements
    def available_moves(self):
        pass
