from chess_piece.piece import Piece

class Pawn(Piece):
    def __init__(self, position, colour):
        super(Pawn, self).__init__(position, colour)
        self.moved = False
        self.direction = ((1, 0), (2, 0)) if colour == 'black' else ((-1, 0), (-2, 0))
        self.name = colour + '_pawn'

    # if moved can only advance 1 square
    # if not moved can advance 2 squares
    def if_moved(self):
        self.moved = True
        self.direction = ((1, 0)) if colour == 'black' else ((-1, 0))

    # wierd movements
    def available_moves(self):
        return [[self.position[0] + d[0], self.position[1] + d[1]] for d in self.direction]
