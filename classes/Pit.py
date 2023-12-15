"""
Class representing a pit in the board.
    @ screen : The screen to draw the Pit on
    @ beads : A list of the current beads
    @ num_of_beads : Current number of beads
"""
class Pit:
    def __init__(self, screen):
        self.screen = screen
        self.beads = []
        self.num_of_beads = 0

    def remove_beads(self):
        """
        Method for removing all the beads in the pit
        :return: None
        """
        for bead in self.beads:
            self.beads.remove(bead)
            self.num_of_beads -= 1
