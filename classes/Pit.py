class Pit:
    """
    Class representing a pit in the game
    """
    def __init__(self, screen):
        """
        Init
        :param screen: Screen to draw pit on
        """
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
