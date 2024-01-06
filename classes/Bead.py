import pygame.draw

from utils.Settings import *


class Bead:
    """
    A class representing a bead in the Mancala game
    """
    def __init__(self, screen, img, pos_x, pos_y):
        """
        Init
        :param screen: The screen to draw on
        :param img: The image of the bead
        :param pos_x: The X position of the bead
        :param pos_y: The Y position of the bead
        """
        self.screen = screen
        self.img = img
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = BEAD_RADIUS

    def draw(self):
        """
        Method to draw the bead
        :return: None
        """
        self.screen.blit(self.img, (self.pos_x, self.pos_y))

    def update_pos(self, pos):
        """
        Method to update the position of the bead on the screen
        :param pos: The new position
        :return: None
        """
        self.pos_x = pos[0]
        self.pos_y = pos[1]

