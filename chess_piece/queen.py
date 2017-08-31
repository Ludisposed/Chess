from chess_piece.piece import Piece

class Queen(Piece):
    def __init__(self, position, colour):
        super(Queen, self).__init__(position, colour)
        self.name = colour + '_queen'



    def available_moves(self):
        direction = ((0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1))
        return super(Queen, self).available_moves(direction)
