class node(object):
	"""docstring for node"""
	def __init__(self, value):
		super(node, self).__init__()
		self.left = None
		self.right = None
		self.parent = None
		self.value = value
		self.color = None

class redBlackTree(object):
	"""docstring for redBlackTree"""
	def __init__(self):
		super(redBlackTree, self).__init__()
		self.nil = node(None)
		self.nil.color = 'Black'
		self.root = self.nil
		
	def leftRotate(self, x):
		y = x.right
		x.right = y.left
		if y.left != self.nil:
			y.left.parent = x
		y.parent = x.parent
		if x.parent == self.nil:
			self.root = y
		elif x == x.parent.left:
			x.parent.left = y
		else:
			x.parent.right = y
		y.left = x
		x.parent = y

	def rightRotate(self, y):
		"""
		CLRS 13.2-1
		"""
		x = y.left 		# set y
		y.left = x.right 	# turn y's left subtree into x's right subtree
		if x.right != self.nil:
			x.right.parent = y
		x.parent = y.parent		# link x's parent to y
		if y.parent == self.nil:
			self.root = x
		elif y.parent.left == y:
			y.parent.left = x
		else:
			y.parent.right = x
		x.right = y 	# put y on x's right
		y.parent = x		

	def rbInsert(self, z):
		y = self.nil
		x = self.root
		while x != self.nil:
			y = x
			if x.value > z.value:
				x = x.left
			else:
				x = x.right
		z.parent = y
		if y == self.nil:
			self.root = z
		elif z.value < y.value:
			y.left = z
		else:
			y.righ = z
		z.left = self.nil
		z.right = self.nil
		z.color = 'Red'
		self.rbInsertFixUp(z)

	def rbInsertFixUp(self, z):
		while z.parent.color == 'Red':
			if z.parent == z.parent.parent.left:
				y = z.parent.parent.right
				if y.color == 'Red':	# case1
					z.parent.color = 'Black'
					y.color = 'Black'
					z.parent.parent.color = 'Red'
					z = z.parent.parent
				else:
					if z == z.parent.right:		# case2
						z = z.parent
						self.leftRotate(z)
					z.parent.color = 'Black'	# case3
					z.parent.parent.color = 'Red'
					self.rightRotate(z.parent.parent)
			else:
				y = z.parent.parent.left
				if y.color == 'Red':
					z.parent.color = 'Black'
					y.color = 'Black'
					z.parent.parent.color = 'Red'
					z = z.parent.parent
				else:
					if z.parent.left == z:
						z = z.parent
						self.rightRotate(z)
					z.parent.color = 'Black'
					z.parent.parent.color = 'Red'
					self.leftRotate(z.parent.parent)
		self.root.color = 'Black'

	def treeMinimum(self, x):
		while x.left != self.nil:
			x = x.left
		return x

	def treeMaximum(self, x):
		while x.right != self.nil:
			x = x.right
		return x

	def rbTransplant(self, u, v):
		if u.parent == self.nil:
			self.root = v
		elif u == u.parent.left:
			u.parent.left = v
		else:
			u.parent.right = v
		v.parent = u.parent

	def rbDelete(self, z):
		y = z
		y_original_color = y.color
		x = self.nil
		if z.left == self.nil:
			x = z.right
			self.rbTransplant(z, z.right)
		elif z.right == self.nil:
			x = z.left
			self.rbTransplant(z, z.left)
		else:
			y = self.treeMinimum(z.right)
			y_original_color = y.color
			x = y.right
			if y.parent == z:
				x.parent = y
			else:
				self.rbTransplant(y, y.right)
				y.right = z.right
				y.right.parent = y
			self.rbTransplant(z, y)
			y.left = z.left
			y.left.parent = y
			y.color = z.color
		if y_original_color == 'Black':
			self.rbDeleteFixUp(x)

	def rbDeleteFixUp(self, x):
		while x != self.nil and x.color == 'Black':
			if x == x.parent.left:
				w = x.parent.right
				if w.color == 'Red':	# case1
					x.parent.color = 'Red'
					w.color = 'Black'
					self.leftRotate(x.parent)
					w = x.parent.right
				if w.left.color == 'Black' and w.right.color == 'Black':		# case2
					w.color = 'Red'
					x = x.parent
				else:
					if w.right.color == 'Black':	# case3
						w.left.color = 'Black'
						w.color = 'Red'
						self.rightRotate(w)
						w = x.parent.right
					w.color = x.parent.color
					x.parent.color = 'Black'
					w.right.color = 'Black'
					self.leftRotate(x.parent)
					x = self.root
			else:
				w = x.parent.left
				if w.color == 'Red':	# case1
					x.parent.color = 'Red'
					w.color = 'Black'
					self.rightRotate(x.parent)
					w = x.parent.left
				if w.left.color == 'Black' and w.right.color == 'Black':		# case2
					w.color = 'Red'
					x = x.parent
				else:
					if w.left.color == 'Black':		# case3
						w.right.color = 'Black'
						w.color = 'Red'
						self.leftRotate(w)
						w = x.parent.left
					w.color = x.parent.color
					x.parent.color = 'Black'
					w.left.color = 'Black'
					self.rightRotate(x.parent)
					x = self.root
		x.color = 'Black'

	def inorderTreeWalk(self, x):
		if x != self.nil:
			self.inorderTreeWalk(x.left)
			if x.value != None:
				print x.value, x.color
			self.inorderTreeWalk(x.right)

tree = redBlackTree()
z1 = node(value=27)
tree.rbInsert(z1)
z2 = node(value=25)
tree.rbInsert(z2)
z3 = node(value=22)
tree.rbInsert(z3)
z4 = node(value=17)
tree.rbInsert(z4)
z5 = node(value=15)
tree.rbInsert(z5)
z6 = node(value=13)
tree.rbInsert(z6)
z7 = node(value=11)
tree.rbInsert(z7)
z8 = node(value=8)
tree.rbInsert(z8)
z9 = node(value=6)
tree.rbInsert(z9)
z10 = node(value=1)
tree.rbInsert(z10)
print 'root:', tree.root.value, tree.root.color
tree.inorderTreeWalk(tree.root)
# tree.rbDelete(z1)
# print "----"
# print 'root:', tree.root.value, tree.root.color
# tree.inorderTreeWalk(tree.root)













