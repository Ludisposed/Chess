from chess_piece.piece import Piece

class Bishop(Piece):
    def __init__(self, position, colour):
        super(Bishop, self).__init__(position, colour)
        self.name = colour + '_bishop' 



    def available_moves(self, board):
        direction = ((-1, -1), (1, 1), (-1, 1), (1, -1))
        return super(Bishop, self).available_moves(direction, board)
