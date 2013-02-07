from tkinter import *
from tkinter.messagebox import showinfo
import math

class gui(Frame):
	"""docstring for gui"""
	def __init__(self, master=None):
		Frame.__init__(self,master)
		self.master = master
		self.master.title("A Simple Calculator")
		self.pack(expand=YES, fill=BOTH)

		self.text= StringVar()
		self.label = Label(self,text="Enter to the textbox below:")
		self.label.pack(side=TOP)
		self.entry = Entry(self, textvariable=self.text)
		self.entry.pack(side=TOP)

		rows = ["abcd", "0123", "4567", "89()"]
		for row in rows:
			frm = Frame(self)
			frm.pack(side=TOP)
			for char in row:
				buttone = Button(frm, text=char, 
					command=lambda char=char: self.text.set(self.text.get() + char))
				buttone.pack(side=LEFT)

		self.frm = Frame(self)
		self.frm.pack(side=TOP)
		for char in "+-*/=":
			buttone = Button(self.frm, text=char, 
				command=lambda char=char: 
					self.text.set(self.text.get() + " " + char + " "))
			buttone.pack(side=LEFT)

		self.frm = Frame(self)
		self.frm.pack(side=BOTTOM)
		buttone = Button(self.frm, text="result", command= 
			lambda: self.result(self.text))
		buttone.pack(side=LEFT)
		buttone = Button(self.frm, text="clear", command=
			lambda: self.text.set(" "))
		buttone.pack(side=RIGHT)

	def result(self, text):
		pass

	def reply(self, name):
		showinfo(title="Reply", message="Your name is: {0}".format(name))

	def gui_pow(self, x, y):
		self.text.set(pow(x, y))		 

	def click_submit(self,event):
		# self.reply(self.entry.get())
		self.gui_pow(int(self.entry1.get()), int(self.entry2.get()))

	def click_quit(self,event):
		self.master.destroy()

# this gets text from entry box and eval it to a result
class Interpreter(object):
	"""docstring for Interpreter"""
	def __init__(self, arg):
		super(Interpreter, self).__init__()
		self.arg = arg

# This class represents a literal token aka. a number
class LiteralToken(object):
	"""docstring for LiteralToken"""
	def __init__(self, value):
		super(LiteralToken, self).__init__()
		self.value = value
	def toInt(self):
		return int(self.value)
		
class Exp(object):
	"""docstring for Exp"""
	def __init__(self, arg):
		super(Exp, self).__init__()
		self.arg = arg

class AddExp(Exp):
	"""docstring for AddExp"""
	def __init__(self, arg):
		super(AddExp, self).__init__()
		self.arg = arg
		
if __name__ == '__main__':
	win = Tk()
	app = gui(win)
	app.mainloop()		

