import pygame
from constants import *
import sys
from startscreen import StartScreen
from gamescreen import GameScreen

"""This is the main program. It initializes pygame and creates instances of both the GameScreen and StartScreen classes.
These are run in a loop, which is controlled by return values of the run() methods of each class"""


def main():
	try:
		pygame.init()
		disp = pygame.display.set_mode((800, 600), False, False)
		pygame.display.set_caption("rock, paper, and scissors")
	except pygame.error:
		print "Pygame failed to initialize"

	try:
		tiles = pygame.image.load(src + "images/ssp_trans.png")
	except pygame.error:
		print "Failed to read game data"
	clk = pygame.time.Clock()
	exit_game = False
	startscreen = StartScreen(disp, clk, tiles)
	gamescreen = GameScreen(disp, clk, tiles)
	while not exit_game:
		ret = startscreen.run()
		exit_game = ret[0]
		if exit_game:
			break

		exit_game = gamescreen.run(ret[1])
	pygame.quit()
	return 1
if __name__ == "__main__":
	status = main()
	sys.exit(status)
