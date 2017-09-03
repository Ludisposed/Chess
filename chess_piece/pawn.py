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
    def available_moves(self, board):
        available_moves = []
        last_moved_piece = False
        skip = False
        
        for d in self.direction:
            pos = self.position
            r, c = [pos[0] + d[0], pos[1] + d[1]]

            # Capture
            if c !- pos[1]:
                if not board[r][c] is None and self.colour != board[r][c].colour:
                    available_moves.append([r, c])
            # Move
            else:
                if not skip:
                    if not board[r][c] is None:
                        available_moves.append([r, c])
                    else:
                        skip = True

        if last_moved_piece:
            pass
            # Add en-passant                
                
        return available_moves
