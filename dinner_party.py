#!/usr/local/bin/python3

def main():
	dinner = DinnerParty()
	people = dinner.parse_file("hw1-inst1.txt")
	dinner.write_output(people)
	for person in people:
		print(person.preference)

class DinnerParty(object):
	"""docstring for DinnerParty"""
	def __init__(self):
		super(DinnerParty, self).__init__()		
	# one interresting fact for me is that even though
	# a method only take one param python passes 2 params 
	# to the function: self AND filename
	def parse_file(self, filename):
		file = open(filename)
		index = 0
		people = []
		for line in file:
			index += 1
			lyne = line.split()
			lyne = [int(i) for i in lyne]
			person = Person(index, lyne)
			people.append(person)
		file.close()
		return people
	# This is a method used to output the result
	def write_output(self, table):
		file = open("hw1-sol1.txt", "wt")
		for t in table:
			# write can only takes string not a list
			file.write(",".join(map(str, t.preference)))
		file.close()

class Person(object):
	"""docstring for Person"""
	def __init__(self, ID, preference):
		super(Person, self).__init__()
		self.ID = ID
		self.preference = preference
		
class Table(object):
	"""docstring for Table"""
	def __init__(self, numberOfChairs, guests):
		super(Table, self).__init__()
		self.numberOfChairs = numberOfChairs
		self.guests = guests
	def seat():
		pass

	def generate_state():
		pass

	def calculate_score():
		pass	

if __name__ == '__main__':
	main()