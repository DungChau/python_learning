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

    def search(self, key, parent=None):
        if self.node is None:
            raise KeyError
        if self.node.key == key:
            return self, parent
        elif self.node.key > key:
            if self.left is not None:
                return self.left.search(key, self)
        else:
            if self.right is not None:
                return self.right.search(key, self)

    def delete(self, key):
        subtree, parent = self.search(key)
        child_cnt = subtree.children_count()
        if child_cnt == 0:
            if parent.left is subtree:
                parent.left = None
            else:
                parent.right = None
            del subtree
        elif child_cnt == 1:
            if subtree.left:
                temp = subtree.left
            else:
                temp = subtree.right
            if parent:
                if parent.left is subtree:
                    parent.left = temp
                elif parent.right is subtree:
                    parent.right = temp
            del subtree
        else:
            parent = subtree
            succ = subtree.right
            while succ.left:
                parent = succ
                succ = succ.left
            # swap it to deleted tree
            subtree.node = succ.node
            if parent.left is succ:
                parent.left = None
            else:
                parent.right = None

    def children_count(self):
        count = 0
        if node is None:
            return None
        if self.left is not None:
            count += 1
        if self.right is not None:
            count += 1
        return count

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print((self.node.key, self.node.val))
        if self.right:
            self.right.print_tree()

    def tree_gen(self):
        stack = []
        sub = self
        while stack or sub:
            if sub:
                stack.append(sub)
                sub = sub.left
            else:
                sub = stack.pop()
                yield sub.node
                sub = sub.right


class Node(object):
    """docstring for Node"""

    def __init__(self, key, val):
        super(Node, self).__init__()
        self.key = key
        self.val = val
