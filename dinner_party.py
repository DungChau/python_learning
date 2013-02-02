#!/usr/local/bin/python3

file = open("hw1-inst1.txt")
# numberOfPeople = int(file.readline())
matrix = []
people = []

def main():
	index = 0
	for line in file:
		index += 1
		lyne = line.split()
		lyne = [int(i) for i in lyne]
		# matrix.append(lyne)
		person = Person(index, lyne)
		people.append(person)
		print(people[index - 1].preference)
	file.close()

class Person(object):
	"""docstring for Person"""
	def __init__(self, ID, preference):
		super(Person, self).__init__()
		self.ID = ID
		self.preference = preference
		
class Table(object):
	"""docstring for Table"""
	def __init__(self, numberOfChairs):
		super(Table, self).__init__()
		self.numberOfChairs = numberOfChairs
		

if __name__ == '__main__':
	main()