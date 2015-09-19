class node(object):
	"""docstring for node"""
	def __init__(self, value):
		super(node, self).__init__()
		self.left = None
		self.right = None
		self.parent = None
		self.value = value


class radixTree(object):
	"""docstring for radixTree"""
	def __init__(self):
		super(radixTree, self).__init__()
		self.root = node(value=None)

	def treeInsert(self, value):
		x = self.root
		y = None
		i = 0
		flag = 0
		while i < len(value):
			if x == None:
				x = node(value=None)
				if flag:
					y.right = x
				else:
					y.left = x
			y = x
			if value[i] == '0':
				x = x.left
				flag = 0
			else:
				x = x.right
				flag = 1
			i += 1
		if x == None:
			x = node(value)
			x.parent = y
			if flag:
				y.right = x
			else:
				y.left = x
		else:
			x.value = value

	def inorderTreeWalk(self, x):
		if x != None:
			if x.value != None:
				print x.value
			self.inorderTreeWalk(x.left)
			self.inorderTreeWalk(x.right)


# tree = radixTree()
# tree.treeInsert(value='0')
# tree.treeInsert(value='011')
# tree.treeInsert(value='10')
# tree.treeInsert(value='100')
# tree.treeInsert(value='1011')
# tree.inorderTreeWalk(x=tree.root)