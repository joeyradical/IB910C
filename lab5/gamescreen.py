import pygame
import random
from collections import OrderedDict
from constants import *
from move import Move
import gamegraphics
import animation

"""The GameScreen class contains the entire screen for gameplay. It contains a scorebox, a box for the opponent's move,
a box for the player's move, and a box with instructions on how to play the game. These graphical objects are all
defined in the gamegraphics.py source file. It also contains a class instance of battleanimation (found in
animation.py) which controls the animation segment after each round. It features several init functions (as there
are a LOT of attributes that need to be initialized) and the game loop itself is in the run() method. The gameloop
redraws the entire screen at a frame rate of 30 fps, and also captures mouse events at the same rate. """


class GameScreen:

	def __init__(self, disp, clk, tiles):
		# Declaration of all class attributes
		self.disp = disp
		self.clk = clk
		self.tiles = tiles
		self.fonts = None
		# Initialize the fonts dictionary
		self.init_fonts()
		# Order for scores: Player heat, Computer heat, Player tot, Computer, tot
		self.scores = [0, 0, 0, 0]
		self.player_name = ""
		# Initialize the score list
		self.init_scores()
		self.scorebox = gamegraphics.ScoreBox(self.fonts, self.scores)
		self.moves = None
		# Initialize list containing all Move objects
		self.init_moves()
		# Declare graphics objects
		self.movebox = gamegraphics.MovesBox(self.fonts, self.moves)
		self.opponentbox = gamegraphics.OpponentBox(self.fonts)
		self.instructionsbox = gamegraphics.InstructionsBox(self.fonts)
		# Declare game variables
		self.game_running = False
		self.beats = {}
		self.shake_cnt = 0
		self.shake_state = False
		self.chosen_move = ''
		self.sounds = {}
		self.animation_phase = 0
		self.results = []
		self.battleanimation = animation.BattleAnimation(self.fonts)
		self.animation_running = -1
		self.exit_game = False

	def init_fonts(self):
		# Initialize all fonts
		self.fonts = {
			"x-large": pygame.font.Font(None, 100),
			"large": pygame.font.Font(None, 30),
			"medium": pygame.font.Font(None, 25),
			"small": pygame.font.Font(None, 20),
		}

	# Sets the scores list to 0
	def init_scores(self):
		for i in range(0, 4):
			self.scores[i] = 0

	# Creates a dictionary with all the move objects
	def init_moves(self):
		self.moves = OrderedDict()
		self.moves['r'] = Move(self.tiles.subsurface(ROCK_ICON_TILE), 'r',
					(MOVES_BOX_ROCK_X, MOVES_BOX_ROCK_Y), False)
		self.moves['p'] = Move(self.tiles.subsurface(PAPER_ICON_TILE), 'p',
					(MOVES_BOX_PAPER_X, MOVES_BOX_PAPER_Y), False)
		self.moves['s'] = Move(self.tiles.subsurface(SCISSORS_ICON_TILE), 's',
					(MOVES_BOX_SCISSORS_X, MOVES_BOX_SCISSORS_Y), False)
		self.moves['cp'] = Move(self.tiles.subsurface(QUESTION_MARK_TILE), '',
					(OPPONENT_BOX_X + 25, OPPONENT_BOX_Y + 50), False)

	# Creates a dictionary with all the sound files.
	def init_sounds(self):
		self.sounds = {
			'shake_down': pygame.mixer.Sound(src + "sounds/shake_down.wav"),
			'shake_up': pygame.mixer.Sound(src + "sounds/shake_up.wav"),
			'charge': pygame.mixer.Sound(src + "sounds/charge.wav"),
			'explosion': pygame.mixer.Sound(src + "sounds/explosion.wav"),
			'bloop': pygame.mixer.Sound(src + "sounds/bloop.wav")
		}

	# Draws all the graphical objects on the screen.
	def draw_screen(self):
		self.scorebox.draw(self.disp)
		self.movebox.draw(self.disp)
		self.opponentbox.draw(self.disp)
		self.instructionsbox.draw(self.disp)
			
	def init_game(self, player_name):
		self.player_name = player_name
		self.scorebox.set_player_name(self.player_name)
		self.game_running = True
		self.exit_game = True
		# Value of dict determines what beats key of dict
		self.beats = {'r': 'p', 'p': 's', 's': 'r'}
		# How many times the move has been dragged up and down
		self.shake_cnt = 0
		# If state is True, move has been moved upwards, if False, move has been moved downwards
		self.shake_state = False
		self.chosen_move = ''
		self.animation_running = -1
		self.init_sounds()
		self.init_scores()

	# Game loop. Returns True if game is to be exited, or False, if we want to go back to the first screen
	def run(self, player_name):
		self.init_game(player_name)
		while self.game_running:
			# Read mouse position
			mouse_pos = pygame.mouse.get_pos()
			# Read mouse velocity
			mouse_vel = pygame.mouse.get_rel()
			# Read event queue
			event_queue = pygame.event.get()
			# Iterate through event queue
			self.process_events(event_queue, mouse_pos)

			# If a move has been chosen, capture mouse motion and increment counter if it has been moved up and down once
			if len(self.chosen_move) > 0:
				self.capture_mouse_motion(mouse_pos, mouse_vel, self.moves[self.chosen_move])

			# Check if move has been made, if so, generate results and start battle animation
			if self.shake_cnt >= 3:
				self.gen_results()

			# Draw background screen
			self.disp.fill(COLOR_BLACK)
			self.draw_screen()
			# Draw player moves
			for move in self.moves.values():
				self.disp.blit(move.get_icon(), move.get_coords())
			# Do animation
			if self.animation_running == 0:
				self.animation_running = self.battleanimation.animate(self.disp, self.results)

			pygame.display.flip()
			# If animation is done, finish
			if self.animation_running == 1:
				pygame.time.set_timer(TIMEOUT_EVENT, 0)
				pygame.time.delay(1000)
				self.finish_round()
			self.clk.tick(30)
		return self.exit_game

	# Processes the event queue
	def process_events(self, event_queue, mouse_pos):
		for e in event_queue:
			if e.type == QUIT:
				self.game_running = False
				self.exit_game = True
			# Disable animation if it has taken too long
			elif e.type == TIMEOUT_EVENT:
				self.animation_running = 1
				print "Animation timed out"
				pygame.time.set_timer(TIMEOUT_EVENT, 0)
			elif e.type == KEYDOWN:
				# Exit game if escape screen has been pressed
				if e.key == K_ESCAPE:
					self.game_running = False
					self.exit_game = True
				# Quit game screen if backspace has been pressed, but do not exit game.
				elif e.key == K_BACKSPACE:
					self.game_running = False
					self.exit_game = False
			# If the mouse has been clicked, we want to see if a move has been clicked. Then, the move will be selected.
			elif e.type == MOUSEBUTTONDOWN and self.animation_running < 0:
				if self.chosen_move == '':
					self.chosen_move = self.select_move(self.moves, mouse_pos)
			# If the mouse button has been released, we want to deselect the move and move it back to the movebox.
			elif e.type == MOUSEBUTTONUP and self.animation_running < 0:
				self.shake_cnt = 0
				self.shake_state = False
				self.chosen_move = ''
				self.release_move(self.moves)

	def gen_results(self):
		self.shake_cnt = 0
		# Make computer move
		self.moves['cp'].set_id(random.sample(set('rps'), 1)[0])
		self.results = self.calc_results(self.chosen_move, self.moves, self.beats)
		# Calculate score but don't update variable before the animation is done, we write to a copy of scores
		scores_cpy = self.scores[:]
		self.calc_score(self.results, scores_cpy)
		# Set a timeout so that if the animation gets stuck, we will exit
		pygame.time.set_timer(TIMEOUT_EVENT, 10000)
		self.battleanimation.init_animation(self.results, self.moves, scores_cpy, self.sounds)
		self.animation_running = 0

	# Capture if mouse has been shaken; plays sounds and increment shake counter and flip state
	def capture_mouse_motion(self, mouse_pos, mouse_vel, move):
		if move.is_clicked() and self.animation_running < 0:
			move.set_coords((mouse_pos[0] - MOVE_DIM / 2, mouse_pos[1] - MOVE_DIM / 2))
			if mouse_vel[1] < 0 and not self.shake_state:
				self.shake_state = True
				self.sounds['shake_up'].play()
			elif mouse_vel[1] > 0 and self.shake_state:
				self.shake_cnt += 1
				self.shake_state = False
				self.sounds['shake_down'].play()

	# Sets the state of a move to clicked and returns the id of the chosen move
	@staticmethod
	def select_move(moves, mouse_pos):
		for move in moves.values():
			coords = move.get_start_coords()
			if coords[0] <= mouse_pos[0] <= coords[0] + MOVE_DIM and coords[1] <= mouse_pos[1] <= coords[1] + MOVE_DIM:
				move.set_clicked(True)
				return move.get_id()

		return ''

	# Releases the selected move and returns it to its start position
	@staticmethod
	def release_move(moves):
		for move in moves.values():
			move.set_coords(move.get_start_coords())
			move.set_clicked(False)

	# Returns a list where slot 0 is the winner and slot 1 is the loser
	@staticmethod
	def calc_results(chosen_move, moves, beats):
		if chosen_move == moves['cp'].get_id():
			# Draw
			return [chosen_move, chosen_move]
		elif beats[chosen_move] == moves['cp'].get_id():
			# Win
			return ['cp', chosen_move]
		else:
			# Lose
			return [chosen_move, 'cp']

	# Calculates the score of a game heat
	@staticmethod
	def calc_score(results, scores):
		if results[0] == 'cp' and results[0] is not results[1]:
			scores[1] += 1
		elif results[0] is not results[1]:
			scores[0] += 1

	# If heat is over, reset heat scores
	@staticmethod
	def reset_heat_score(scores):
		if sum(scores[0:2]) > 2:
			scores[scores.index(max(scores[0:2])) + 2] += 1
			for i in range(0, 2):
				scores[i] = 0

	def finish_round(self):
		# Restore coordinates of moves to starting positons
		self.init_moves()
		# Calculate scores and update scorebox
		self.calc_score(self.results, self.scores)
		self.reset_heat_score(self.scores)
		self.scorebox.update(self.scores)
		# Disable animation
		self.animation_running = - 1
		self.chosen_move = ''
