from constants import *
import pygame

""""This file contains class definitions for all graphical objects used in the gamescreen
ScoreBox is a table which keeps track of the score.
MovesBox is a box which will later contain the dragable "move" icons (r/p/s)
OpponentBox is a box which shows the move of the computer (initially just displaying a question mark)
InstructionsBox is a box which contains instructions on how to play the game.
Each class has an init function which do all the rendering.
They also have a draw function which draws the graphical object on the screen"""


class ScoreBox:

	def __init__(self, fonts, scores):
		#  Declare class attributes
		self.fonts = fonts
		self.player_name = ""
		self.scores = scores
		self.player_score_title = None
		self.heat_score_title = None
		self.total_score_title = None
		self.player_title = None
		self.computer_name_text = None
		self.player_name_text = None
		# Initialize class attributes
		self.init()

	def init(self):
		self.player_title = self.fonts['medium'].render("player", True, COLOR_WHITE)
		self.heat_score_title = self.fonts['medium'].render("heat score", True, COLOR_WHITE)
		self.total_score_title = self.fonts['medium'].render("total score", True, COLOR_WHITE)
		self.player_name_text = self.fonts['small'].render(self.player_name, True, COLOR_WHITE)
		self.computer_name_text = self.fonts['small'].render("computer", True, COLOR_WHITE)

	def draw(self, disp):
		# Draw score box rectangle and lines
		pygame.draw.rect(disp, COLOR_WHITE, SCORE_BOX, 1)
		pygame.draw.line(disp, COLOR_WHITE, (SCORE_BOX_X + 90, SCORE_BOX_Y),
						(SCORE_BOX_X + 90, SCORE_BOX_Y + SCORE_BOX_HEIGHT))
		pygame.draw.line(disp, COLOR_WHITE, (SCORE_BOX_X + 230, SCORE_BOX_Y),
						(SCORE_BOX_X + 230, SCORE_BOX_Y + SCORE_BOX_HEIGHT))
		pygame.draw.line(disp, COLOR_WHITE, (SCORE_BOX_X, SCORE_BOX_Y + SCORE_BOX_HEIGHT * 2 / 3),
						(SCORE_BOX_X + SCORE_BOX_WIDTH, SCORE_BOX_Y + SCORE_BOX_HEIGHT * 2 / 3))
		pygame.draw.line(disp, COLOR_WHITE, (SCORE_BOX_X, SCORE_BOX_Y + SCORE_BOX_HEIGHT * 1 / 3),
						(SCORE_BOX_X + SCORE_BOX_WIDTH, SCORE_BOX_Y + SCORE_BOX_HEIGHT * 1 / 3))

		# Draw titles
		disp.blit(self.player_title, (SCORE_BOX_X + 20, SCORE_BOX_Y + 10))
		disp.blit(self.heat_score_title, (SCORE_BOX_X + 100, SCORE_BOX_Y + 10))
		disp.blit(self.total_score_title, (SCORE_BOX_X + 240, SCORE_BOX_Y + 10))
		disp.blit(self.player_name_text, (SCORE_BOX_X + 10, SCORE_BOX_Y + SCORE_BOX_HEIGHT / 3 +
						SCORE_BOX_HEIGHT / 12))
		disp.blit(self.computer_name_text, (SCORE_BOX_X + 10, SCORE_BOX_Y + SCORE_BOX_HEIGHT * 2 / 3 +
						SCORE_BOX_HEIGHT / 12))

		# Draw scores
		positions = [
			(SCORE_BOX_X + 110, SCORE_BOX_Y + SCORE_BOX_HEIGHT / 3 + SCORE_BOX_HEIGHT / 12),
			(SCORE_BOX_X + 110, SCORE_BOX_Y + SCORE_BOX_HEIGHT * 2 / 3 + SCORE_BOX_HEIGHT / 12),
			(SCORE_BOX_X + 250, SCORE_BOX_Y + SCORE_BOX_HEIGHT / 3 + SCORE_BOX_HEIGHT / 12),
			(SCORE_BOX_X + 250, SCORE_BOX_Y + SCORE_BOX_HEIGHT * 2 / 3 + SCORE_BOX_HEIGHT / 12)
		]

		for i, score in enumerate(self.scores):
			score_text = self.fonts['medium'].render(str(score), True, COLOR_WHITE)
			disp.blit(score_text, positions[i])

	def set_player_name(self, player_name):
		self.player_name = player_name
		self.player_name_text = self.fonts['small'].render(self.player_name, True, COLOR_WHITE)

	def update(self, scores):
		self.scores = scores


class MovesBox:
	def __init__(self, fonts, moves):
		self.fonts = fonts
		self.moves = moves
		self.moves_title = None
		self.init()

	def init(self):
		self.moves_title = self.fonts['large'].render("moves: ", True, COLOR_WHITE)

	def draw(self, disp):
		# Draw moves box
		pygame.draw.rect(disp, COLOR_WHITE, MOVES_BOX, 1)
		pygame.draw.rect(disp, COLOR_WHITE, MOVES_BOX_ROCK, 1)
		pygame.draw.rect(disp, COLOR_WHITE, MOVES_BOX_PAPER, 1)
		pygame.draw.rect(disp, COLOR_WHITE, MOVES_BOX_SCISSORS, 1)
		# Draw box title
		disp.blit(self.moves_title, (MOVES_BOX_X + 20, MOVES_BOX_Y + 20))


class OpponentBox:
	def __init__(self, fonts):
		self.fonts = fonts
		self.opponent_title = None
		self.init()

	def init(self):
		self.opponent_title = self.fonts['large'].render("opponent: ", True, COLOR_WHITE)

	def draw(self, disp):
		pygame.draw.rect(disp, COLOR_WHITE, OPPONENT_BOX, 1)
		disp.blit(self.opponent_title, (OPPONENT_BOX_X + 20, OPPONENT_BOX_Y + 20))


class InstructionsBox:
	def __init__(self, fonts):
		self.fonts = fonts
		self.instructions_title = None
		self.inst_images = []
		self.init()

	def init(self):
		# Load player instructions from text file
		instructions = []
		try:
			f = open(src + "info/instructions.txt", 'r')
			instructions = f.read().split('%')
			f.close()
		except IOError:
			instructions[0] = "instructions.txt not found"

		# Create surface from text file
		self.instructions_title = self.fonts['large'].render("instructions: ", True, COLOR_WHITE)
		for inst in instructions:
			self.inst_images.append(self.fonts['small'].render(inst, True, COLOR_WHITE))

	def draw(self, disp):
		pygame.draw.rect(disp, COLOR_WHITE, INSTRUCTIONS_BOX, 1)
		disp.blit(self.instructions_title, (INSTRUCTIONS_BOX_X + 20, INSTRUCTIONS_BOX_Y + 20))
		for i, inst in enumerate(self.inst_images):
			disp.blit(inst, (INSTRUCTIONS_BOX_X + 20, INSTRUCTIONS_BOX_Y + 50 + i * 20))
