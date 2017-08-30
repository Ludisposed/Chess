import pygame

DARK=(8,118,49)
LIGHT=(181,221,196)
LAST_POSTION_COLOUR = (0,0,0)
AVAILABLE_MOVE_COLOUR = (0,0,0)

class BoardView():
    @classmethod
    def render_chess_board(self, board, position, rect):
        colour = LIGHT if (position[0] % 2) == (position[1] % 2) else DARK
        pygame.draw.rect(board, colour, rect, 0)

    @classmethod
    def render_available_moves(self, board,center):
        radius = 10
        pygame.draw.circle(board, AVAILABLE_MOVE_COLOUR, center, radius, 0)

    @classmethod
    def render_piece(self, board, piece_image_name, position):
        piece = pygame.image.load('Images/' + piece_image_name + '.png')
        board.blit(piece ,(position[0], position[1]))

    @classmethod
    def render_last_position(self,board, rect):
        pygame.draw.rect(board, LAST_POSTION_COLOUR, rect, 1)
