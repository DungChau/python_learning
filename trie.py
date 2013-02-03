#!/usr/local/bin/python3

import re, types
from collections import defaultdict

def main():
	# create a trie
	trie = Trie()
	trie.add("new")
	trie.add("none")
	trie.add("test")
	trie.find("none")
	print("the size of the trie is: %d" % trie.size_trie())

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

	def find(self, word):
		curr_node = 0
		for char in word:
			if self.nodes[curr_node].next[char] == 0:
				raise AttributeError("no word found: %s" % word)
			else:
				curr_node = self.nodes[curr_node].next[char]
		print("Word found for: %s" % word);

	def size_trie(self):
		return len([node for node in self.nodes if node.endofword == True])
		
if __name__ == '__main__':
	main()