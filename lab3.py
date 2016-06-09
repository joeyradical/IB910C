#IB910C -S VT2016 Laboration 3:
#Written in Python 2.7.9 using Mac OSX 10.3

import Tkinter
import random
import tkMessageBox

class Game:
	#Declare widgets
	def __init__(self):
		self.init_game()
		
	#Function mapped to guess button and return key
	def guess(self, event):
		try:
			#Highlight text
			self.text_field.tag_add(Tkinter.SEL, "1.0", Tkinter.END)
			self.text_field.mark_set("insert", 1.1)
			
			#Retrieve text from text field
			ans = int(self.text_field.get(1.0,Tkinter.END))
			
			#Increment number of guesses
			self.no_guesses +=1
			self.no_guesses_label['text'] = "Guesses: " + str(self.no_guesses)
			
			#Check if guess was correct
			if ans > self.corr_answer:
				self.text['text'] = "Your guess was too high! Try a lower number"
			elif ans < self.corr_answer:
				self.text['text'] = "Your guess was too low! Try a higher number"
			elif ans == self.corr_answer:
				self.text['text'] = "Correct!!!"
				self.text['bg'] = 'green'
				self.text['font'] = ('Comic Sans', 40)
				if tkMessageBox.askyesno("Victory is yours!","Congratulations! \n" + str(ans) + " was the correct number. \nWould you like to play again?"):
					self.restart()
				else:
					self.exit()
			
		except ValueError:
			tkMessageBox.showerror("Error!", "Guess was not an integer value. Please enter an integer value instead.")
		
	
	#Function mapped to restart button
	def restart(self):
		self.root.destroy()
		self.init_game()
	
	#Function mapped to exit button	
	def exit(self):
		self.root.destroy()

	def init_game(self):
	
		#Initialize game variables
		self.no_guesses = 0
		self.corr_answer = random.randint(1,100);
		self.intro_text = 'Welcome to "Guess my number". \n I am thinking of a number between 1 and 100, and your task is to guess this number! Please enter your guess in the box below.'
	
		#Initialize root window
		self.root = Tkinter.Tk()
		self.root.resizable(width=False, height=False)
		self.root.title("Guess my number - the classic guessing name for children of all ages.")
		#Binds return key to guess function
		self.root.bind('<Return>', self.guess)
		
		#Initialize upper frame
		self.upper_frame = Tkinter.Frame(bd = 2)
		self.text = Tkinter.Label(self.upper_frame, font = ("Helvetica", 20), anchor = Tkinter.W, wraplength = 500,justify = Tkinter.CENTER)
		self.upper_frame.pack(side=Tkinter.TOP, fill = Tkinter.BOTH)
		self.text['text'] = self.intro_text
		self.text.pack(side = Tkinter.TOP, fill=Tkinter.BOTH, expand = Tkinter.YES,pady = 10)
	
		#Initialize lower frame
		self.lower_frame = Tkinter.Frame(height = 100, bg = 'grey')
		self.no_guesses_label = Tkinter.Label(self.lower_frame)
		self.text_field = Tkinter.Text(self.lower_frame,width = 30, height = 2)
		self.text_field.pack(side = Tkinter.LEFT,padx = 5,pady=5)
		self.text_field.insert(Tkinter.INSERT, "Enter your guess here")
		self.exit_button = Tkinter.Button(self.lower_frame, text = "Exit",bg = 'grey',command = self.exit);
		self.exit_button.pack(side=Tkinter.RIGHT,padx=5);
		self.restart_button = Tkinter.Button(self.lower_frame, text = "Restart", command = self.restart, bg = 'grey');
		self.restart_button.pack(side=Tkinter.RIGHT,padx =5,pady = 5)
		self.guess_button = Tkinter.Button(self.lower_frame, text = "Guess", command = lambda: self.guess(None), bg = 'grey');
		self.guess_button.pack(side=Tkinter.LEFT,padx =5)
		self.no_guesses_label.pack(side = Tkinter.LEFT, padx = 5)
		self.no_guesses_label['text'] = "Guesses: " + str(self.no_guesses)
		self.lower_frame.pack(fill = Tkinter.BOTH)
		
	def run(self):
		self.root.mainloop()
	
def main():
	game = Game()
	game.run()

if __name__ == "__main__":
    main()