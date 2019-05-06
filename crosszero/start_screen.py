from .other import load_image, terminate
import pygame

class StartScreen:
    def __init__(self, surface):
        self.surface = surface
        self.start = False
        self.background = load_image("background.png")
        self.play_button = load_image("play_button.png")

    def run(self):
        while not self.start:
            self.events()
            self.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.start = True

    def update(self):
        self.surface.blit(self.background, (0, 0))
        self.background.blit(self.play_button, (200, 100))
        pygame.display.flip()
