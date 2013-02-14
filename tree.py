import unittest

class Tree(object):
	"""docstring for Tree"""
	def __init__(self, node=None):
		super(Tree, self).__init__()
		self.left = None
		self.right = None
		self.node = node
	def insert(self, key, val):
		if self.node is None:
			self.node = Node(key, val)
		if self.node.key == key:
			self.node.val = val
		elif key < self.node.key:
			if self.left is None:
				self.left = Tree()
			self.left.insert(key, val)
		else:
			if self.right is None:
				self.right = Tree()
			self.right.insert(key, val)
	def search(self, key):
		if self.node is None:
			raise KeyError
		if self.node.key == key:
			return self
		elif self.node.key > key:
			if self.left is not None:
				return self.left.search(key)
		else:
			if self.right is not None:
				return self.right.search(key)
	def delete(self, key):
		pass
		
class Node(object):
	"""docstring for Node"""
	def __init__(self, key, val):
		super(Node, self).__init__()
		self.key = key
		self.val = val

class testBinaryTree(unittest.TestCase):
	"""docstring for testBinaryTree"""
	def setUp(self):
		self.tree = Tree()
	def test_insert(self):
	 	self.tree.insert("John", 14)
	 	self.assertTrue(self.tree.search("John").node.val == 14)	
	 	self.tree.insert("Jane", 34)
	 	self.assertTrue(self.tree.search("Jane").node.val == 34)
	 	self.tree.insert("Xie", 45)
	 	self.assertTrue(self.tree.search("Xie").node.val == 45)
	 	self.tree.insert("Jane", 24)
	 	self.assertTrue(self.tree.search("Jane").node.val == 24)
	def test_search(self):
	 	self.tree.insert("Xie", 45)
	 	self.tree.insert("Tang", 67)
	 	self.tree.insert("Abel", 43)
	 	self.assertTrue(self.tree.search("Tang"), 67)
	 	self.assertRaises(KeyError, self.tree.search("Amber"),0)	

if __name__ == '__main__':
	unittest.main()
