from .other import load_image, terminate
import pygame

class EndScreen:
    def __init__(self, game):
        self.start = False
        self.game = game
        self.surface = game.surface
        restart = load_image("restart.png")
        self.restart_images = [(restart, (200, 100)),
                               (pygame.transform.scale(restart, (100, 50)), (200, 100))]
        self.restart = self.restart_images[0]
        self.win = load_image("win.png")
        self.background = load_image("background.png")

    def run(self):
        while not self.start:
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
        self.background.blit(self.restart[0], self.restart[1])
        self.background.blit(self.win, (230, 200))
        if self.game.find_winner() == 'x':
            self.background.blit(self.game.cross, (180, 200))
        elif self.game.find_winner() == 'o':
            self.background.blit(self.game.zero, (180, 200))
        self.mouse_handler()
        pygame.display.flip()

    def mouse_handler(self):
        pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        if pygame.Rect(*self.restart[1], *self.restart[0].get_rect().size).collidepoint(*pos):
            self.restart = self.restart_images[1]
            if mouse_pressed:
                pass
                self.start = True
                pygame.event.clear()
        else:
            self.restart = self.restart_images[0]