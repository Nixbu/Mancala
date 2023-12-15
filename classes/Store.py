from classes.Pit import *
from utils.Settings import *


class Store(Pit):
    def __init__(self, screen, side):
        super().__init__(screen)
        self.width = STORE_WIDTH
        self.height = STORE_HEIGHT
        self.x = STORE_BUFFER
        self.y = side
        self.rect = (self.x, self.y, self.width, self.height)
        self.first_bead_pos = [self.x + BEAD_DIAMETER, self.y + self.height // 2 - 2 * BEAD_DIAMETER]
        self.next_bead_pos = [self.first_bead_pos[0], self.first_bead_pos[1]]

    def draw(self):
        for bead in self.beads:
            bead.draw()

    def draw_frame(self):
        pygame.draw.rect(self.screen, WHITE, self.rect, width=1)

    def clicked(self, mouse_pos):
        return pygame.Rect(self.rect).collidepoint(mouse_pos[0], mouse_pos[1])

    def update_next_bead_pos(self):
        self.next_bead_pos[0] = self.first_bead_pos[0] + (BEAD_DIAMETER * self.num_of_beads) % (12 * BEAD_DIAMETER)
        self.next_bead_pos[1] = self.first_bead_pos[1] + (
                    (BEAD_DIAMETER * self.num_of_beads) // (12 * BEAD_DIAMETER)) * BEAD_DIAMETER
