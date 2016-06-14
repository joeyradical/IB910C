import pygame
from pygame.locals import *
import sys
from startscreen import StartScreen
from gamescreen import GameScreen

def main():
	pygame.init()
	disp = pygame.display.set_mode((800,600),False,False)
	pygame.display.set_caption("rock, papers, and scissors")
	clk = pygame.time.Clock()
	startScreen = StartScreen(disp,clk)
	escape = startScreen.run()
	if escape == False:
		gameScreen = GameScreen(disp,clk)
		gameScreen.run()
	pygame.quit()
	return 1
if __name__ == "__main__":
	status = main()
	sys.exit(status)
	