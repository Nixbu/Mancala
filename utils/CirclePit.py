import random

from .Pit import *


class CirclePit(Pit):
    def __init__(self, screen, center):
        super().__init__(screen)
        self.radius = PIT_RADIUS
        self.center = center
        self.rect = pygame.Rect(self.center[0] - PIT_RADIUS, self.center[1] - PIT_RADIUS, 2 * PIT_RADIUS, 2 * PIT_RADIUS)
        self.next_bead_pos = [self.center[0] - 2 * BEAD_DIAMETER, self.center[1] - 2 * BEAD_DIAMETER]

    def initialize(self):
        self.remove_beads()

        for _ in range(INITIAL_BEAD_NUM):
            bead_image = random.choice(BEAD_IMAGE_LIST)
            self.beads.append(
                Bead(self.screen, bead_image,
                     self.next_bead_pos[0],
                     self.next_bead_pos[1]))
            self.num_of_beads += 1
            self.update_next_bead_pos()

    def draw(self):
        for bead in self.beads:
            bead.draw()

    def draw_frame(self):
        pygame.draw.circle(self.screen, WHITE, self.center, self.radius, width=1)

    def clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos[0], mouse_pos[1])

    def update_next_bead_pos(self):
        self.next_bead_pos[0] = (self.center[0] - 2 * BEAD_DIAMETER
                                 + (self.num_of_beads * BEAD_DIAMETER) % (3 * BEAD_DIAMETER))
        self.next_bead_pos[1] = (self.center[1] - 2 * BEAD_DIAMETER +
                                 ((self.num_of_beads * BEAD_DIAMETER) // (3 * BEAD_DIAMETER)) * BEAD_DIAMETER)
