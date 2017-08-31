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
        available_moves = [[pos[0] + d[0], pos[1] + d[1]] for d in direction]
        return [i for i in available_moves if 0 <= i[0] <=7 and 0 <= i[1] <= 7]
