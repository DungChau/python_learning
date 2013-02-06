from tkinter import *
from tkinter.messagebox import showinfo
import math

class gui(Frame):
	"""docstring for gui"""
	def __init__(self, master=None):
		Frame.__init__(self,master)
		self.master = master
		self.label = Label(self,text="Enter 2 numbers:")
		self.label.pack(side=TOP)
		self.entry1 = Entry(self)
		self.entry1.pack(side=TOP)
		self.entry2 = Entry(self)
		self.entry2.pack(side=TOP)
		self.button = Button(self, text="Submit")
		self.button.bind("<Button-1>", self.click_submit)
		self.button.pack(side=LEFT)
		self.button2 = Button(self, text="Quit")
		self.button2.bind("<Button-1>", self.click_quit)
		self.button2.pack(side=RIGHT)
		self.pack()

	def reply(self, name):
		showinfo(title="Reply", message="Your name is: {0}".format(name))

	def add(self, x, y):
		showinfo(title="Result", message="x^y is: {0}".format(pow(x,y)))		 

	def click_submit(self,event):
		# self.reply(self.entry.get())
		self.add(int(self.entry1.get()), int(self.entry2.get()))

	def click_quit(self,event):
		self.master.destroy()

if __name__ == '__main__':
	win = Tk()
	app = gui(win)
	app.mainloop()		

