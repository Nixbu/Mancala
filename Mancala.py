import pygame

from utils import *
from classes import *

def draw_main_screen(main_window, main_title, ai_vs_player_option, pvp_option, ai_vs_ai_button, options_button):
    """
    The function draws the main screen
    :param main_window: Main window object
    :param main_title: The title of the window
    :param ai_vs_player_option: Button for ai vs player
    :param pvp_option:  Button for player vs player
    :param ai_vs_ai_button: Button for ai vs ai
    :param options_button: Button for options
    :return: None
    """
    main_window.blit(BACKGROUND_IMG, (0, 0))
    main_window.blit(BOARD_IMG,
                     (SCR_WIDTH // 2 - BOARD_IMG.get_width() // 2, SCR_HEIGHT // 2 - BOARD_IMG.get_height() // 2))
    main_window.blit(main_title, (SCR_WIDTH // 2 - main_title.get_width() // 2,
                                  SCR_HEIGHT // 2 - main_title.get_height() // 2))
    ai_vs_player_option.draw()
    pvp_option.draw()
    ai_vs_ai_button.draw()
    options_button.draw()

    pygame.display.flip()


def main():
    # Main window setup
    main_window = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
    pygame.display.set_caption("Mancala")

    # Main title setup
    main_title = get_font("Times new roman", 40).render("MANCALA", 1, BLACK)

    # Main screen game variables
    running = True
    ai_vs_player_button = Button(main_window, "AI vs Player", 50, 400, WHITE)
    pvp_button = Button(main_window, "Player vs Player", 50, 450, WHITE)
    ai_vs_ai_button = Button(main_window, "AI vs AI", 50, 500, WHITE)
    options_button = Button(main_window, "Options", 50, 550, WHITE)

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
            # AI vs player game
            if ai_vs_player_button.is_clicked(mouse_pos):
                ai_vs_player_game()
                continue

            # Player vs Player game
            if pvp_button.is_clicked(mouse_pos):
                one_vs_one()
                continue

            # AI vs AI game
            if ai_vs_ai_button.is_clicked(mouse_pos):
                ai_vs_ai_game()
                continue

            if options_button.is_clicked(mouse_pos):
                options()
                pygame.time.wait(500)
                continue

        draw_main_screen(main_window, main_title, ai_vs_player_button, pvp_button, ai_vs_ai_button, options_button)

    pygame.quit()

def draw_options_window(options_window, options_title, beadset1_button, beadset2_button):
    """
    Function for drawing the options window
    :param options_window: The options window
    :param options_title: The title of the window
    :param beadset1_button: Button for beadset 1
    :param beadset2_button: Button for beadset 2
    :return: None
    """
    options_window.blit(BACKGROUND_IMG, (0, 0))
    options_window.blit(BOARD_IMG,
                        (SCR_WIDTH // 2 - BOARD_IMG.get_width() // 2, SCR_HEIGHT // 2 - BOARD_IMG.get_height() // 2))
    options_window.blit(options_title, (SCR_WIDTH // 2 - options_title.get_width() // 2,
                                        SCR_HEIGHT // 2 - options_title.get_height() // 2))
    beadset1_button.draw()
    beadset2_button.draw()

    pygame.display.flip()

def options():
    """
    Options window to choose a wanted beadset
    :return: None
    """
    options_window = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
    pygame.display.set_caption("Mancala")

    options_title = get_font("Times new roman", 40).render("Bead Options", 1, BLACK)

    beadset1_button = Button(options_window, "Bead set #1", 50, 400, WHITE)
    beadset2_button = Button(options_window, "Bead set #2", 50, 450, WHITE)

    running = True

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
            # AI vs player game
            if beadset1_button.is_clicked(mouse_pos):
                set_bead_list(1)
                break

            # Player vs Player game
            if beadset2_button.is_clicked(mouse_pos):
                set_bead_list(2)
                break

        draw_options_window(options_window, options_title, beadset1_button, beadset2_button)

def ai_vs_player_game():
    """
    Function for AI vs Player game
    :return: None
    """
    # Game Variables
    game = Game("Player1", "AI Player")
    computer = AIPlayer(game.board, 6, False)

    # Game Loop
    while game.running:

        # Get keyboard state
        keys = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        game.draw()
        game.mid_move = False

        game.poll_events(keys)

        # Human turn
        if game.turn:
            # Check if mouse clicked
            if pygame.mouse.get_pressed(3)[0]:
                # Turn logic
                for move, pit in game.turn_pits.items():
                    # Check if pit is clicked
                    if pit.collided(mouse_pos) and pit.num_of_beads != 0:
                        # Spread the beads
                        # another_turn = check_another_turn(num, pit)
                        game.make_move(move)

        # AI turn
        else:
            move = str(computer.choose_best_move())
            print(move)

            game.make_move(move)

        # Check if there is a winner
        if game.winner is not None:
            print(f"The winner is... {game.winner}!")
            pygame.time.wait(5000)
            break

        # limits FPS to 60
        game.clock.tick(60)

def ai_vs_ai_game():
    """
    Function for AI vs AI game
    :return: None
    """
    # Game Variables
    # Set AI mode to True to skip waiting for moves
    game = Game("AI Player 1", "AI Player 2", True)
    ai_player1 = AIPlayer(game.board, 11, True)
    ai_player2 = AIPlayer(game.board, 11, False)
    print(game.turn)

    # Game Loop
    while game.running:

        # Get keyboard state
        keys = pygame.key.get_pressed()

        game.draw()
        game.mid_move = False

        game.poll_events(keys)

        # AI 1 turn
        if game.turn:
            move = str(ai_player1.choose_best_move())
            print(move)

            game.make_move(move)

        # AI 2 turn
        else:
            move = str(ai_player2.choose_best_move())
            print(move)

            game.make_move(move)

        # Check if there is a winner
        if game.winner is not None:
            winner_text = arial30.render(game.winner + " won!", 1, BLACK)
            game.screen.blit(winner_text, (SCR_WIDTH // 2 - winner_text.get_width() // 2,
                                           SCR_HEIGHT // 2 - winner_text.get_height() // 2))
            pygame.display.flip()

            pygame.time.wait(5000)
            break

        # limits FPS to 60
        game.clock.tick(60)

def one_vs_one():
    """
    Function for Player vs Player game
    :return: None
    """
    # screen Setup
    game = Game("Player1", "Player2")

    # Game Loop
    while game.running:
        # Get keyboard state
        keys = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        game.draw()
        game.mid_move = False

        game.poll_events(keys)

        # Check if mouse clicked
        if pygame.mouse.get_pressed(3)[0]:

            # Turn logic
            for move, pit in game.turn_pits.items():
                # Check if pit is clicked
                if pit.collided(mouse_pos) and pit.num_of_beads != 0:
                    game.make_move(move)

        # Check if there is a winner
        if game.winner is not None:
            game.screen.blit(arial30.render(game.winner + " won!", 1, BLACK), (SCR_WIDTH // 2, SCR_HEIGHT // 2))
            pygame.time.wait(5000)
            break

        # limits FPS to 60
        game.clock.tick(60)


if __name__ == '__main__':
    main()
