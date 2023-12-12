import pygame

from utils import *

def draw_main_screen(main_window, main_title, ai_option, one_vs_one_option):
    main_window.blit(BACKGROUND_IMG, (0, 0))
    main_window.blit(BOARD_IMG, (SCR_WIDTH // 2 - BOARD_IMG.get_width() // 2, SCR_HEIGHT // 2 - BOARD_IMG.get_height() // 2))
    main_window.blit(main_title, (SCR_WIDTH // 2 - main_title.get_width() // 2,
                                  SCR_HEIGHT // 2 - main_title.get_height() // 2))
    ai_option.draw()
    one_vs_one_option.draw()
    pygame.display.flip()

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

def ai_game():
    # Game Variables
    game = Game("Player1", "AI Player")
    computer = AIPlayer(game.board, 11)

    # Game Loop
    while game.running:

        # Get keyboard state
        keys = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        game.draw()

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
                        game.print_game_state()

        # AI turn
        else:
            move = str(computer.choose_best_move())
            print(move)

            game.make_move(move)
            game.print_game_state()

        # Check if there is a winner
        if game.winner is not None:
            print(f"The winner is... {game.winner}!")
            pygame.time.wait(5000)
            break

        # limits FPS to 60
        game.clock.tick(60)

    pygame.quit()


def one_vs_one():
    # screen Setup
    game = Game("Player1", "Player2")

    # Game Loop
    while game.running:
        # Get keyboard state
        keys = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        game.draw()

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
            print(f"The winner is... {game.winner}!")
            pygame.time.wait(5000)
            break

        # limits FPS to 60
        game.clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
