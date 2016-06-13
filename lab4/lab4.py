#IB910C -S VT2016 Laboration 4:
#Written in Python 2.7.9 using Mac OSX 10.3
import Tkinter
import tkMessageBox
import sys
from PIL import ImageTk, Image
import pygame

#Class for label which inherits from a Tkinter Label and also contains a boolean variable specifying if the label is made of an image or text
class ImageLabel(Tkinter.Label):
	def __init__(self,*args,**kwargs):
		Tkinter.Label.__init__(self,*args,**kwargs)
		self.is_image = None

#Application Class
class Slideshow():
	def __init__(self):
		#Initialize root
		self.root = Tkinter.Tk()
		self.root.title("Top 10 greatest guitar players of all time")
		self.info_list = None
		self.init_startscreen()


#####     CLASS METHODS FOR START SCREEN       #####
	
	def init_startscreen(self):
		self.start_button = Tkinter.Button(self.root, text="Start slideshow", font = ("Helvetica", 20), command = self.start_slideshow)
		self.start_button.pack(fill = Tkinter.BOTH, side = Tkinter.TOP,padx = 50, pady = 50)
		
	def start_slideshow(self):
		self.start_button.destroy()
		self.init_slideshow()

#####    CLASS METHODS FOR SLIDESHOW SCREEN     #####

	def init_slideshow(self):	
		#Initialize Main window
		self.frame = Tkinter.Frame(self.root,bg = "grey")
		self.frame.pack()
		self.heading = Tkinter.Label(self.frame,text = "Temporary heading", font=('Helvetica', 20), bg = "grey")
		self.heading.pack(side=Tkinter.TOP, pady = 10)
		self.photo_container = Tkinter.Canvas(self.frame, width = 500, height = 500, bg = "black", highlightbackground = "black")
		self.photo_container.pack(side = Tkinter.TOP,padx = 10)
		
		#Initialize infotext
		self.info_text = Tkinter.Label(self.frame, font = ("Helvetica", 15), anchor = Tkinter.W, wraplength = 500,justify = Tkinter.CENTER,bg = "white")
		self.info_text.pack(side=Tkinter.TOP)
		
		
		#Initialize bottom frame
		self.bottom_frame = Tkinter.Frame(self.frame, bg = "grey",pady = 15,padx = 10)
		self.bottom_frame.pack(side = Tkinter.BOTTOM, fill = Tkinter.BOTH)
		
		#Initialize front arrow. If arrow image is not found, replace with text.
		try:
			front_arrow = ImageTk.PhotoImage(Image.open("app_data/images/frontarrow.jpg"))
			front_arrow_disabled = ImageTk.PhotoImage(Image.open("app_data/images/frontarrow_disabled.jpg"))
			self.front_button = ImageLabel(self.bottom_frame,image = front_arrow, bg = "grey")
			self.front_button.is_image = True
			self.front_button.image = front_arrow
			self.front_button.image_disabled = front_arrow_disabled
		except IOError:
			self.front_button = ImageLabel(self.bottom_frame, text = "Forward")
			self.front_button.is_image = False
		self.front_button.bind("<Button-1>", self.increment)
		self.front_button.pack(side= Tkinter.RIGHT, fill = Tkinter.BOTH)
		
		#Initialize back arrow. If arrow image is not found, replace with text
		try:
			back_arrow = ImageTk.PhotoImage(Image.open("app_data/images/backarrow.jpg"))
			back_arrow_disabled = ImageTk.PhotoImage(Image.open("app_data/images/backarrow_disabled.jpg"))
			self.back_button = ImageLabel(self.bottom_frame,image = back_arrow, bg = "grey")
			self.back_button.is_image = True
			self.back_button.image = back_arrow
			self.back_button.image_disabled = back_arrow_disabled
		except IOError:
			self.back_button = ImageLabel(self.bottom_frame, text = "Backward")
			self.back_button.is_image = False
		self.back_button.bind("<Button-1>", self.decrement)
		self.back_button.pack(side = Tkinter.LEFT, fill = Tkinter.BOTH)
		
		#Initialize infolist
		try:
			file = open("app_data/info.txt",'r')
			temp = file.read().split('%')
			file.close()
		except IOError as e:
			tkMessageBox.showerror("Error", str(e) + ". Closing application.")
			self.root.destroy()
			sys.exit(-1)
		self.index = 0
		self.info_list = []
		for entry in temp:
			temp2 = entry.split('#')
			self.info_list.append([temp2[0].replace("\n", ""), temp2[1]])
		self.update()
		
	def update(self):
		#Change arrow to disable if at the end or beginning of the slideshow, or if the button consists of text, change the text color to grey
		if self.index >= len(self.info_list)-1:
			if self.front_button.is_image:
				self.front_button['image'] = self.front_button.image_disabled
			else:
				self.front_button['fg'] = "grey"
		else:
			if self.front_button.is_image:
				self.front_button['image'] = self.front_button.image
			else:
				self.front_button['fg'] = "black"
		if self.index == 0:
			if self.back_button.is_image:
				self.back_button['image'] = self.back_button.image_disabled
			else:
				self.back_button['fg'] = "grey"
		else:
			if self.back_button.is_image:
				self.back_button['image'] = self.back_button.image
			else:
				self.back_button['fg'] = "black"
		
		#Update slide content
		name = self.info_list[self.index][0]
		self.heading['text'] = name
		pygame.mixer.init()
		
		#Open image, if not found show error message and insert black dot instead of image
		try:
			image = Image.open("app_data/images/"+name.replace(" ", "") + ".jpg")
		except IOError as e:
			mixer.music.stop()
			self.show_filenotfound("Image", str(e))
			image = Image.new("RGB", (1,1), "black")
			
		photo = ImageTk.PhotoImage(image)
		self.photo_container.create_image(250,250,image=photo)
		self.photo_container.image = photo
		self.info_text['text'] = self.info_list[self.index][1]
	
		#Play audio
		try:
			pygame.mixer.music.load("app_data/audio/"+ name.replace(" ","") + ".ogg");
			pygame.mixer.music.play()
		except pygame.error as e:
			pygame.mixer.music.stop()
			self.show_filenotfound("Audio", str(e))
			
	def show_filenotfound(self,filetype, msg):
		tkMessageBox.showerror("Error", filetype + " not found. " + msg)
		
	def run(self):
		self.root.mainloop()	
	
	def increment(self, event):
		#If not at end of list, update content
		if self.index < len(self.info_list)-1:
			self.index += 1
			self.update()
		else:
			tkMessageBox.showwarning("Warning!", "Reached end of slideshow!")
		
		
	def decrement(self, event):
		#If not at beginning of list, update content
		if self.index > 0:
			self.index -= 1
			self.update()
		else:
			tkMessageBox.showwarning("Warning!", "Reached beginning of slideshow")
		
	
def main():
	slideshow = Slideshow()
	slideshow.run()


if __name__ == "__main__":
    main()