import pygame.draw

from utils.Settings import *
from classes.Board import *


def check_floating_in(pits, mouse_pos):
    """
    The function checks if the mouse floats in one of the pits.
    :param pits: The given pits
    :param mouse_pos: The current mouse position
    :return: None
    """
    for pit in pits:
        if pit.collided(mouse_pos):
            pit.draw_amount()


class Game:
    """
    Class representing a Game of Mancala
    """
    def __init__(self, player1, player2, ai_mode=False):
        """
        Init
        :param player1: The first player's name
        :param player2: The second player's name
        :param ai_mode: If True - skips time dilation
        """
        # Set up game window
        self.screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
        pygame.display.set_caption("Mancala")
        self.clock = pygame.time.Clock()

        # Set up game variables
        self.board = Board(self.screen)
        self.board.initialize()
        self.cup = CirclePit(self.screen, CUP_POS)
        self.turn = random.choice([True, False])
        self.turn_pits = self.board.lower_pits if self.turn else self.board.upper_pits
        self.background_img = BACKGROUND_IMG
        self.board.background_img = PLAYER1_TURN_BOARD if self.turn else PLAYER2_TURN_BOARD
        self.cup_img = CUP_IMG
        self.player1_text = arial30.render(player1 + ":", 1, WHITE)
        self.player2_text = arial30.render(player2 + ":", 1, WHITE)
        self.winner = None

        self.running = True
        self.mid_move = False
        self.ai_mode = ai_mode

    """---------------- Draw methods ----------------------"""
    def draw(self):
        """
        The method draws the entire game
        :return: None
        """
        # Draw the background, board and beads
        self.draw_background()
        self.board.draw_board()
        self.cup.draw()

        # Check if a pit is floated on to display the amount of beads in it
        if not self.mid_move:
            self.check_floating()

        pygame.display.flip()

    def draw_background(self):
        """
        The method draws the background of the game
        :return: None
        """
        # Draw background image and cup
        self.screen.blit(self.background_img, (0, 0))
        self.screen.blit(self.cup_img, CUP_IMG_POS)

        # Draw player names
        self.screen.blit(self.player1_text, PLAYER1_POS)
        self.screen.blit(self.player2_text, PLAYER2_POS)

        # Draw player scores
        self.screen.blit(arial30.render(str(self.board.lower_store.num_of_beads), 1, WHITE), P1SCORE_POS)
        self.screen.blit(arial30.render(str(self.board.upper_store.num_of_beads), 1, WHITE), P2SCORE_POS)

    def check_floating(self):
        """
        The method checks if the mouse is floating in one of the pits
        :return: None
        """
        mouse_pos = pygame.mouse.get_pos()
        check_floating_in(self.board.lower_pits.values(), mouse_pos)
        check_floating_in(self.board.upper_pits.values(), mouse_pos)

    """---------------- Game methods ----------------------"""
    def make_move(self, move):
        """
        The method makes the wanted move on the board
        :param move: The wanted move - number of the pits to
         move beads from
        :return: None
        """
        another_turn = self.check_another_turn(move)
        self.spread_beads(move)

        # Check if the game ended
        if self.check_empty():
            self.winner = self.find_winner()

        # Check if the player gets another turn
        if not another_turn:
            self.turn = not self.turn
            self.turn_pits = self.board.lower_pits if self.turn else self.board.upper_pits

        # Update board image
        self.board.background_img = PLAYER1_TURN_BOARD if self.turn else PLAYER2_TURN_BOARD

    def check_empty(self):
        """
        The method checks if current player's side is empty.
        :return: Empty - True, else - False
        """
        for pit in self.turn_pits.values():
            if pit.num_of_beads > 0:
                return False

        return True

    def find_winner(self):
        """
        The method returns who the winner is.
        :return: String
        """
        if self.board.lower_store.num_of_beads > self.board.upper_store.num_of_beads:
            return "Player 1"
        elif self.board.lower_store.num_of_beads < self.board.upper_store.num_of_beads:
            return "Player 2"
        else:
            return "Draw"

    def move_beads_to_cup(self, pit):
        """
        The method moves the beads to the cup
        :param pit: The pit to take the beads from
        :return: None
        """
        while pit.num_of_beads != 0:
            # Remove a bead and add it to the cup
            bead = pit.beads.pop()
            bead.update_pos(self.cup.next_bead_pos)
            self.cup.beads.append(bead)

            # Update cup's number of beads and bext bead position
            self.cup.num_of_beads += 1
            self.cup.update_next_bead_pos()

            # Update pit's number of beads and bext bead position
            pit.num_of_beads -= 1
            pit.update_next_bead_pos()

        # Draw the beads in the cup
        self.draw()
        pygame.display.flip()
        pygame.time.wait(300)

    def spread_beads(self, move):
        """
        The method spreads the beads from the cup to the next pits
        :param move: The number of the original pit
        :return: None
        """
        # Get the wanted pit and move the beads from it to the cup
        pit = self.turn_pits.get(move)
        self.move_beads_to_cup(pit)

        # Get board side
        curr_pit_num = int(move) - 1
        board_side = self.board.lower_pits if self.turn else self.board.upper_pits
        playing_store = self.board.lower_store if self.turn else self.board.upper_store
        spread_length = self.cup.num_of_beads
        self.board.background_img = BOARD_IMG
        self.mid_move = True

        # Spread the beads
        while spread_length > 0:

            # Get one bead
            curr_bead = self.cup.beads.pop()
            self.cup.num_of_beads -= 1
            self.cup.update_next_bead_pos()

            if curr_pit_num == 0:
                # Add to player's store
                playing_store.beads.append(curr_bead)
                curr_bead.update_pos(playing_store.next_bead_pos)
                playing_store.num_of_beads += 1
                playing_store.update_next_bead_pos()

                # Change sides
                curr_pit_num = 6
                board_side = self.board.upper_pits if board_side == self.board.lower_pits else self.board.lower_pits

            else:
                # Add to circle pits
                curr_pit = board_side[str(curr_pit_num)]
                curr_pit.beads.append(curr_bead)
                curr_pit.num_of_beads += 1
                curr_bead.update_pos(curr_pit.next_bead_pos)
                curr_pit.update_next_bead_pos()
                curr_pit_num -= 1

            # Update window
            self.draw()
            pygame.display.flip()
            if not self.ai_mode:
                pygame.time.wait(500)

            spread_length -= 1

    def check_another_turn(self, move):
        """
        The method checks if the player gets another turn
        :param move: The chosen move
        :return: True - if the player gets another turn, else - False
        """
        pit = self.turn_pits.get(move)
        return (pit.num_of_beads - int(move)) % 7 == 0

    def poll_events(self, keys):
        """
        The function polls for events in the game
        :param keys: The current state of the keyborad keys
        :return: None
        """
        # Poll for events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            if keys[pygame.K_ESCAPE]:
                self.running = False












