import pygame
from constants import *
""""This file contains class definitions for all graphical objects used in the startscreen
RulesWindow is the window which shows the player which move beats another.
InputField is the field where the player inputs his or her name.
Each class has an init function which do all the rendering.
They also have a draw function which draws the graphical object on the screen"""


class RulesWindow:
	def __init__(self, tiles, fonts):
		self.fonts = fonts
		self.tiles = tiles
		self.rules_title = None
		self.beats_label = None
		self.init()

	def init(self):
		self.rules_title = self.fonts['large'].render("rules: ", True, COLOR_WHITE)
		self.beats_label = self.fonts['medium'].render("beats", True, COLOR_WHITE)

	def draw(self, disp):
		pygame.draw.rect(disp, COLOR_WHITE, RULES_BOX, 1)
		disp.blit(self.rules_title, (RULES_BOX_X + 20, RULES_BOX_Y + 20))
		# Put out icons and the "beats" labels

		# Row 1
		disp.blit(self.tiles, (RULES_BOX_X + 20, RULES_BOX_Y + 50), ROCK_ICON_TILE)
		disp.blit(self.beats_label, (RULES_BOX_X + 100, RULES_BOX_Y + 70))
		disp.blit(self.tiles, (RULES_BOX_X + 160, RULES_BOX_Y + 50), SCISSORS_ICON_TILE)
		# Row 2
		disp.blit(self.tiles, (RULES_BOX_X + 20, RULES_BOX_Y + 130), PAPER_ICON_TILE)
		disp.blit(self.beats_label, (RULES_BOX_X + 100, RULES_BOX_Y + 150))
		disp.blit(self.tiles, (RULES_BOX_X + 160, RULES_BOX_Y + 130), ROCK_ICON_TILE)
		# Row 3
		disp.blit(self.tiles, (RULES_BOX_X + 20, RULES_BOX_Y + 210), SCISSORS_ICON_TILE)
		disp.blit(self.beats_label, (RULES_BOX_X + 100, RULES_BOX_Y + 230))
		disp.blit(self.tiles, (RULES_BOX_X + 160, RULES_BOX_Y + 210), PAPER_ICON_TILE)


class InputField:
	def __init__(self, fonts):
		self.fonts = fonts
		self.underscore = False
		self.input_string = ''
		self.input_text = None
		self.init()

	def init(self):
		self.input_string = "name: "
		self.input_text = self.fonts['tiny'].render(self.input_string, True, COLOR_WHITE)
		self.underscore = False

	def draw(self, disp):
		pygame.draw.rect(disp, COLOR_WHITE, INPUT_BOX, 1)
		disp.blit(self.input_text, (141, 304))

	def blink(self, disp, user_string):
		# Blink underscore sign
		self.clear(disp)
		if self.underscore:
			input_text_image = self.fonts['tiny'].render((self.input_string + user_string).replace("_", ""), True,
														COLOR_WHITE)
			disp.blit(input_text_image, (141, 304))
			self.underscore = False
		else:
			input_text_image = self.fonts['tiny'].render(self.input_string + user_string + "_", True, COLOR_WHITE)
			disp.blit(input_text_image, (141, 304))
			self.underscore = True

	@staticmethod
	def clear(disp):
		# Clear inputfield
		pygame.draw.rect(disp, (0x00, 0x00, 0x00), INPUT_BOX, 30)
		pygame.draw.rect(disp, (0xFF, 0xFF, 0xFF), INPUT_BOX, 1)

	def update(self, disp, user_string):
		# Update text in inputfield
		input_text = self.fonts['tiny'].render(self.input_string + user_string, True, COLOR_WHITE)
		disp.blit(input_text, (141, 304))
