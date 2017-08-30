from chess_piece.piece import Piece

class Bishop(Piece):
    def __init__(self, position, colour):
        super(Bishop, self).__init__(position, colour)
        self.name = colour + '_bishop'
        self.direction = ((-1, -1), (1, 1), (-1, 1), (1, -1))



    def available_moves(self):
        super().available_moves(self.directions)
