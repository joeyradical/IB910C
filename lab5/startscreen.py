import pygame
from constants import *
import startscreengraphics

""""The class Startscreen is a class which contains the entire start screen for the game.
This screen features an introductory text (obtained from "appdata/info/introduction.txt",
a rules window, and an input field where the player inputs his or her name,
meaning that these graphical objects (whose class definitions can be found in startscreengraphics.py) are included
as attributes to the StartScreen class. The class has several init functions, and a run functions which contains
a loop which processes events and draws graphical objects on the screen at a 30 fps frame rate"""


class StartScreen:
	def __init__(self, disp, clk, tiles):
		self.disp = disp
		self.clk = clk
		self.tiles = tiles
		self.fonts = {}
		self.init_fonts()
		self.ruleswindow = startscreengraphics.RulesWindow(self.tiles, self.fonts)
		self.inputfield = startscreengraphics.InputField(self.fonts)
		self.sounds = {}

	def init_fonts(self):
		# Initialize fonts
		self.fonts = {
			"tiny": pygame.font.Font(None, 18),
			"small": pygame.font.Font(None, 20),
			"medium": pygame.font.Font(None, 25),
			"large": pygame.font.Font(None, 40)
						}

	def init_sounds(self):
		self.sounds = {"keyboard": pygame.mixer.Sound(src + "sounds/keyboard.wav")}

	def init(self):
		# Initialize start screen
		self.init_sounds()

		startbg = pygame.Surface((800, 600))
		startbg.fill(COLOR_BLACK)
		self.disp.blit(startbg, (0, 0))

		# Initialize introduction text
		f = open(src + "info/intro.txt")
		intro_text = f.read()
		f.close()

		intro_text_image = self.fonts['small'].render(intro_text, True, COLOR_WHITE)
		self.disp.blit(intro_text_image, (100, 100))

		# Draw rules window
		self.ruleswindow.draw(self.disp)

		# Initialize input field
		self.inputfield.draw(self.disp)
	
		pygame.display.flip()
		pygame.time.set_timer(BLINKEVENT, 500)

	def run(self):
		# Start screen
		self.init()
		running = True
		escape = False
		user_string = ""
		
		while running:
			# Iterate through event queue
			for e in pygame.event.get():
					if e.type == QUIT:
						running = False
						escape = True
					
					# Blink underscore sign after input string
					elif e.type == BLINKEVENT:
						self.inputfield.blink(self.disp, user_string)
					# User input
					elif e.type == KEYDOWN:
						self.sounds['keyboard'].play()
						self.inputfield.clear(self.disp)
						if e.key == K_ESCAPE:
							running = False
							escape = True
						elif (96 < e.key < 123) and len(user_string) < 10:
							user_string += str(unichr(e.key))
						elif e.key == K_SPACE:
							user_string += " "
						elif e.key == K_BACKSPACE:
							user_string = user_string[:-1]
						elif e.key == K_RETURN:
							running = False
									
						# Update input field
						self.inputfield.update(self.disp, user_string)

			pygame.display.flip()
			self.clk.tick(30)
		# Return player name and escape code
		return [escape, user_string]
