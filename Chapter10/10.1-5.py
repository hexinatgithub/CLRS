from queue import *

class deque(list):
	"""docstring for deque"""
	def __init__(self, n):
		super(deque, self).__init__()
		self.n = n
		init_list = [0]*n
		self.extend(init_list)

	def front_pop(self):
		if self.head == self.tail:
			print "queue underflow"
			return None

		x = self[self.head]
		if self.head == len(self)-1:
			self.head = 1
		else:
			self.head += 1
		return x

	def end_insert(self):
		if self.head == self.tail+1:
			print "queue overflow"
			return None

		self[self.tail] = x
		if self.tail == len(self)-1:
			self.tail = 1
		else:
			self.tail += 1

	def front_insert(self, x):
		if (self.head == self.tail+1) or (self.head == 1 and self.tail == len(self)-1):
			print "queue overflow"
			return None

		if self.head == 1:
			self.head = len(self)-1
		self[self.head] = x

	def end_pop(self):
		x = self[self.tail]
		if self.tail == 1:
			sel.tail = len(self)-1
		else:
			self.tail -= 1
		return x





