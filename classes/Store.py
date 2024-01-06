from classes.Pit import *
from utils.Settings import *


class Store(Pit):
    """
    Class representing a store pit
    Inheriting from the class Pit
    """
    def __init__(self, screen, side):
        """
        Init
        :param screen: The screen to draw the store on
        :param side: The side of the store
        """
        super().__init__(screen)
        self.width = STORE_WIDTH
        self.height = STORE_HEIGHT
        self.x = STORE_BUFFER
        self.y = side
        self.rect = (self.x, self.y, self.width, self.height)
        self.first_bead_pos = [self.x + BEAD_DIAMETER, self.y + self.height // 2 - 2 * BEAD_DIAMETER]
        self.next_bead_pos = [self.first_bead_pos[0], self.first_bead_pos[1]]

    def draw(self):
        """
        The method draws the store's beads on the screen
        :return: None
        """
        for bead in self.beads:
            bead.draw()

    def draw_frame(self):
        """
        The method draws the frame of the store (for testing
        :return: None
        """
        pygame.draw.rect(self.screen, WHITE, self.rect, width=1)

    def update_next_bead_pos(self):
        """
        The method updates where is the next bead position
        :return:
        """
        self.next_bead_pos[0] = self.first_bead_pos[0] + (BEAD_DIAMETER * self.num_of_beads) % (12 * BEAD_DIAMETER)
        self.next_bead_pos[1] = self.first_bead_pos[1] + (
                    (BEAD_DIAMETER * self.num_of_beads) // (12 * BEAD_DIAMETER)) * BEAD_DIAMETER
