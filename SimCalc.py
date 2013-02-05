from tkinter import *
from tkinter.messagebox import showinfo

class gui(Frame):
	"""docstring for gui"""
	def __init__(self, master=None):
		Frame.__init__(self,master)
		self.master = master
		self.label = Label(self,text="Enter your name:")
		self.label.pack(side=TOP)
		self.entry = Entry(self)
		self.entry.pack(side=TOP)
		self.button = Button(self, text="Submit")
		self.button.bind("<Button-1>", self.click_submit)
		self.button.pack(side=LEFT)
		self.button2 = Button(self, text="Quit")
		self.button2.bind("<Button-1>", self.click_quit)
		self.button2.pack(side=RIGHT)
		self.pack()

	def reply(self, name):
		showinfo(title="Reply", message="Your name is: {0}".format(name))

	def click_submit(self,event):
		self.reply(self.entry.get())

	def click_quit(self,event):
		self.master.destroy()

if __name__ == '__main__':
	win = Tk()
	app = gui(win)
	app.mainloop()		

