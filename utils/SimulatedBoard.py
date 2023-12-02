class SimulatedBoard:
    def __init__(self, board, turn):
        self.lower_pits_state = [pit.num_of_beads for pit in board.lower_pits.values]
        self.upper_pits_state = [pit.num_of_beads for pit in board.upper_pits.values]
        self.turn = turn
        self.side = turn
        if self.side:
            self.my_store = board.lower_store.num_of_beads
            self.rival_store = board.upper_store.num_of_beads
        else:
            self.my_store = board.upper_store.num_of_beads
            self.rival_store = board.lower_store.num_of_beads

    def make_move(self, pit_number):
        current_pits = self.lower_pits_state if self.side else self.upper_pits_state
        beads = current_pits[pit_number]
        current_pits[pit_number] = 0

        for bead in range(beads):
            pit_number -= 1

            if pit_number == -1:
                self.my_store += 1
                pit_number = 6
                self.side = not self.side
                current_pits = self.lower_pits_state if self.side else self.upper_pits_state
                continue
            else:
                current_pits[pit_number] += 1








