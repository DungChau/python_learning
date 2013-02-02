#!/usr/local/bin/python3

file = open("hw1-inst1.txt")
# numberOfPeople = int(file.readline())
matrix = []
for line in file:
	lyne = line.split()
	lyne = [int(i) for i in lyne]
	matrix.append(lyne)
	print(lyne)
file.close()

class Person(object):
	"""docstring for Person"""
	def __init__(self, ID):
		super(Person, self).__init__()
		self.ID = ID
		
class Table(object):
	"""docstring for Table"""
	def __init__(self, numberOfChairs):
		super(Table, self).__init__()
		self.numberOfChairs = numberOfChairs
		