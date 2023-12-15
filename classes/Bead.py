import pygame.draw

from utils.Settings import *


class Bead:
    def __init__(self, screen, img, pos_x, pos_y):
        self.screen = screen
        self.img = img
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = BEAD_RADIUS

    def draw(self):
        self.screen.blit(self.img, (self.pos_x, self.pos_y))

    def update_pos(self, pos):
        self.pos_x = pos[0]
        self.pos_y = pos[1]

