from .other import load_image, terminate
from .end_screen import EndScreen
import pygame


class Game:
    def __init__(self, surface):
        self.surface = surface
        self.background = load_image("main_background.png")
        self.cross = load_image("cross.png")
        self.zero = load_image("zero.png")
        self.table = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.players = ['x', 'o']
        self.table_coords = [[(145, 65), (220, 65), (300, 65)],
                             [(145, 165), (220, 165), (300, 165)],
                             [(145, 265), (220, 265), (300, 265)]]
        self.clock = pygame.time.Clock()
        self.t = 0

    def run(self):
        while True:
            self.events()
            self.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_handler()

    def update(self):
        self.surface.blit(self.background, (0, 0))
        self.set_symbols()
        if self.t:
            self.end()
            self.__init__(self.surface)
        if self.find_winner():
            print(self.table)
            self.t = 1

    def set_symbols(self):
        for row in range(len(self.table)):
            for col in range(len(self.table[row])):
                if self.table[row][col] == 'x':
                    self.background.blit(self.cross, self.table_coords[row][col])

                elif self.table[row][col] == 'o':
                    self.background.blit(self.zero, self.table_coords[row][col])
        pygame.display.flip()

    def mouse_handler(self):
        pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        for row in range(len(self.table)):
            for col in range(len(self.table[row])):
                if pygame.Rect(self.table_coords[row][col], (50, 50)).collidepoint(*pos):
                    if mouse_pressed and self.table[row][col] == 0:
                        self.table[row][col] = self.players[0]
                        self.players.reverse()

    def find_winner(self):
        for sym in self.players:
            if (self.table[0][0] == self.table[0][1] == self.table[0][2] == sym) or (
                    self.table[1][0] == self.table[1][1] == self.table[1][2] == sym) or (
                    self.table[2][0] == self.table[2][1] == self.table[2][2] == sym) or (

                    self.table[0][0] == self.table[1][0] == self.table[2][0] == sym) or (
                    self.table[0][1] == self.table[1][1] == self.table[2][1] == sym) or (
                    self.table[0][2] == self.table[1][2] == self.table[2][2] == sym) or (

                    self.table[0][0] == self.table[1][1] == self.table[2][2] == sym) or (
                    self.table[0][2] == self.table[1][1] == self.table[2][0] == sym):
                return sym

    def end(self):
        ending = EndScreen(self)
        ending.run()
