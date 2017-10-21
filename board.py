import pygame

from chess_piece import Piece, Pawn, Rook, Bishop, Knight, King, Queen
from player import Player
from chess_game import PlayGame
from chess_game import BoardView

WIDTH = 50
HEIGHT = 50
PADDING = 20

BLACK = "black"
WHITE = "white"

class Board():
    def __init__(self, current_player, another_player):
        self.current_player = current_player
        self.player_a = current_player
        self.player_b = another_player

        self.game = PlayGame(self,custom = True)
        pieces = [Queen([0,1],BLACK),
                  King([2,4],BLACK),
                  Bishop([6,5],BLACK),
                  King([6,4],WHITE),
                  Bishop([2,5],WHITE),
                  Knight([7,6],WHITE)]
        self.game.add_pieces(pieces)

        self.game.start()
        self.lastPosition = [-1,-1]
        self.dragging_place = [-1,-1]
        self.movements = []

        pygame.init()
        self.font = pygame.font.SysFont("comicsansms",24)
        self.board = pygame.display.set_mode(
            (WIDTH * 15, HEIGHT * 10),
            pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption('Chess')

    def on_event(self,event):
        if event.type == pygame.QUIT:
            self.game.finish()
        else:
            pos = pygame.mouse.get_pos()
            c = (pos[0] - HEIGHT) // HEIGHT
            r = (pos[1] - WIDTH) // WIDTH
            if event.type == pygame.MOUSEBUTTONDOWN:
                p = self.game.piece_in_position([r,c])
                if p is not None and p.colour == self.current_player.colour:
                    self.game.start_drag_piece_in_position([r,c])
                    self.dragging_place = pos

            elif event.type == pygame.MOUSEBUTTONUP:
                
                if self.game.place_dragging_piece_in_position([r,c]):
                    self.current_player = self.player_a if self.current_player == self.player_b else self.player_b
                self.dragging_place = [-1,-1]

            elif event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                self.dragging_place = pos
        # check win


    def on_render(self):
        self.render_chess_piece()
        self.render_available_moves()
        self.render_last_position()
        self.render_dragging_piece()
        self.render_movements()
        pygame.display.update()

    def on_execute(self):
        while self.game.playing():
            self.init_chess_board()
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
        self.on_cleanup()

    def on_cleanup(self):
        pygame.quit()

    def init_chess_board(self):
        BoardView.render_whole_board(self.board, [WIDTH,HEIGHT], PADDING)
        BoardView.render_chess_coordinate(self.board,self.font,[WIDTH,HEIGHT],PADDING)
        for row in range(8):
            for column in range(8):
                BoardView.render_chess_board(self.board,
                                             [row,column],
                                             (WIDTH * (row + 1),
                                             HEIGHT * (column + 1),
                                             WIDTH,
                                             HEIGHT))
    def render_available_moves(self):
        for m in self.game.available_moves():
            rect = [(m[1] + 1) * WIDTH, (m[0] + 1) * HEIGHT, WIDTH, HEIGHT]
            BoardView.render_available_moves(self.board, rect)

    def render_dragging_piece(self):
        p = self.game.dragging_piece()
        if p is not None:
            BoardView.render_piece(self.board, p.name,
                        (self.dragging_place[0] - WIDTH // 2,
                        self.dragging_place[1] - HEIGHT // 2))


    def render_chess_piece(self):
        for r in range(8):
            for c in range(8):
                p = self.game.piece_in_position([r,c])
                if p is not None:
                    BoardView.render_piece(self.board, p.name, (HEIGHT * (c + 1), WIDTH * (r + 1)))

    def render_last_position(self):
        if self.lastPosition[0] >= 0 and self.lastPosition[1] >= 0:
            BoardView.render_last_position(self.board,
                                (WIDTH * (self.lastPosition[1] + 1),
                                 HEIGHT * (self.lastPosition[0] + 1),
                                 WIDTH,
                                 HEIGHT))
    def render_movements(self):
        pos = [WIDTH * 11, HEIGHT]
        for i in range(len(self.movements)):
            movement = self.movements[i]
            position = [pos[0], pos[1] + i * 20]
            BoardView.render_movement(self.board, movement, self.font, position)

    def add_movement_record(self, movement):
        self.lastPosition = movement
        self.movements.append([self.current_player, movement])
         

