from .CirclePit import *
from .Store import *

class Board:
    def __init__(self, screen):
        self.screen = screen
        self.upper_store = Store(screen, UP_STORE_BUFFER)
        self.lower_store = Store(screen, DOWN_STORE_BUFFER)
        self.upper_pits = {str(num): CirclePit(screen, center) for num, center in UP_PIT_DIC.items()}
        self.lower_pits = {str(num): CirclePit(screen, center) for num, center in  LOW_PIT_DIC.items()}

    def initialize(self):
        self.upper_store.remove_beads()
        self.lower_store.remove_beads()

        for pit in self.upper_pits.values():
            pit.initialize()

        for pit in self.lower_pits.values():
            pit.initialize()

    def draw_board(self):
        self.upper_store.draw()
        self.lower_store.draw()

        for pit in self.upper_pits.values():
            pit.draw()

        for pit in self.lower_pits.values():
            pit.draw()
