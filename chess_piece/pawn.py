from chess_piece.piece import Piece

class Pawn(Piece):
    def __init__(self, position, colour):
        super(Pawn, self).__init__(position, colour)
        self.moved = False
        self.direction = ((1, 0), (2, 0), (1, -1), (1, 1)) if colour == 'black' else ((-1, 0), (-2, 0), (-1, -1), (-1, 1))
        self.name = colour + '_pawn'

    # if moved can only advance 1 square
    # if not moved can advance 2 squares
    def if_moved(self):
        self.moved = True
        self.direction = ((1, 0), (1, -1), (1, 1)) if 'black' in self.name else ((-1, 0), (-1, -1), (-1, 1))

    # wierd movements
    def available_moves(self):
        available_moves = [[self.position[0] + d[0], self.position[1] + d[1]] for d in self.direction]
        return [i for i in available_moves if 0 <= i[0] <=7 and 0 <= i[1] <= 7]
