#!/usr/local/bin/python3

import re, types
from collections import defaultdict

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
		self.nodes.append(Node()) # add root

	def add(self, word):
		for char in word:
			pass
	
	def find(self, word):
		pass

	def size(self):
		pass
		
