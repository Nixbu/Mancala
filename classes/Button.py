import pygame
from utils.Settings import *

class Button:
    """
    Class representing a button
    """
    def __init__(self, screen, text, pos_x, pos_y, text_color):
        """
        Init
        :param screen: The screen to draw the button on
        :param text: Wanted text on the button
        :param pos_x: The X position of the button
        :param pos_y: The Y position of the button
        :param text_color: The color of the text
        """
        self.screen = screen
        self.text = default_font.render(text, 1, text_color)
        self.width = self.text.get_width()
        self.height = self.text.get_height()
        self.pos_x = pos_x
        self.rect = pygame.Rect(pos_x, pos_y, self.width, self.height)
        self.pos_y = pos_y

    def draw(self):
        """
        The method draws the button on the screen
        :return: None
        """
        pygame.draw.rect(self.screen, BLACK, self.rect)
        self.screen.blit(self.text, (self.pos_x, self.pos_y))

    def is_clicked(self, mouse_pos):
        """
        The method returns True if the button is clicked, else False
        :param mouse_pos: The current mouse position
        :return: True if colliding, else False
        """
        return self.rect.collidepoint(mouse_pos[0], mouse_pos[1])

    def center(self):
        """
        The function centers the X posistion of the button
        :return: None
        """
        self.pos_x = self.screen.get_width() // 2 - self.width // 2
        self.rect.x = self.pos_x


