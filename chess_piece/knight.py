from chess_piece.piece import Piece

class Knight(Piece):
    def __init__(self, position, colour, direction):
        super().__init__(position, colour, direction)
        self.name = colour + '_knight'
        self.directions = ()


    # wierd movements
    def available_moves(self):
        pass
