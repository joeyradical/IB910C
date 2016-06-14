import pygame
from pygame.locals import *
from constants import *

class GameScreen:
	def __init__(self, disp, clk):
		self.disp = disp
		self.clk = clk
		self.init_GUI()
		
	def init_GUI(self):
		self.disp.fill(COLOR_BLACK)
		pygame.display.flip()
		
	def run(self):
		#Game loop
		game_running = True
		while game_running:
			#Iterate through event queue
			for e in pygame.event.get():
				if e.type == QUIT:
					game_running = False
				elif e.type == KEYDOWN:
					if e.key == K_ESCAPE:
						game_running = False
			self.clk.tick(30)
		
