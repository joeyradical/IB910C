from pygame.locals import * 
"""This file contains constant values which are used by both the gamescreen and the startscreen. These constants
are mostly positions and dimensions of the graphical objects, color hexcodes, and the speed of the animation."""

# Search path for files
src = "app_data/"

# Color hexcodes
COLOR_WHITE = (0xFF, 0xFF, 0xFF)
COLOR_BLACK = (0x00, 0x00, 0x00)
COLOR_GREEN = (0x00, 0xFF, 0x00)
COLOR_RED = (0xFF, 0x00, 0x00)

# Dimensions used to obtain icons from the tiles image file
ROCK_ICON_TILE = (8, 13, 67, 67)
PAPER_ICON_TILE = (84, 13, 67, 67)
SCISSORS_ICON_TILE = (160, 13, 67, 67)
QUESTION_MARK_TILE = (236, 1, 152, 238)


# User-defined events
BLINKEVENT = USEREVENT + 1
TIMEOUT_EVENT = USEREVENT + 2

# Dimensions and positions for graphical objects on the startscreen
INPUT_BOX = (140, 300, 130, 20)
RULES_BOX_X = 480
RULES_BOX_Y = 230
RULES_BOX = (RULES_BOX_X, RULES_BOX_Y, 250, 300)

# Dimensions and position for grapgical objects on the gamescreen

SCORE_BOX_X = 50
SCORE_BOX_Y = 50
SCORE_BOX_HEIGHT = 120
SCORE_BOX_WIDTH = 400
SCORE_BOX = (SCORE_BOX_X, SCORE_BOX_Y, SCORE_BOX_WIDTH, SCORE_BOX_HEIGHT)

INSTRUCTIONS_BOX_X = 50
INSTRUCTIONS_BOX_Y = 470
INSTRUCTIONS_BOX = (INSTRUCTIONS_BOX_X, INSTRUCTIONS_BOX_Y, 400, 130)

MOVE_DIM = 67
MOVES_BOX_X = 50
MOVES_BOX_Y = 230
MOVES_BOX = (MOVES_BOX_X, MOVES_BOX_Y, 300, 150)
MOVES_BOX_ROCK_X = MOVES_BOX_X + 20
MOVES_BOX_ROCK_Y = MOVES_BOX_Y + 50
MOVES_BOX_ROCK = (MOVES_BOX_ROCK_X, MOVES_BOX_ROCK_Y, MOVE_DIM, MOVE_DIM)
MOVES_BOX_PAPER_X = MOVES_BOX_X + 107
MOVES_BOX_PAPER_Y = MOVES_BOX_Y + 50
MOVES_BOX_PAPER = (MOVES_BOX_PAPER_X, MOVES_BOX_PAPER_Y, MOVE_DIM, MOVE_DIM)
MOVES_BOX_SCISSORS_X = MOVES_BOX_X + 194
MOVES_BOX_SCISSORS_Y = MOVES_BOX_Y + 50
MOVES_BOX_SCISSORS = (MOVES_BOX_SCISSORS_X, MOVES_BOX_SCISSORS_Y, MOVE_DIM, MOVE_DIM)

OPPONENT_BOX_X = 550
OPPONENT_BOX_Y = 170
OPPONENT_BOX = (OPPONENT_BOX_X, OPPONENT_BOX_Y, 200, 300)

# Constants for animation
ABS_VELOCITY = 32
