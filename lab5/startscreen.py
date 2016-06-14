import pygame
from pygame.locals import *
from constants import * 

class StartScreen:
	def __init__(self,disp,clk):
		self.disp = disp
		self.init_GUI()
		self.clk = clk
		
	def init_GUI(self):
		src = "app_data/"
		#Initialize constants
		self.BLINKEVENT = USEREVENT + 1
		self.INPUT_BOX = (140,300,180,20)
		RULES_BOX_X = 480
		RULES_BOX_Y = 230
		RULES_BOX = (RULES_BOX_X, RULES_BOX_Y, 250, 300)
	
		#Initialize start screen
		
		startbg = pygame.Surface((800,600))
		startbg.fill((0,0,0))
		startbg.convert()
		self.disp.blit(startbg, (0,0))
	
		#Initialize title
		f = open(src + "info/intro.txt")
		intro_text = f.read()
		f.close()
		intro_text_font = pygame.font.Font(None, 20)
		intro_text_image = intro_text_font.render(intro_text, True, COLOR_WHITE)
		self.disp.blit(intro_text_image,(100,100))
	
		#Initialize rules:
		tiles = pygame.image.load(src + "images/ssp_trans.png", )
		rules_text_font = pygame.font.Font(None, 40)
		rules_text = rules_text_font.render("rules: ", True, COLOR_WHITE)
		self.disp.blit(rules_text,(RULES_BOX_X + 20, RULES_BOX_Y + 20))
		pygame.draw.rect(self.disp, COLOR_WHITE, RULES_BOX, 1)
		beats_text_font = pygame.font.Font(None, 25)
		beats_text = beats_text_font.render("beats", True, COLOR_WHITE)
	
		#Put out icons and the "beats" labels
		#Row 1
		self.disp.blit(tiles, (RULES_BOX_X + 20,RULES_BOX_Y + 50),ROCK_ICON_TILE)
		self.disp.blit(beats_text, (RULES_BOX_X + 100, RULES_BOX_Y + 70))
		self.disp.blit(tiles, (RULES_BOX_X + 160, RULES_BOX_Y + 50), SCISSORS_ICON_TILE)
		#Row 2
		self.disp.blit(tiles, (RULES_BOX_X + 20, RULES_BOX_Y + 130), PAPER_ICON_TILE)
		self.disp.blit(beats_text, (RULES_BOX_X + 100, RULES_BOX_Y + 150))
		self.disp.blit(tiles, (RULES_BOX_X + 160, RULES_BOX_Y + 130), ROCK_ICON_TILE)
		#Row 2
		self.disp.blit(tiles, (RULES_BOX_X + 20, RULES_BOX_Y + 210), SCISSORS_ICON_TILE)
		self.disp.blit(beats_text, (RULES_BOX_X + 100, RULES_BOX_Y + 230))
		self.disp.blit(tiles, (RULES_BOX_X + 160, RULES_BOX_Y + 210), PAPER_ICON_TILE)
	
		#Initialize input field
		self.input_string = "name: "
		self.input_text_font = pygame.font.Font(None,18)
		input_text_image = self.input_text_font.render(self.input_string, True, COLOR_WHITE)
		self.disp.blit(input_text_image,(141, 304))
		pygame.draw.rect(self.disp, COLOR_WHITE, self.INPUT_BOX, 1)
	
		pygame.display.flip()
		pygame.time.set_timer(self.BLINKEVENT, 500)
	def run(self):
		#Start screen
		running = True
		escape = False
		underscore = False
		input_string_user = ""
		input_string = self.input_string
		
		while running:
			#Iterate through event queue
			for e in pygame.event.get():
					if e.type == QUIT:
						running = False
						escape = True
					
					#Blink underscore sign after input string
					elif e.type == self.BLINKEVENT:
						pygame.draw.rect(self.disp, (0x00, 0x00,0x00), self.INPUT_BOX, 30)
						pygame.draw.rect(self.disp, (0xFF, 0xFF,0xFF), self.INPUT_BOX, 1)
						if underscore:
							input_text_image = self.input_text_font.render((input_string+input_string_user).replace("_",""), True, COLOR_WHITE)
							self.disp.blit(input_text_image,(141, 304))
							underscore = False
						else:
							input_text_image = self.input_text_font.render(input_string+input_string_user + "_", True, COLOR_WHITE)
							self.disp.blit(input_text_image,(141, 304))
							underscore = True
						
					#User input
					elif e.type == KEYDOWN:
						pygame.draw.rect(self.disp, COLOR_BLACK, self.INPUT_BOX, 30)
						pygame.draw.rect(self.disp, COLOR_WHITE, self.INPUT_BOX, 1)
						if e.key == K_ESCAPE:
							running = False
							escape = True
						elif ((e.key > 96 and e.key < 123)) and len(input_string_user) < 20:
							input_string_user += str(unichr(e.key))
						elif e.key == K_SPACE:
							input_string_user = input_string_user + " "
						elif e.key == K_BACKSPACE:
							input_string_user = input_string_user[:-1]
						elif e.key == K_RETURN:
							running = False
									
						#Update input field
						input_text_image = self.input_text_font.render(input_string + input_string_user, True, COLOR_WHITE)
						self.disp.blit(input_text_image,(141, 304))
					
			pygame.display.flip()
			self.clk.tick(30)
		return escape