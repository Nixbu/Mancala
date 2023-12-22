import os.path
import pygame

pygame.font.init()

# Board
BOARD_IMG = pygame.image.load(os.path.join('assets', 'Game Assets', 'Board.png'))
BOARD_IMG = pygame.transform.scale_by(BOARD_IMG, 0.75)

PLAYER1_TURN_BOARD = pygame.image.load(os.path.join('assets', 'Game Assets', 'Player1_turn_board.png'))
PLAYER1_TURN_BOARD = pygame.transform.scale_by(PLAYER1_TURN_BOARD, 0.75)

PLAYER2_TURN_BOARD = pygame.image.load(os.path.join('assets', 'Game Assets', 'Player2_turn_board.png'))
PLAYER2_TURN_BOARD = pygame.transform.scale_by(PLAYER2_TURN_BOARD, 0.75)

# Screen
SCR_WIDTH, SCR_HEIGHT = 800, BOARD_IMG.get_height()

# Backgrounds
BACKGROUND_IMG = pygame.image.load(os.path.join('assets', 'Carpets', 'CarpetBackground6.png'))
BACKGROUND_IMG = pygame.transform.scale(BACKGROUND_IMG, (SCR_WIDTH, SCR_HEIGHT))

# Player names and scores positions
PLAYER1_POS = (550, 700)
P1SCORE_POS = (600, 730)

PLAYER2_POS = (120, 20)
P2SCORE_POS = (150, 50)


# Beads
INITIAL_BEAD_NUM = 6
BEAD_RADIUS = 7
BEAD_DIAMETER = 2 * BEAD_RADIUS


def set_bead(path, file):
    bead_img = pygame.transform.scale(pygame.image.load(os.path.join(path, file)), BEAD_SIZE)
    bead_img.set_alpha(200)

    return bead_img

# First set
FIRST_SET_PATH = os.path.join('assets', 'Game Assets', 'Beads_set1')
RED_BEAD_IMG = pygame.transform.scale_by(pygame.image.load(os.path.join(FIRST_SET_PATH, 'RED_BEAD.png')), 0.25)
LIGHT_BLUE_BEAD_IMG = pygame.transform.scale_by(pygame.image.load(os.path.join(FIRST_SET_PATH,  'LIGHT_BLUE_BEAD.png')), 0.25)
BLUE_BEAD_IMG = pygame.transform.scale_by(pygame.image.load(os.path.join(FIRST_SET_PATH,  'BLUE_BEAD.png')), 0.25)
YELLOW_BEAD_IMG = pygame.transform.scale_by(pygame.image.load(os.path.join(FIRST_SET_PATH,  'YELLOW_BEAD.png')), 0.25)
GREEN_BEAD_IMG = pygame.transform.scale_by(pygame.image.load(os.path.join(FIRST_SET_PATH,  'GREEN_BEAD.png')), 0.25)
BEAD_IMAGE_LIST1 = [RED_BEAD_IMG, GREEN_BEAD_IMG, BLUE_BEAD_IMG, LIGHT_BLUE_BEAD_IMG, YELLOW_BEAD_IMG]

# Second set
SECOND_SET_PATH = os.path.join('assets', 'Game Assets', 'Beads_set2')
BEAD_SIZE = (20, 20)
BEAD1_IMG = set_bead(SECOND_SET_PATH, 'BEAD1.png')
BEAD2_IMG = set_bead(SECOND_SET_PATH, 'BEAD2.png')
BEAD3_IMG = set_bead(SECOND_SET_PATH, 'BEAD3.png')
BEAD_IMAGE_LIST2 = [BEAD1_IMG, BEAD2_IMG, BEAD3_IMG]

# Bead set
BEAD_SETS = [BEAD_IMAGE_LIST1, BEAD_IMAGE_LIST2]
bead_set = BEAD_SETS[1]

def set_bead_list(set_num):
    global bead_set
    bead_set = BEAD_SETS[set_num - 1]

# Pits
PIT_RADIUS = 40
UP_PIT_BUFFER = 260
LOW_PIT_BUFFER = 760
PIT_BUFFER = 185
UP_PIT_DIC = {"1": (335, 235), "2": (335, 145), "3": (335, 60), "4": (445, 60), "5": (445, 145), "6": (445, 235)}
LOW_PIT_DIC = {"1": (445, 560), "2": (445, 645), "3": (445, 730), "4": (335, 730), "5": (335, 645), "6": (335, 560)}
CUP_IMG = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'Game Assets', 'Cup.png')), (100, 100))
CUP_POS = (600, 400)
CUP_IMG_POS = (550, 350)

# Stores
STORE_WIDTH = 200
STORE_HEIGHT = 60
STORE_BUFFER = 275
UP_STORE_BUFFER = 285
DOWN_STORE_BUFFER = 430

# Fonts
default_font = pygame.font.Font(None, 30)
arial30 = pygame.font.SysFont("Arial", 30)

def get_font(font_name, size):
    return pygame.font.SysFont(font_name, size)

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

