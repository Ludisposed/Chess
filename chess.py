import itertools
import pygame

DARK=(8,118,49)
LIGHT=(181,221,196)
WIDTH = 50
HEIGHT = 50
LAST_POSTION_COLOUR = (0,0,0)

'''
Class of the Player
'''
class Player():
    def __init__(self, colour, name):
        self.colour = colour
        self.name = name
        self.castle_long = False
        self.castle_short = False

    def __str__(self):
        return '{} as {}'.format(self.name, self.colour)

'''
Class of the board
'''
class Board():
    def __init__(self, current_player):
        self.current_player = current_player
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.grid_init()
        self.lastPosition = [-1,-1]
        self.running = True
        self.dragging = False
        self.dragging_piece = None
        self.dragging_place = [-1,-1]

        pygame.init()
        pygame.font.init()
        self.board = pygame.display.set_mode(
            (WIDTH * 8, HEIGHT * 8),
            pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('Chess')
        
    def grid_init(self):
        self.grid[0] = [Rook([0,0],'black'),
                        Knight([0,1],'black'),
                        Bishop([0,2],'black'),
                        Queen([0,3],'black'),
                        King([0,4],'black'),
                        Bishop([0,5],'black'),
                        Knight([0,6],'black'),
                        Rook([0,7],'black')]

        self.grid[-1] = [Rook([7,0],'white'),
                         Knight([7,1],'white'),
                         Bishop([7,2],'white'),
                         Queen([7,3],'white'),
                         King([7,4],'white'),
                         Bishop([7,5],'white'),
                         Knight([7,6],'white'),
                         Rook([7,7],'white')]

        self.grid[1] = [Pawn([1, i], 'black') for i in range(8)]
        self.grid[-2] = [Pawn([6, i], 'white') for i in range(8)]

    def on_event(self,event):
        if event.type == pygame.QUIT:
            self.running = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            c = pos[0] // HEIGHT
            r = pos[1] // WIDTH

            if self.grid[r][c] is not None:
                self.dragging = True
                self.dragging_piece = self.grid[r][c]
                self.dragging_place = pos
                self.grid[r][c] = None

                print self.dragging_piece.available_moves()

                if not self.dragging_piece.available_moves() is None:
                    for pos in self.dragging_piece.available_moves():
                        if not self.grid[pos[0]][pos[1]] is None:
                            pass
                            # Is available
                            # Render available move
                        else:
                            # Skip till next direction
                            pass

        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            c = pos[0] // HEIGHT
            r = pos[1] // WIDTH
            if self.dragging:
                if self.grid[r][c] is not None:
                    p = self.grid[r][c]
                    if p.colour == self.dragging_piece.colour:
                        pos = self.dragging_piece.position
                        self.grid[pos[0]][pos[1]] = self.dragging_piece
                    else:
                        #identify if the dragging win
                        if False:
                            pass
                        else:
                            pos = self.dragging_piece.position
                            self.grid[pos[0]][pos[1]] = self.dragging_piece

                else:
                    self.dragging_piece.position = [r,c]
                    self.grid[r][c] = self.dragging_piece

            self.dragging = False
            self.dragging_piece = None
            self.dragging_place = [-1,-1]

        elif event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            if self.dragging:
                # check is it in availabel moves
                self.dragging_place = pos

        #check win

    def on_render(self):
        self.render_chess_piece()
        self.render_dragging_piece()
        self.render_available_moves()
        self.render_last_position()
        pygame.display.update()

    def on_execute(self):
        while self.running:
            self.chess_board_init()
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
        self.on_cleanup()

    def on_cleanup(self):
        pygame.quit()

    def chess_board_init(self):
        for row in range(8):
            for column in range(8):
                colour = DARK
                if (row % 2 == 0 and column % 2 == 0) or (row % 2 == 1 and column % 2 == 1):
                    colour = LIGHT
                pygame.draw.rect(self.board, colour, (WIDTH * column, HEIGHT * row, WIDTH, HEIGHT), 0)


    def render_available_moves(self):
        pass
    
    def render_dragging_piece(self):
        if self.dragging:
            piece = pygame.image.load('Images/' + self.dragging_piece.name + '.png')
            self.board.blit(piece ,(self.dragging_place[0] - WIDTH // 2, self.dragging_place[1] - HEIGHT // 2))

    def render_chess_piece(self):
        for r in range(8):
            for c in range(8):
                if self.grid[r][c] is not None:
                    p = self.grid[r][c]
                    piece = pygame.image.load('Images/' + p.name + '.png')
                    self.board.blit(piece,(HEIGHT * c, WIDTH * r))

    def render_last_position(self):
        if self.lastPosition[0] > 0 and self.lastPosition[1] > 0:
            pygame.draw.rect(self._display_surf, LAST_POSTION_COLOUR,
                             (WIDTH * self.lastPosition[0] + WIDTH // 2,
                              WIDTH * self.lastPosition[1] + WIDTH // 2,
                              WIDTH,
                              WIDTH), 1)

'''
Class of the chess Pieces
'''
class Piece(object):
    def __init__(self, position, colour, direction):
        self.name = ''
        self.position = position
        self.colour = colour
        self.direction = direction
        
    def available_moves(self, directions):
        valid_moves = []
        
        for d in directions:
            pos = self.position
            while 0 >= pos[0] <= 7 and 0 >= pos[0] <= 7 and pos != self.position:
                valid_moves.append(pos)
                pos[0] += d[0]
                pos[1] += d[1]

        return valid_moves

'''
Classes for individual pieces derived from Piece class
'''
class Pawn(Piece):
    def __init__(self, position, colour):
        self.directions = ()
        self.name = colour + '_pawn' 
        Piece().__init__(self, position, colour, direction)

    # wierd movements
    def available_moves(self):
        pass

class Knight(Piece):
    def __init__(self, position, colour):
        self.name = colour + '_knight'
        self.directions = () 
        Piece().__init__(self, position, colour, direction)

    # wierd movements
    def available_moves(self):
        pass

class Rook(Piece):
    def __init__(self, position, colour):
        self.name = colour + '_rook'
        self.directions = ((0, 1), (1, 0), (-1, 0), (0, -1)) 
        Piece().__init__(self, position, colour, direction)
        
    def available_moves(self):
        super().available_moves(self.directions)

class Bishop(Piece):
    def __init__(self, position, colour):
        self.name = colour + '_bishop'
        self.directions = ((-1, -1), (1, 1), (-1, 1), (1, -1)) 
        Piece().__init__(self, position, colour, direction)
        
    def available_moves(self):
        super().available_moves(self.directions)

class Queen(Piece):
    def __init__(self, position, colour):
        self.name = colour + '_queen'
        self.directions = ((0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)) 
        Piece().__init__(self, position, colour, direction)
        
    def available_moves(self):
        super().available_moves(self.directions)

class King(Piece):
    def __init__(self, position, colour):
        self.name = colour + '_king'
        self.directions = ((0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1))
        Piece().__init__(self, position, colour, direction) 
        
    def available_moves(self):
        super().available_moves(self.directions)

if __name__ == '__main__':
    board = Board('White')
    board.on_execute()
