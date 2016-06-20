import random
import sys


def chr2str(input):
	# Converts char to string
	if input == 'r':
		return "Rock"
	elif input == 'p':
		return "Paper"
	elif input == 's':
		return "Scissors"


def print_intro():
	# Prints introductory text
	print "\n********** \t ROCK, PAPER, AND SCISSORS \t **************** \n"
	print "Welcome to Rock, Paper, and Scissors! The rules follow: "
	print "Each player chooses between either rock, paper or scissors. "
	print "Rock beats scissors, paper beats rock, and scissors beat paper."
	print "Enjoy!\n"
	print "*************************************************************"


def det_results(comp_choice, user_choice, beats):
	# Compares user and computer move and determines results
	if comp_choice == user_choice:
		print "It's a draw! You both chose " + chr2str(comp_choice)
		return 0
	elif beats[comp_choice] == user_choice:
		print chr2str(user_choice) + " beats " + chr2str(comp_choice) + ". You lose!"
		return -1
	else:
		print chr2str(comp_choice) + " beats " + chr2str(user_choice) + ". You win!"
		return 1


def create_comp_move():
	# Generate the move of the computer
	return random.sample(set('rps'), 1)[0]


def create_user_move():
	# Input move from user
	user_choice = raw_input("Please input your choice (r/p/s): \t").lower()
	corr_input = False

	# Check that input is in the correct format, otherwise request new input
	while not corr_input:
		if user_choice == 'r' or user_choice == 'p' or user_choice == 's':
			corr_input = True
		else:
			user_choice = raw_input(
				"Invalid option. Please choose between Rock ('r'), Paper ('p'), or Scissors('s'): \t").lower()
	return user_choice


def run():
	running = True
	# Value of dict determines what beats key of dict
	beats = {'r': 'p', 'p': 's', 's': 'r'}
	user_score = 0
	comp_score = 0
	while running:

		user_move = create_user_move()
		comp_move = create_comp_move()

		# Output move of user and computer
		print "You chose " + chr2str(user_move) + " and the computer chose " + chr2str(comp_move)

		# Determine results
		winner = det_results(user_move, comp_move, beats)
		if winner > 0:
			user_score += 1
		elif winner < 0:
			comp_score += 1

		# Ask user if he/she wants to play again
		print "The current score is \t You: " + str(user_score) + " \t Computer: " + str(comp_score)
		play_again = raw_input("Would you like to play again? (y/n) \t").lower()
		if play_again == 'n':
			running = False
	print "Game finished! The final score was: \t You: " + str(user_score) + "\t Computer: " + str(comp_score)
	return 1


def main():
	print_intro()
	run()
	return 1


if __name__ == "__main__":
	status = main()
	sys.exit(status)