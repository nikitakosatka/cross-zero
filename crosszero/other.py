from os import path
import pygame


def load_image(filename):
    fullname = path.join("data", "images", filename)
    return pygame.image.load(fullname).convert_alpha()


def terminate():
    pygame.quit()
    exit()
