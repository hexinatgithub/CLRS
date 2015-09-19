class binarySearchTree(object):
	"""docstring for binarySearchTree"""
	def __init__(self):
		super(binarySearchTree, self).__init__()
		self.root = None

	class node(object):
		"""docstring for node"""
		def __init__(self, key):
			self.key = key
			self.parent = None
			self.left = None
			self.right = None

		def setRight(self, right):
			self.right = right

		def setLeft(self, left):
			self.left = left

		def setParent(self, parent):
			self.parent = parent

	def treeSearch(self, x, k):
		if x == None or x.key == k:
			return x
		if k < x.key:
			return treeSearch(x.left, k)
		else:
			return treeSearch(x.right, k)

	def treeMinimum(self, x):
		while x.left != None:
			x = x.left
		return x

	def treeMaximum(self, x):
		while x.right != None:
			x = x.right
		return x

	def treeSuccessor(self, x):
		if x.right != None:
			return self.treeMinimum(x.right)
		y = x.p
		while y != None and y.right == x:
			x = y.parent
			y = y.parent
		return y

	def treePredecessor(self, x):
		if x.left != None:
			return self.treeMaximum(x.left)
		y = x.p
		while y != None and y.left == x:
			x = y
			y = y.parent
		return y

	def inorderTreeWalk(self, x):
		if x != None:
			self.inorderTreeWalk(x.left)
			print x.key
			self.inorderTreeWalk(x.right)

	def treeInsert(self, z):
		x = self.root
		y = None
		while x != None:
			y = x
			if x.key < z.key:
				x = x.right
			else:
				x = x.left
		z.parent = y
		if y == None:
			self.root = z
		elif z.key > y.key:
			y.right = z
		else:
			y.left = z

	def transplant(self, u, v):
		if u.parent == None:
			self.root = v
		elif u == u.parent.right:
			u.parent.right = v
		else:
			u.parent.left = v
		if v != None:
			v.p = u.p

	def treeDelete(self, z):
		if z.left == None:
			self.transplant(z, z.right)
		elif z.right == None:
			self.transplant(z, z.left)
		else:
			y = self.treeMinimum(z)
			if z != y.p:
				self.transplant(y, y.right)
				y.right = z.right
				y.right.p = y
			self.transplant(z, y)
			y.left = z.left
			y.left.parent = y


# tree = binarySearchTree()
# z1 = tree.node(key=2)
# tree.treeInsert(z1)
# z2 = tree.node(key=1)
# tree.treeInsert(z2)
# z3 = tree.node(key=5)
# tree.treeInsert(z3)
# z4 = tree.node(key=4)
# tree.treeInsert(z4)
# z5 = tree.node(key=3)
# tree.treeInsert(z5)
# tree.inorderTreeWalk(tree.root)
# tree.treeDelete(z5)
# print "----"
# tree.inorderTreeWalk(tree.root)