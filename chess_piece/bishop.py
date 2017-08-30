from chess_piece.piece import Piece

class Bishop(Piece):
    def __init__(self, position, colour):
        self.name = colour + '_bishop'
        self.direction = ((-1, -1), (1, 1), (-1, 1), (1, -1))
        super(Bishop, self).__init__(position, colour, self.direction, self.name)


    def available_moves(self):
        super().available_moves(self.directions)
