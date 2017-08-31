from chess_piece.piece import Piece

class King(Piece):
    def __init__(self, position, colour):
        super(King, self).__init__(position, colour)
        self.name = colour + '_king'



    def available_moves(self):
        direction = ((0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1))
        return super().available_moves(direction)
