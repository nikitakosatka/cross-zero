from crosszero.start_screen import StartScreen
from crosszero.game import Game
import pygame

pygame.init()
size = WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode(size)

start = StartScreen(screen)
start.run()
game = Game(screen)
game.run()