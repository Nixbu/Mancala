import pygame

from utils import *


def draw(screen, board):
    screen.blit(BOARD_IMG, (0, 0))
    board.draw_board()
    pygame.display.flip()


def spread_beads(num, pit, turn, board):
    curr_pit_num = int(num) - 1
    board_side = board.lower_pits if turn else board.upper_pits
    playing_store = board.lower_store if turn else board.upper_store
    spread_length = pit.num_of_beads

    while spread_length > 0:

        # Get one bead
        curr_bead = pit.beads.pop()
        pit.num_of_beads -= 1
        pit.update_next_bead_pos()

        if curr_pit_num == 0:
            # Add to player's store
            playing_store.beads.append(curr_bead)
            curr_bead.update_pos(playing_store.next_bead_pos)
            playing_store.num_of_beads += 1
            playing_store.update_next_bead_pos()

            # Change sides
            curr_pit_num = 6
            board_side = board.upper_pits if board_side == board.lower_pits else board.lower_pits

        else:
            # Add to circle pits
            curr_pit = board_side[str(curr_pit_num)]
            curr_pit.beads.append(curr_bead)
            curr_pit.num_of_beads += 1
            curr_bead.update_pos(curr_pit.next_bead_pos)
            curr_pit.update_next_bead_pos()
            curr_pit_num -= 1

        draw(board.screen, board)
        pygame.time.wait(500)

        spread_length -= 1

    # Determine if the player gets another turn
    return curr_pit_num == 6


def check_empty(turn_pits):
    for _, pit in turn_pits.items():
        if pit.num_of_beads > 0:
            return False

    return True


def find_winner(board):
    if board.lower_store.num_of_beads > board.upper_store.num_of_beads:
        return "Player 1"
    elif board.lower_store.num_of_beads < board.upper_store.num_of_beads:
        return "Player 2"
    else:
        return "Draw"


def print_game_state(board):
    print(f"Player 1 num of beads: {board.lower_store.num_of_beads}")
    print(f"Player 2 num of beads: {board.upper_store.num_of_beads}")

# TODO Create 2 options - 1v1 or AI vs Player, 2 different windows, and a main window
def main():
    # 1v1 or AI
    option = input("1 for AI, 2 for 1v1: ")

    if option == "1":
        ai_game()
    elif option == "2":
        one_vs_one()

def ai_game():
    # screen Setup
    screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
    pygame.display.set_caption("Mancala")
    clock = pygame.time.Clock()

    # Board Setup
    board = Board(screen)
    board.initialize()

    # Game Variables
    running = True
    turn = random.choice([True, False])
    print(turn)
    turn_pits = board.lower_pits if turn else board.upper_pits
    winner = None
    computer = AIPlayer(board, 9)

    # Game Loop
    while running:

        # Get keyboard state
        keys = pygame.key.get_pressed()

        # poll for events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if keys[pygame.K_ESCAPE]:
                running = False

        # Human turn
        if turn:
            # Check if mouse clicked
            if pygame.mouse.get_pressed(3)[0]:
                mouse_pos = pygame.mouse.get_pos()

                # Turn logic
                for num, pit in turn_pits.items():
                    # Check if pit is clicked
                    if pit.clicked(mouse_pos) and len(pit.beads) != 0:
                        # Spread the beads
                        another_turn = spread_beads(num, pit, turn, board)

                        print_game_state(board)

                        # Check if the game ended
                        if check_empty(turn_pits):
                            winner = find_winner(board)
                            break

                        # Check if the player gets another turn
                        if not another_turn:
                            turn = not turn
                            turn_pits = board.lower_pits if turn else board.upper_pits

                        print(turn)

        # AI turn
        else:
            move = str(computer.choose_best_move() + 1)
            print(move)
            pit = turn_pits.get(move)
            another_turn = spread_beads(move, pit, turn, board)

            print_game_state(board)

            # Check if the game ended
            if check_empty(turn_pits):
                winner = find_winner(board)
                break

            # Check if the player gets another turn
            if not another_turn:
                turn = not turn
                turn_pits = board.lower_pits if turn else board.upper_pits

            print(turn)

        # Check if there is a winner
        if winner is not None:
            print(f"The winner is... {winner}!")
            pygame.time.wait(5000)
            break

        draw(screen, board)

        # limits FPS to 60
        clock.tick(60)

    pygame.quit()


def one_vs_one():
    # screen Setup
    screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
    pygame.display.set_caption("Mancala")
    clock = pygame.time.Clock()

    # Board Setup
    board = Board(screen)
    board.initialize()

    # Game Variables
    running = True
    turn = random.choice([True, False])
    print(turn)
    turn_pits = board.lower_pits if turn else board.upper_pits
    winner = None

    # Game Loop
    while running:

        # Get keyboard state
        keys = pygame.key.get_pressed()

        # poll for events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if keys[pygame.K_ESCAPE]:
                running = False

        # Check if mouse clicked
        if pygame.mouse.get_pressed(3)[0]:
            mouse_pos = pygame.mouse.get_pos()

            # Turn logic
            for num, pit in turn_pits.items():
                # Check if pit is clicked
                if pit.clicked(mouse_pos) and len(pit.beads) != 0:

                    # Spread the beads
                    another_turn = spread_beads(num, pit, turn, board)

                    print_game_state(board)

                    # Check if the game ended
                    if check_empty(turn_pits):
                        winner = find_winner(board)
                        break

                    # Check if the player gets another turn
                    if not another_turn:
                        turn = not turn
                        turn_pits = board.lower_pits if turn else board.upper_pits

                    print(turn)

        # Check if there is a winner
        if winner is not None:
            print(f"The winner is... {winner}!")
            pygame.time.wait(5000)
            break

        draw(screen, board)

        # limits FPS to 60
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
