from chess_piece.piece import Piece

class King(Piece):
    def __init__(self, position, colour):
        self.name = colour + '_king'
        self.direction = ((0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1))
        super(King, self).__init__(position, colour, self.direction)


    def available_moves(self):
        super().available_moves(self.directions)
