import os.path
import pygame

pygame.font.init()

# Board
BOARD_IMG = pygame.image.load(os.path.join('assets', 'Board.png'))
BOARD_IMG = pygame.transform.scale_by(BOARD_IMG, 0.75)

# Beads
INITIAL_BEAD_NUM = 6
BEAD_RADIUS = 7
BEAD_DIAMETER = 2 * BEAD_RADIUS
RED_BEAD_IMG = pygame.transform.scale_by(pygame.image.load(os.path.join('assets', 'RED_BEAD.png')), 0.25)
LIGHT_BLUE_BEAD_IMG = pygame.transform.scale_by(pygame.image.load(os.path.join('assets', 'LIGHT_BLUE_BEAD.png')), 0.25)
BLUE_BEAD_IMG = pygame.transform.scale_by(pygame.image.load(os.path.join('assets', 'BLUE_BEAD.png')), 0.25)
YELLOW_BEAD_IMG = pygame.transform.scale_by(pygame.image.load(os.path.join('assets', 'YELLOW_BEAD.png')), 0.25)
GREEN_BEAD_IMG = pygame.transform.scale_by(pygame.image.load(os.path.join('assets', 'GREEN_BEAD.png')), 0.25)
BEAD_IMAGE_LIST = [RED_BEAD_IMG, GREEN_BEAD_IMG, BLUE_BEAD_IMG, LIGHT_BLUE_BEAD_IMG, YELLOW_BEAD_IMG]


# Pits
PIT_RADIUS = 40
UP_PIT_BUFFER = 260
LOW_PIT_BUFFER = 760
PIT_BUFFER = 185
UP_PIT_DIC = {"1": (70, 225), "2": (70, 135), "3": (70, 50), "4": (180, 50), "5": (180, 135), "6": (180, 225)}
LOW_PIT_DIC = {"1": (180, 550), "2": (180, 635), "3": (180, 720), "4": (70, 720), "5": (70, 635), "6": (70, 550)}

# Stores
STORE_WIDTH = 200
STORE_HEIGHT = 60
STORE_BUFFER = 20
UP_STORE_BUFFER = 280
DOWN_STORE_BUFFER = 430

# Screen
SCR_WIDTH, SCR_HEIGHT = BOARD_IMG.get_width(), BOARD_IMG.get_height()

# Fonts
default_font = pygame.font.Font(None, 30)

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

