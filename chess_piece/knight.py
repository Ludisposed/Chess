from chess_piece.piece import Piece

class Knight(Piece):
    def __init__(self, position, colour):
        super(Knight, self).__init__(position, colour)
        self.name = colour + '_knight'
        self.direction = ()



    # wierd movements
    def available_moves(self):
        pass
