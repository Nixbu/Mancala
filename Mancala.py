import pygame

from utils import *

"""---------------- Draw functions ----------------------"""
def draw_main_screen(main_window, main_title, ai_option, one_vs_one_option):
    main_window.blit(BACKGROUND_IMG, (0, 0))
    main_window.blit(BOARD_IMG, (SCR_WIDTH // 2 - BOARD_IMG.get_width() // 2, SCR_HEIGHT // 2 - BOARD_IMG.get_height() // 2))
    main_window.blit(main_title, (SCR_WIDTH // 2 - main_title.get_width() // 2,
                                  SCR_HEIGHT // 2 - main_title.get_height() // 2))
    ai_option.draw()
    one_vs_one_option.draw()
    pygame.display.flip()

def draw_game(screen, board, mouse_pos, player1_text, player2_text):
    # Draw the background, board and beads
    draw_background(screen, player1_text, player2_text)
    board.draw_board()

    # Check if a pit is floated on to display the amount of beads in it
    check_floating(board, mouse_pos)

    pygame.display.flip()

def draw_background(screen, player1_text, player2_text):
    screen.blit(BACKGROUND_IMG, (0, 0))
    screen.blit(player1_text, PLAYER1_POS)
    screen.blit(player2_text, PLAYER2_POS)


def spread_beads(num, pit, turn, board):
    curr_pit_num = int(num) - 1
    board_side = board.lower_pits if turn else board.upper_pits
    playing_store = board.lower_store if turn else board.upper_store
    spread_length = pit.num_of_beads
    board.background_img = BOARD_IMG

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

        board.draw_board()
        pygame.time.wait(500)

        spread_length -= 1

    # Determine if the player gets another turn
    return curr_pit_num == 6


def check_empty(turn_pits):
    for pit in turn_pits.values():
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


def main():
    # Main window setup
    main_window = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
    pygame.display.set_caption("Mancala")

    # Main title setup
    main_title = get_font("Times new roman", 40).render("MANCALA", 1, BLACK)

    # Main screen game variables
    running = True
    ai_option = Button(main_window, "AI Player", 0, 300)
    one_vs_one_option = Button(main_window, "One vs One", 0, 450)
    ai_option.center()
    one_vs_one_option.center()

    while running:
        keys = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if keys[pygame.K_ESCAPE]:
                running = False

        # Check if the mouse is clicked
        if pygame.mouse.get_pressed(3)[0]:
            # AI player game
            if ai_option.is_clicked(mouse_pos):
                ai_game()
                break

            # 1 vs 1 Game
            if one_vs_one_option.is_clicked(mouse_pos):
                one_vs_one()
                break

        draw_main_screen(main_window, main_title, ai_option, one_vs_one_option)

    pygame.quit()


# def check_another_turn(num, pit):
#     return (pit.num_of_beads - int(num)) % 7


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
    board.background_img = PLAYER1_TURN_BOARD if turn else PLAYER2_TURN_BOARD
    player1_text = get_font("Arial", 30).render("Player 1", 1, WHITE)
    player2_text = get_font("Arial", 30).render("AI Player", 1, WHITE)

    winner = None
    computer = AIPlayer(board, 11)

    # Game Loop
    while running:

        # Get keyboard state
        keys = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        draw_game(screen, board, mouse_pos, player1_text, player2_text)

        # Poll for events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if keys[pygame.K_ESCAPE]:
                running = False

        # Human turn
        if turn:
            # Check if mouse clicked
            if pygame.mouse.get_pressed(3)[0]:
                # Turn logic
                for num, pit in turn_pits.items():
                    # Check if pit is clicked
                    if pit.collided(mouse_pos) and len(pit.beads) != 0:
                        # Spread the beads
                        # another_turn = check_another_turn(num, pit)
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

                        # Update board image
                        board.background_img = PLAYER1_TURN_BOARD if turn else PLAYER2_TURN_BOARD

        # AI turn
        else:
            move = str(computer.choose_best_move())
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

            # Update board image
            board.background_img = PLAYER1_TURN_BOARD if turn else PLAYER2_TURN_BOARD

        # Check if there is a winner
        if winner is not None:
            print(f"The winner is... {winner}!")
            pygame.time.wait(5000)
            break

        # limits FPS to 60
        clock.tick(60)

    pygame.quit()


def check_floating_in(pits, mouse_pos):
    for pit in pits:
        if pit.collided(mouse_pos):
            pit.draw_amount()


def check_floating(board, mouse_pos):
    check_floating_in(board.lower_pits.values(), mouse_pos)
    check_floating_in(board.upper_pits.values(), mouse_pos)

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
    board.background_img = PLAYER1_TURN_BOARD if turn else PLAYER2_TURN_BOARD
    player1_text = get_font("Arial", 30).render("Player 1", 1, WHITE)
    player2_text = get_font("Arial", 30).render("Player 2", 1, WHITE)
    winner = None

    # Game Loop
    while running:

        # Get keyboard state
        keys = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        draw_game(screen, board, mouse_pos, player1_text, player2_text)

        # poll for events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if keys[pygame.K_ESCAPE]:
                running = False

        # Check if mouse clicked
        if pygame.mouse.get_pressed(3)[0]:

            # Turn logic
            for num, pit in turn_pits.items():
                # Check if pit is clicked
                if pit.collided(mouse_pos) and len(pit.beads) != 0:

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

                    # Update board image
                    board.background_img = PLAYER1_TURN_BOARD if turn else PLAYER2_TURN_BOARD

                    print(turn)

        # Check if there is a winner
        if winner is not None:
            print(f"The winner is... {winner}!")
            pygame.time.wait(5000)
            break

        # limits FPS to 60
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
