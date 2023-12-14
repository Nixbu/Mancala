import math


class SimulatedBoard:
    def __init__(self, board, turn):
        self.board = board
        self.turn = turn
        self.lower_pits_state = None
        self.upper_pits_state = None
        self.side = None
        self.my_store = None
        self.rival_store = None
        self.current_pits = None
        self.turn_count = None
        self.minimize = None

    def initialize(self):
        self.lower_pits_state = [pit.num_of_beads for pit in self.board.lower_pits.values()]
        self.upper_pits_state = [pit.num_of_beads for pit in self.board.upper_pits.values()]
        self.side = self.turn
        self.my_store = self.board.lower_store.num_of_beads if self.turn else self.board.upper_store.num_of_beads
        self.rival_store = self.board.lower_store.num_of_beads if not self.turn else self.board.upper_store.num_of_beads
        self.current_pits = self.lower_pits_state if self.side else self.upper_pits_state
        self.turn_count = 0
        self.minimize = False

    def create_copy(self):
        board_copy = SimulatedBoard(self.board, self.turn)
        board_copy.lower_pits_state = self.lower_pits_state.copy()
        board_copy.upper_pits_state = self.upper_pits_state.copy()
        board_copy.side = self.side
        board_copy.my_store = self.my_store
        board_copy.rival_store = self.rival_store
        board_copy.current_pits = board_copy.lower_pits_state if board_copy.side else board_copy.upper_pits_state
        board_copy.turn_count = self.turn_count
        board_copy.minimize = self.minimize

        return board_copy

    def make_move(self, pit_number):
        beads = self.current_pits[pit_number]
        self.current_pits[pit_number] = 0

        # Spread the beads
        for bead in range(beads):
            pit_number -= 1

            if pit_number == -1:
                if self.minimize:
                    self.rival_store += 1
                else:
                    self.my_store += 1

                pit_number = 6
                self.side = not self.side
                self.current_pits = self.lower_pits_state if self.side else self.upper_pits_state

            else:
                self.current_pits[pit_number] += 1

        # Check if the player gets another turn
        if pit_number == 6:
            # Player gets another turn
            if not self.minimize:
                self.turn_count += 1

        else:
            self.turn = not self.turn
            self.minimize = not self.minimize

    def is_over(self):
        return (all(bead_num == 0 for bead_num in self.lower_pits_state)
                or all(bead_num == 0 for bead_num in self.upper_pits_state))

    def evaluate(self):
        if self.is_over() and self.my_store > self.rival_store:
            return math.inf
        else:
            return self.my_store - self.rival_store










