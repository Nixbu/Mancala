import os.path
import pygame

pygame.font.init()

# Board
BOARD_IMG = pygame.image.load(os.path.join('assets', 'Game Assets', 'Board.png'))
BOARD_IMG = pygame.transform.scale_by(BOARD_IMG, 0.75)

# Screen
SCR_WIDTH, SCR_HEIGHT = 800, BOARD_IMG.get_height()

# Backgrounds
BACKGROUND_IMG = pygame.image.load(os.path.join('assets', 'Carpets', 'CarpetBackground6.png'))
BACKGROUND_IMG = pygame.transform.scale(BACKGROUND_IMG, (SCR_WIDTH, SCR_HEIGHT))

# Beads
INITIAL_BEAD_NUM = 6
BEAD_RADIUS = 7
BEAD_DIAMETER = 2 * BEAD_RADIUS
RED_BEAD_IMG = pygame.transform.scale_by(pygame.image.load(os.path.join('assets', 'Game Assets', 'RED_BEAD.png')), 0.25)
LIGHT_BLUE_BEAD_IMG = pygame.transform.scale_by(pygame.image.load(os.path.join('assets', 'Game Assets',  'LIGHT_BLUE_BEAD.png')), 0.25)
BLUE_BEAD_IMG = pygame.transform.scale_by(pygame.image.load(os.path.join('assets', 'Game Assets',  'BLUE_BEAD.png')), 0.25)
YELLOW_BEAD_IMG = pygame.transform.scale_by(pygame.image.load(os.path.join('assets', 'Game Assets',  'YELLOW_BEAD.png')), 0.25)
GREEN_BEAD_IMG = pygame.transform.scale_by(pygame.image.load(os.path.join('assets', 'Game Assets',  'GREEN_BEAD.png')), 0.25)
BEAD_IMAGE_LIST = [RED_BEAD_IMG, GREEN_BEAD_IMG, BLUE_BEAD_IMG, LIGHT_BLUE_BEAD_IMG, YELLOW_BEAD_IMG]


# Pits
PIT_RADIUS = 40
UP_PIT_BUFFER = 260
LOW_PIT_BUFFER = 760
PIT_BUFFER = 185
UP_PIT_DIC = {"1": (335, 235), "2": (335, 145), "3": (335, 60), "4": (445, 60), "5": (445, 145), "6": (445, 235)}
LOW_PIT_DIC = {"1": (445, 560), "2": (445, 645), "3": (445, 730), "4": (335, 730), "5": (335, 645), "6": (335, 560)}

# Stores
STORE_WIDTH = 200
STORE_HEIGHT = 60
STORE_BUFFER = 275
UP_STORE_BUFFER = 285
DOWN_STORE_BUFFER = 430

# Fonts
default_font = pygame.font.Font(None, 30)

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

