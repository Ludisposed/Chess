from chess_piece.piece import Piece

class Knight(Piece):
    def __init__(self, position, colour):
        super(Knight, self).__init__(position, colour)
        self.name = colour + '_knight'
        self.direction = ()

    # wierd movements
    def available_moves(self):
        direction = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))
        pos = self.position
        return [[pos[0] + d[0], pos[1] + d[1]] for d in direction]
