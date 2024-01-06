import random

from classes.Pit import *
from .Bead import *

class CirclePit(Pit):
    """
    Class representing a circular pit
    Inheriting from class Pit
    """
    def __init__(self, screen, center):
        """
        Init
        :param screen: The screen to draw the pit on.
        :param center: The center of the pit
        """
        super().__init__(screen)
        self.radius = PIT_RADIUS
        self.center = center
        self.rect = pygame.Rect(self.center[0] - PIT_RADIUS, self.center[1] - PIT_RADIUS, 2 * PIT_RADIUS, 2 * PIT_RADIUS)
        self.next_bead_pos = [self.center[0] - 2 * BEAD_DIAMETER, self.center[1] - 2 * BEAD_DIAMETER]

    def initialize(self):
        """
        The method initializes the beads of the pit
        :return: None
        """
        self.remove_beads()
        from utils.Settings import bead_set
        for _ in range(INITIAL_BEAD_NUM):
            bead_image = random.choice(bead_set)
            self.beads.append(
                Bead(self.screen, bead_image,
                     self.next_bead_pos[0],
                     self.next_bead_pos[1]))
            self.num_of_beads += 1
            self.update_next_bead_pos()

    def draw(self):
        """
        The method draws the pit's beads
        :return: None
        """
        for bead in self.beads:
            bead.draw()

    def draw_frame(self):
        """
        The method draws the frame of the pit (For Testing)
        :return: None
        """
        pygame.draw.circle(self.screen, WHITE, self.center, self.radius, width=1)

    def collided(self, mouse_pos):
        """
        The method checks if the pit is being collided with the mouse
        :param mouse_pos: The current mouse position
        :return: True if colliding with mouse, else False
        """
        return self.rect.collidepoint(mouse_pos[0], mouse_pos[1])

    def update_next_bead_pos(self):
        """
        The method updates where the next bead should be located in the pit
        :return: None
        """
        self.next_bead_pos[0] = (self.center[0] - 2 * BEAD_DIAMETER
                                 + (self.num_of_beads * BEAD_DIAMETER) % (3 * BEAD_DIAMETER))
        self.next_bead_pos[1] = (self.center[1] - 2 * BEAD_DIAMETER +
                                 ((self.num_of_beads * BEAD_DIAMETER) // (3 * BEAD_DIAMETER)) * BEAD_DIAMETER)

    def draw_amount(self):
        """
        The method draws the amount of beads in the pit
        :return: None
        """
        amount = default_font.render(str(self.num_of_beads), 1, BLACK)
        self.screen.blit(amount, self.center)
        pygame.display.flip()


