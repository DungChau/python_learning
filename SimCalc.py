from tkinter import *
from tkinter.messagebox import showinfo
import math
import parser

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
			lambda: self.text.set(self.result(self.text.get())))
		buttone.pack(side=LEFT)
		buttone = Button(self.frm, text="clear", command=
			lambda: self.text.set(" "))
		buttone.pack(side=RIGHT)

	def load_exp(self, text):
		st = parser.expr(text)
		return st, st.compile() 

	def result(self, text):
		source_string = str(text)
		t , s = self.load_exp(source_string)
		return eval(s)

	def click_quit(self,event):
		self.master.destroy()

###################################################################
# this is for future implementation
###################################################################
# this gets text from entry box and eval it to a result
class Interpreter(object):
	"""docstring for Interpreter"""
	def __init__(self, text):
		super(Interpreter, self).__init__()
		self.stack = []
		self.text = text
		self.pos = 0
		self.operator = ["+", "-"]

	def parse(self):
		pass

	def evaluate(self):
		pass

# This class represents a literal token aka. a number
class Integer(object):
	"""docstring for Integer"""
	def __init__(self, value):
		super(Integer, self).__init__()
		self.value = value
	def toInt(self):
		return int(self.value)
		
class Exp(object):
	"""docstring for Exp"""
	def __init__(self, arg):
		super(Exp, self).__init__()
		self.arg = arg

class Term(Exp):
	"""docstring for Term"""
	def __init__(self, arg):
		super(Term, self).__init__()
		self.arg = arg

class Factor(object):
	"""docstring for Factor"""
	def __init__(self, arg):
		super(Factor, self).__init__()
		self.arg = arg
		
		
if __name__ == '__main__':
	win = Tk()
	app = gui(win)
	app.mainloop()		

