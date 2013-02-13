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
			self.left = Tree(Node(key, val))
		else:
			self.right = Tree(Node(key, val))
	def search(self, subTree, key):
		if subTree.node is None:
			raise KeyError
		if subTree.node.key == key:
			return subTree.node.val
		elif subTree.node.key < key:
			return self.search(subTree.left, key)
		else:
			return self.search(subTree.right, key)
		
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
	print(tree.search(tree, "Mike"))

if __name__ == '__main__':
	main()
