class Stack(list):
	"""docstring for Stack"""
	def __init__(self, n):
		super(Stack, self).__init__()
		self.n = n
		init_list = [0]*n
		self.extend(init_list)
		self.top = 0

	def stack_empty(self):
		if self.top == 0:
			return True
		else:
			return False

	def push(self, x):
		self.top += 1
		self[self.top] = x

	def pop(self):
		if self.stack_empty():
			print "Stack underflow"
		else:
			self.top -= 1
		return self[self.top+1]


# s = Stack(n=10)
# s.push(x=10)
# s.push(x=20)
# s.push(x=30)
# s.push(x=40)
# s.push(x=50)
# print s.pop()
# print s.pop()
