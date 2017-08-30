from chess_piece.piece import Piece

class Queen(Piece):
    def __init__(self, position, colour, direction):
        super().__init__(position, colour, direction)
        self.name = colour + '_queen'
        self.directions = ((0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1))


    def available_moves(self):
        super().available_moves(self.directions)
