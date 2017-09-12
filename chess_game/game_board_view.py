import pygame
import pygame.gfxdraw

DARK=(8,118,49)
LIGHT=(181,221,196)
LAST_POSTION_COLOUR = (0,0,0)
AVAILABLE_MOVE_COLOUR = pygame.Color(0,0,0,155)

class BoardView():
    @classmethod
    def render_whole_board(self,board, rect, padding):
        w_width = rect[0] * 15
        w_height = rect[1] * 10
        pygame.draw.rect(board, DARK, (0, 0, w_width, w_height), 0)

        #padding rect
        p_width = rect[0] * 8 + padding * 2
        p_height = rect[1] * 8 + padding * 2
        pygame.draw.rect(board, LIGHT,(rect[0] - padding, rect[1] - padding, p_width, p_height), 0)

        #chess game rect
        line = 3
        c_x = rect[0] - line
        c_y = rect[1] - line
        c_width = rect[0] * 8 + line * 2
        c_height = rect[1] * 8 + line * 2
        pygame.draw.rect(board, DARK, (c_x, c_y, c_width, c_height), 0)
    @classmethod
    def render_chess_coordinate(self, board, font, rect, padding):
        def render_text(board, is_number, positions, t, font, rect, padding):
            for position in positions:
                text = font.render(t,True,(255,255,255))
                text_w = text.get_rect().width
                text_h = text.get_rect().height
                x_pos = position[0] + (rect[0] - text_w - (padding if is_number else 0)) // 2
                y_pos = position[1] + (rect[1] - text_h - (0 if is_number else padding)) // 2
                board.blit(text,(x_pos, y_pos))
        
        for t in range(1,9):
            y_pos = (9 - t) * rect[1]
            positions = [(0, y_pos),(rect[0] * 9 + padding, y_pos)]
            t = str(t)
            render_text(board, True, positions, t, font, rect, padding)

        for t in range(ord('A'),ord('I')):
            x_pos = (t - ord('A') + 1) * rect[0]
            positions = [(x_pos,0),(x_pos,rect[1] * 9 + padding)]
            t = chr(t)
            render_text(board, False, positions, t, font, rect, padding)

            
    @classmethod
    def render_chess_board(self, board, position, rect):
        colour = LIGHT if (position[0] % 2) == (position[1] % 2) else DARK
        pygame.draw.rect(board, colour, rect, 0)

    @classmethod
    def render_available_moves(self, board, rect):
        pygame.gfxdraw.box(board, pygame.Rect(rect), AVAILABLE_MOVE_COLOUR)

    @classmethod
    def render_piece(self, board, piece_image_name, position):
        piece = pygame.image.load('Images/' + piece_image_name + '.png')
        board.blit(piece ,(position[0], position[1]))

    @classmethod
    def render_last_position(self,board, rect):
        pygame.draw.rect(board, LAST_POSTION_COLOUR, rect, 1)

    @classmethod
    def render_movement(self, board, movement, font, position):
        player = movement[0]
        t = player.name + '  ' + chr(movement[1][1] + ord('A')) + str(8 - movement[1][0])
        text = font.render(t,True,(255,255,255))
        board.blit(text,position)
