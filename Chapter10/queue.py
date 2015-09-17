class Queue(list):
	"""docstring for Queue"""
	def __init__(self, n):
		super(Queue, self).__init__()
		self.n = n
		init_list = [0]*n
		self.extend(init_list)
		self.tail = 1
		self.head = 1

	def enqueue(self, x):
		if self.head == self.tail+1:
			print "queue overflow"
			return None

		self[self.tail] = x
		if self.tail == len(self)-1:
			self.tail = 1
		else:
			self.tail += 1

	def dequeue(self):
		if self.head == self.tail:
			print "queue underflow"
			return None

		x = self[self.head]
		if self.head == len(self)-1:
			self.head = 1
		else:
			self.head += 1
		return x


# q = Queue(n=10)
# q.enqueue(x=10)
# q.enqueue(x=20)
# q.enqueue(x=30)
# q.enqueue(x=40)
# q.enqueue(x=50)
# print q.dequeue()
# print q.dequeue()
