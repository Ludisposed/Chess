from chess_piece.piece import Piece

class Pawn(Piece):
    def __init__(self, position, colour):
        super(Pawn, self).__init__(position, colour)
        self.direction = ()
        self.name = colour + '_pawn'



    # wierd movements
    def available_moves(self):
        #for test in black
        return [[self.position[0] + 1,self.position[1]], [self.position[0] + 2,self.position[1]]]
