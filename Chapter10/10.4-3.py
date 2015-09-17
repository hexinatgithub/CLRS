class tree_t(object):
	"""docstring for tree_t"""
	def __init__(self, parent, left, right, key):
		super(tree_t, self).__init__()
		self.parent = parent
		self.left = left
		self.right = right
	

import sys

def print_tree(tree):
	stack = list(sys.maxint)
	count = 0
	stack[count] = tree
	count += 1
	while count > -1:
		count -= 1
		tree = stack[count]
		print tree.key
		if tree.right:
			stack[count] = tree.right
			count += 1

		if tree.left:
			stack[count] = tree.left
			count += 1