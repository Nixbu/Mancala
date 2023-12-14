import pygame
from .Settings import *

class Button:
    def __init__(self, screen, text, pos_x, pos_y, text_color):
        self.screen = screen
        self.text = default_font.render(text, 1, text_color)
        self.width = self.text.get_width()
        self.height = self.text.get_height()
        self.pos_x = pos_x
        self.rect = pygame.Rect(pos_x, pos_y, self.width, self.height)
        self.pos_y = pos_y

    def draw(self):
        pygame.draw.rect(self.screen, BLACK, self.rect)
        self.screen.blit(self.text, (self.pos_x, self.pos_y))

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos[0], mouse_pos[1])

    def center(self):
        self.pos_x = self.screen.get_width() // 2 - self.width // 2
        self.rect.x = self.pos_x


