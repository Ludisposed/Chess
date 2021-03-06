from chess_piece.piece import Piece

class Knight(Piece):
    def __init__(self, position, colour):
        super(Knight, self).__init__(position, colour)
        self.name = colour + '_knight'
        self.direction = ()

    # wierd movements
    def available_moves(self, board):
        direction = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))
        available_moves = []
        for d in direction:
            pos = self.position
            r, c = [pos[0] + d[0], pos[1] + d[1]]

            # inrange
            if 0 <= r and r <= 7 and 0 <= c and c <= 7:
                # empty
                if board[r][c] is None:
                    available_moves.append([r, c])
                else:
                    # or can attack
                    if board[r][c].colour != self.colour:
                        available_moves.append([r, c])
                
        return available_moves
