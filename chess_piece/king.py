from chess_piece.piece import Piece

class King(Piece):
    def __init__(self, position, colour):
        super(King, self).__init__(position, colour)
        self.name = colour + '_king'
        self.castle_long = False
        self.castle_short = False
        self.castle_long_position = None
        self.castle_short_position = None

    # TODO
    # Wierd movement with Castling
    def available_moves(self, board):
        direction = ((0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1))
        available_moves = []
        self.castle_long_position = None
        self.castle_short_position = None
        for d in direction:
            pos = self.position
            r, c = [pos[0] + d[0], pos[1] + d[1]]

            if 0 <= r and r <= 7 and 0 <= c and c <= 7:
                # empty
                if board[r][c] is None:
                    available_moves.append([r, c])
                else:
                    # or can attack
                    if board[r][c].colour != self.colour:
                        available_moves.append([r, c])
        
        if self.castle_long:
            self.castle_long_position = [self.position[0],self.position[1] - 2]
            available_moves.append(self.castle_long_position)
            

        if self.castle_short:
            self.castle_short_position = [self.position[0],self.position[1] + 2]
            available_moves.append(self.castle_short_position)
            
        
        return available_moves
