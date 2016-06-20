import pygame
from constants import *

""""The BattleAnimation class provides methods which do an animation, which is initialized in init_animation()
and executed in animate(). It also plays sounds related to the animation. """


class BattleAnimation:
	def __init__(self, fonts):
		self.moves = {}
		self.fonts = fonts
		self.scores = None
		self.winner = 0
		self.winner_destination = [0, 0]
		self.animation_cnt = 0
		self.animation_x = 0
		self.animation_y = 0
		self.x_sign = 0
		self.y_sign = 0
		self.winner_start_coords = (0, 0)
		self.animation_phase = 0
		self.sounds = {}

	def init_animation(self, results, moves, scores, sounds):
		# Initialize variables
		self.winner = 0
		self.winner_destination = [0, 0]
		self.animation_cnt = 0
		self.animation_x = 0
		self.animation_y = 0
		self.x_sign = 0
		self.y_sign = 0
		self.winner_start_coords = (0, 0)
		self.animation_phase = 1
		self.moves = moves
		self.scores = scores
		self.sounds = sounds

		# Calculate destination for winner to travel
		if self.moves[results[0]].get_coords()[0] < self.moves[results[1]].get_coords()[0]:
			self.x_sign = 1
			self.winner_destination[0] = self.moves[results[1]].get_coords()[0] - \
				self.moves[results[0]].get_coords()[0]
		else:
			self.x_sign = -1
			self.winner_destination[0] = self.moves[results[0]].get_coords()[0] - \
				self.moves[results[1]].get_coords()[0]

		if self.moves[results[0]].get_coords()[1] < self.moves[results[1]].get_coords()[1]:
			self.y_sign = 1
			self.winner_destination[1] = self.moves[results[1]].get_coords()[1] - \
				self.moves[results[0]].get_coords()[1]
		else:
			self.y_sign = -1
			self.winner_destination[1] = self.moves[results[0]].get_coords()[1] - \
				self.moves[results[1]].get_coords()[1]
		self.winner_start_coords = self.moves[results[0]].get_coords()

	def animate(self, disp, results):
		# Fade out question mark
		if self.animation_phase == 1:
			icon = self.moves['cp'].get_icon().convert()
			alpha = icon.get_alpha()
			icon.set_alpha(alpha - 10)
			self.moves['cp'].set_icon(icon)
			if alpha == 0:
				self.animation_phase = 2
				icon = self.moves[self.moves['cp'].get_id()].get_icon().convert()
				icon.set_alpha(0)
				self.moves['cp'].set_icon(icon)
			return 0
		# Fade in computer move
		elif self.animation_phase == 2:
			icon = self.moves['cp'].get_icon()
			alpha = icon.get_alpha()
			icon.set_alpha(alpha + 10)
			self.moves['cp'].set_icon(icon)
			if alpha > 245:
				icon = self.moves[self.moves['cp'].get_id()].get_icon()
				self.moves['cp'].set_icon(icon)
				self.animation_phase = 3
			return 0
		# Flip winner if necesserary
		elif self.animation_phase == 3:
			if self.moves[results[0]].get_coords()[0] < self.moves[results[1]].get_coords()[0]:
				icon = self.moves[results[0]].get_icon()
				icon = pygame.transform.flip(icon, True, False)
				self.moves[results[0]].set_icon(icon)
			self.animation_phase = 4
			return 0
		# Take charge...
		elif self.animation_phase == 4:
			if results[0] is not results[1]:
				self.sounds['charge'].play()
			winner_coords = self.moves[results[0]].get_coords()
			self.moves[results[0]].set_coords((winner_coords[0] - self.x_sign * self.winner_destination[0] / 100,
													winner_coords[1] - self.y_sign * self.winner_destination[1] / 100))
			self.animation_cnt += 1
			if self.animation_cnt > 10:
				self.animation_phase = 5
			return 0
		# Smash the other guy!
		elif self.animation_phase == 5:
			# Animation phase is assumed to be done until proven otherwise
			x_done = True
			y_done = True
			pygame.mixer.stop()
			if (((self.animation_x < self.winner_destination[0] - MOVE_DIM / 2) and self.x_sign > 0) or (
				((self.animation_x > self.winner_destination[0] * self.x_sign + MOVE_DIM / 2) and self.x_sign < 0))):
				self.animation_x += self.x_sign * ABS_VELOCITY
				x_done = False
			if (((self.animation_y < self.winner_destination[1] - MOVE_DIM / 2) and self.y_sign > 0) or (
				((self.animation_y > self.winner_destination[1] * self.y_sign + MOVE_DIM / 2) and self.y_sign < 0))):
				self.animation_y += self.y_sign * ABS_VELOCITY
				y_done = False

			self.moves[results[0]].set_coords(
				(self.winner_start_coords[0] + self.animation_x, self.winner_start_coords[1] + self.animation_y))

			if y_done and x_done:
				self.animation_phase = 6
			return 0
		# If draw, do confused animation
		elif self.animation_phase == 6:
			if results[0] == results[1]:
				self.sounds['bloop'].play()
				question_mark = self.fonts['medium'].render("?", True, COLOR_WHITE)
				disp.blit(question_mark, (self.moves[results[0]].get_coords()[0] + MOVE_DIM / 2,
											self.moves[results[0]].get_coords()[1] - 2))
				disp.blit(question_mark, (
					self.moves['cp'].get_coords()[0] + MOVE_DIM / 2, self.moves['cp'].get_coords()[1] - 2))
				pygame.display.flip()
			else:
				self.sounds['explosion'].play()
			if sum(self.scores[0:2]) < 3:
				return 1
			else:
				self.animation_phase = 7
				return 0

		# Draw win/lose message
		elif self.animation_phase == 7:
				if self.scores[0] > self.scores[1]:
					msg = self.fonts['x-large'].render("victory.", True, COLOR_GREEN)
				else:
					msg = self.fonts['x-large'].render("defeat.", True, COLOR_RED)
				disp.blit(msg, (50, 50))
				return 1
		else:
			return 1
