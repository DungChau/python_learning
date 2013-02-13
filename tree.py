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
			return self.node.val
		elif self.node.key > key:
			if self.left is not None:
				return self.left.search(key)
		else:
			if self.right is not None:
				return self.right.search(key)
		
class Node(object):
	"""docstring for Node"""
	def __init__(self, key, val):
		super(Node, self).__init__()
		self.key = key
		self.val = val

def main():
	tree = Tree()
	tree.insert("John", 14)
	tree.insert("Jane", 34)
	tree.insert("Mike", 56)
	tree.insert("Xie", 45)
	tree.insert("Tang", 67)
	tree.insert("Abel", 43)
	print(tree.search("Mike"))
	print(tree.search("Xie"))
	print(tree.search("Abel"))
if __name__ == '__main__':
	main()
