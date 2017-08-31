from chess_piece.piece import Piece

class King(Piece):
    def __init__(self, position, colour):
        super(King, self).__init__(position, colour)
        self.name = colour + '_king'

    # TODO
    # Wierd movement with Castling
    def available_moves(self):
        direction = ((0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1))
        pos = self.position
        return [[pos[0] + d[0], pos[1] + d[1]] for d in direction]
