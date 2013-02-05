#!/usr/local/bin/python3

import sys
from collections import defaultdict

def main():
	# create a trie
	trie = Trie()
	word = None
	args = (trie, ) # singleton right now
	choices = {'a': test_add, 'b': test_find, 'c': test_size,'d':test_exit}
	while True:
		try:
			char = get_choice("enter a b c d for test: ")	
			if char == 'a' or char == 'b':
				word = input("enter a word: ")
				args = trie, word
			c = choices[char]
			c(*args)
			args = trie,
		except TypeError:
			continue
		except Exception as e:
			break

def test_add(aTrie, word):
	aTrie.add(word)

def test_find(aTrie,word):
	try:
		aTrie.find(word)
	except AttributeError as e:
		print(e)

def test_size(aTrie):
	print("the size of the trie is: {0}".format(aTrie.size_trie()))

def test_exit(aTrie):
	raise Exception

def get_choice(message):
	choice = input(message)
	choice.lower()
	if choice[0] not in ['a', 'b', 'c', 'd']:
		raise TypeError
	return choice[0]

class Node(object):
	"""docstring for Node"""
	def __init__(self):
		super(Node, self).__init__()
		self.next = defaultdict(int)
		# flag of the end of a word
		self.endofword = False

class Trie(object):
	"""docstring for Trie"""
	def __init__(self):
		super(Trie, self).__init__()
		self.size = 0
		self.nodes = []
		self.pos = 1	# this is the position of a node on list
						# since the tree is actually a list of nodes
		self.nodes.append(Node()) # add root

	def add(self, word):
		curr_node = 0
		for char in word:
			if self.nodes[curr_node].next[char] == 0:
				# create a new Node
				self.nodes.append(Node())
				self.nodes[curr_node].next[char] = self.pos
				curr_node = self.pos
				self.pos += 1
			else:
				curr_node = self.nodes[curr_node].next[char]
		# mark the end of a word
		self.nodes[curr_node].endofword = True
		self.size += 1

	def find(self, word):
		curr_node = 0
		for char in word:
			if self.nodes[curr_node].next[char] == 0:
				raise AttributeError("no word found: %s" % word)
			else:
				curr_node = self.nodes[curr_node].next[char]
		print("Word found for: %s" % word);

	def size_trie(self):
		return self.size

if __name__ == '__main__':
	main()