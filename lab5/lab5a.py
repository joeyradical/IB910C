import random
import sys

def gen_name(input):
	if input =='r':
		return "Rock"
	elif input =='p':
		return "Paper"
	elif input =='s':
		return "Scissors"
		

def main():
	running = True
	#Value of dict determines what beats key of dict
	beats = {'r': 'p', 'p' : 's', 's': 'r'}
	user_score = 0
	comp_score = 0
	print "\n********** \t ROCK, PAPER, AND SCISSORS \t ************ \n"
	print "Welcome to Rock, Paper, and Scissors! The rules follow: "
	print "Each player chooses between either rock, paper or scissors. "
	print "Rock beats scissors, paper beats rock, and scissors beat paper."
	print "Enjoy!\n"
	print "*************************************************************"
	
	while running:
		#Input move from user
		user_choice =  raw_input("Please input your choice (r/p/s): \t").lower()
		corr_input = False
		
		#Check that input is in the correct format, otherwise request new input
		while corr_input == False:
			if user_choice == 'r' or user_choice == 'p' or user_choice == 's':
				corr_input = True
			else:
				user_choice = raw_input("Invalid option. Please choose between Rock ('r'), Paper ('p'), or Scissors('s'): \t").lower()
			
		#Generate the move of the computer	
		comp_move = random.randint(0,2)
		if comp_move == 0:
			comp_choice = 'r'
		elif comp_move == 1:
			comp_choice = 'p'
		elif comp_move == 2:
			comp_choice = 's'
		
		#Output move of user and computer	
		print "You chose " + gen_name(user_choice) + " and the computer chose " + gen_name(comp_choice)
		
		#Determine results
		if comp_choice == user_choice:
			print "It's a draw! You both chose " + gen_name(comp_choice)
		elif beats[comp_choice] == user_choice:
			print gen_name(user_choice) + " beats " + gen_name(comp_choice) + ". You win!"
			user_score += 1
		else:
			print gen_name(comp_choice) + " beats " + gen_name(user_choice) + ". You lose!"
			comp_score += 1
			
		#Ask user if he/she wants to play again
		print "The current score is \t You: " + str(user_score) + " \t Computer: " + str(comp_score)
		play_again = raw_input("Would you like to play again? (y/n) \t").lower()
		if play_again == 'n':
			running = False			
	print "Game finished! The final score was: \t You: " + str(user_score) + "\t Computer: " + str(comp_score)
	return 1

if __name__ == "__main__":
	status = main()
	sys.exit(status)