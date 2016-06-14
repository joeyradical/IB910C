import pygame
from pygame.locals import *
import sys



def main():
	src = "app_data/"
	game_running = False
	start_screen_running = True
	pygame.init()
	
	#Initialize constants
	BLINKEVENT = USEREVENT + 1
	INPUT_BOX = (140,300,180,20)
	RULES_BOX_X = 480
	RULES_BOX_Y = 230
	RULES_BOX = (RULES_BOX_X, RULES_BOX_Y, 250, 300)
	COLOR_WHITE = (0xFF, 0xFF, 0xFF)
	COLOR_BLACK = (0x00, 0x00, 0x00)
	ROCK_ICON_TILE = (8,13, 67, 67)
	PAPER_ICON_TILE = (84, 13, 67, 67)
	SCISSORS_ICON_TILE = (160, 13, 67, 67)
	
	#Initialize start screen
	disp = pygame.display.set_mode((800,600),False,False)
	pygame.display.set_caption("rock, papers, and scissors")
	startbg = pygame.Surface((800,600))
	startbg.fill((0,0,0))
	startbg.convert()
	disp.blit(startbg, (0,0))
	
	#Initialize title
	f = open(src + "info/intro.txt")
	intro_text = f.read()
	f.close()
	intro_text_font = pygame.font.Font(None, 20)
	intro_text_image = intro_text_font.render(intro_text, True, COLOR_WHITE)
	disp.blit(intro_text_image,(100,100))
	
	#Initialize rules:
	tiles = pygame.image.load(src + "images/ssp_trans.png", )
	rules_text_font = pygame.font.Font(None, 40)
	rules_text = rules_text_font.render("rules: ", True, COLOR_WHITE)
	disp.blit(rules_text,(RULES_BOX_X + 20, RULES_BOX_Y + 20))
	pygame.draw.rect(disp, COLOR_WHITE, RULES_BOX, 1)
	beats_text_font = pygame.font.Font(None, 25)
	beats_text = beats_text_font.render("beats", True, COLOR_WHITE)
	
	#Put out icons and the "beats" labels
	#Row 1
	disp.blit(tiles, (RULES_BOX_X + 20,RULES_BOX_Y + 50),ROCK_ICON_TILE)
	disp.blit(beats_text, (RULES_BOX_X + 100, RULES_BOX_Y + 70))
	disp.blit(tiles, (RULES_BOX_X + 160, RULES_BOX_Y + 50), SCISSORS_ICON_TILE)
	#Row 2
	disp.blit(tiles, (RULES_BOX_X + 20, RULES_BOX_Y + 130), PAPER_ICON_TILE)
	disp.blit(beats_text, (RULES_BOX_X + 100, RULES_BOX_Y + 150))
	disp.blit(tiles, (RULES_BOX_X + 160, RULES_BOX_Y + 130), ROCK_ICON_TILE)
	#Row 2
	disp.blit(tiles, (RULES_BOX_X + 20, RULES_BOX_Y + 210), SCISSORS_ICON_TILE)
	disp.blit(beats_text, (RULES_BOX_X + 100, RULES_BOX_Y + 230))
	disp.blit(tiles, (RULES_BOX_X + 160, RULES_BOX_Y + 210), PAPER_ICON_TILE)
	
		
	
	#Initialize input field
	input_string = "name: "
	input_string_user = ""
	underscore = False
	input_text_font = pygame.font.Font(None,18)
	input_text_image = input_text_font.render(input_string, True, COLOR_WHITE)
	disp.blit(input_text_image,(141, 304))
	pygame.draw.rect(disp, COLOR_WHITE, INPUT_BOX, 1)
	
	
	pygame.display.flip()
	clk = pygame.time.Clock()
	pygame.time.set_timer(BLINKEVENT, 500)
	
	#Start screen
	while start_screen_running:
	
		#Iterate through event queue
		for e in pygame.event.get():
				if e.type == QUIT:
					start_screen_running = False
					
				#Blink underscore sign after input string
				elif e.type == BLINKEVENT:
					pygame.draw.rect(disp, (0x00, 0x00,0x00), INPUT_BOX, 30)
					pygame.draw.rect(disp, (0xFF, 0xFF,0xFF), INPUT_BOX, 1)
					if underscore:
						input_text_image = input_text_font.render((input_string+input_string_user).replace("_",""), True, COLOR_WHITE)
						disp.blit(input_text_image,(141, 304))
						underscore = False
					else:
						input_text_image = input_text_font.render(input_string+input_string_user + "_", True, COLOR_WHITE)
						disp.blit(input_text_image,(141, 304))
						underscore = True
						
				#User input
				elif e.type == KEYDOWN:
					pygame.draw.rect(disp, COLOR_BLACK, INPUT_BOX, 30)
					pygame.draw.rect(disp, COLOR_WHITE, INPUT_BOX, 1)
					if e.key == K_ESCAPE:
						start_screen_running = False
					elif ((e.key > 96 and e.key < 123)) and len(input_string_user) < 20:
						input_string_user += str(unichr(e.key))
					elif e.key == K_SPACE:
						input_string_user = input_string_user + " "
					elif e.key == K_BACKSPACE:
						input_string_user = input_string_user[:-1]
					elif e.key == K_RETURN:
						start_screen_running = False
						game_running = True
						
					#Update input field
					input_text_image = input_text_font.render(input_string + input_string_user, True, COLOR_WHITE)
					disp.blit(input_text_image,(141, 304))
					
		pygame.display.flip()
		clk.tick(30)
	
	#Initialize game session
	disp.fill(COLOR_BLACK)
	pygame.display.flip()
	
	#Game loop
	while game_running:
		#Iterate through event queue
		for e in pygame.event.get():
			if e.type == QUIT:
				game_running = False
			elif e.type == KEYDOWN:
				if e.key == K_ESCAPE:
					game_running = False
		clk.tick(30)
	pygame.quit()
	return 1
if __name__ == "__main__":
	status = main()
	sys.exit(status)
	