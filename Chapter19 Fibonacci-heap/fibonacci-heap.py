import math
import sys

class linkedList(object):
	"""docstring for linkedList"""
	def __init__(self):
		super(linkedList, self).__init__()
		self.head = None
		self.n = 0

	def insert(self, x):
		if self.head != None:
			x.right = self.head.right
			x.left = self.head
			self.head.right.left = x
			self.head.right = x
		else:
			x.right = x
			x.left = x
			self.head = x
		self.n = self.n+1

	def delete(self, x):
		if self.n == 0:
			self.head = None
		else:
			x.left.right = x.right
			x.right.left = x.left
		self.n = self.n-1

	def concatenate(self, list2):
		if list2.head != None:
			self.head.left.right = list2.head.left
			list2.head.left.right = self.head.left
			self.head.left = list2.head
			list2.head.left = self.head
		return self

	def p(self):
		n = self.head
		for x in range(0, self.n):
			print n.key
			n = n.right


class node(object):
	"""docstring for node"""
	def __init__(self):
		super(node, self).__init__()
		self.degree = 0
		self.left = None
		self.right = None
		self.p = None
		self.mark = False
		self.child = None
		self.key = None

	def insert_child(self, x):
		if self.child == None:
			x.left = x
			x.right = x
			self.child = x
		else:
			x.left = self.child
			x.right = self.child.right
			self.child.right = x
			self.degree = self.degree+1


class fibonacciHeap(object):
	"""docstring for fibonacciHeap"""
	def __init__(self):
		super(fibonacciHeap, self).__init__()
		self.n = 0
		self.min = None
		self.rootList = None

	def fib_heap_insert(self, x):
		x.degree = 0
		x.p = None
		x.mark = False
		x.child = None
		if self.min == None:
			self.rootList = linkedList()
			self.rootList.insert(x)
			self.min = x
		else:
			self.rootList.insert(x)
			if x.key < self.min.key:
				self.min = x
		self.n = self.n+1

	def fib_heap_minimum(self):
		return self.min

	def fib_heap_union(self, h2):
		h = fibonacciHeap()
		h.min = self.min
		h.rootList = self.rootList
		h.rootList.concatenate(h2.rootList)
		if (self.min == None) or (h2.min != None and h2.min.key < self.min.key):
			h.min = h2.min
		h.n = self.n+h2.n
		return h

	def fib_heap_extract_min(self):
		z = self.min
		if z != None:
			x = z.child
			flag = 0
			while flag == 1 and x != None:
				if x.right == z.child:
					flag = 1
				self.rootList.insert(x)
				x.p = None
				x = x.right
			self.rootList.delete(z)
			if z == z.right:
				self.min = None
			else:
				self.min = z.right
				self.consolidate()
			self.n = self.n-1
		return z

	def consolidate(self):
		A = [None for i in range(0, self.D()+1)]
		# for i in range(0, self.D()+1):
		# 	A[i] = None
		flag = 0
		w = self.min
		while flag == 0:
			if w.right == self.min:
				flag = 1
			x = w
			d = x.degree
			while A[d] != None:
				y = A[d]
				if x.key > y.key:
					x, y = y, x
				self.fib_heap_link(y, x)
				A[d] = None
				d = d+1
			A[d] = x
			w = w.right
		self.min = None
		for i in range(0, self.D()+1):
			if A[i] != None:
				if self.min == None:
					self.rootList = linkedList()
					self.rootList.insert(A[i])
					self.min = A[i]
					# print '1', A[i].key
				else:
					self.rootList.insert(A[i])
					if A[i].key < self.min.key:
						self.min = A[i]
					# print '2', A[i].key		
		w = w.right

	def fib_heap_link(self, y, x):
		self.rootList.delete(y)
		x.insert_child(y)
		y.mark = False

	def D(self):
		return int(math.log(self.n))+10

	def fib_heap_decrease_key(self, x, k):
		if k > x.key:
			print "new key is greater than current key"
			return
		x.key = k
		y = x.p
		if y != None and x.key < y.key:
			self.cut(x, y)
			self.cascading_cut(y)
		if x.key < self.min.key:
			self.min = x

	def cut(self, x, y):
		if x == y.child:
			if x.right == x:
				y.child = None
			else:
				x.right.left = x.left
				x.left.right = x.right
				y.child = x.right
		else:
			x.right.left = x.left
			x.left.right = x.right
		self.rootList.insert(x)
		x.p = None
		x.mark = False

	def cascading_cut(self, y):
		z = y.p
		if z != None:
			if y.mark == False:
				y.mark = True
			else:
				self.cut(y, z)
				self.cascading_cut(z)

	def fib_heap_delete(self, x):
		self.fib_heap_decrease_key(x, -sys.maxint)
		return self.fib_heap_extract_min()


f = fibonacciHeap()

x1 = node()
x1.key = 1
f.fib_heap_insert(x1)

x2 = node()
x2.key = 2
f.fib_heap_insert(x2)

x3 = node()
x3.key = 3
f.fib_heap_insert(x3)

x4 = node()
x4.key = 4
f.fib_heap_insert(x4)

# f.rootList.p()
f.fib_heap_extract_min()
f.rootList.p()
# print f.rootList.n





