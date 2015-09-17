class elements(object):
	"""docstring for elements"""
	def __init__(self, key):
		super(elements, self).__init__()
		self.pre = None
		self.key = key
		self.next = None


class linkedList(object):
	"""docstring for linkedList"""
	def __init__(self):
		super(linkedList, self).__init__()
		self.nil = elements(None)
		self.nil.pre = self.nil
		self.nil.next = self.nil
		self.length = 0

	def list_search(self, k):
		x = self.nil.next
		while x != self.nil and x.key != k:
			x = x.next
		return x

	def list_insert(self, x):
		x.next = self.nil.next
		x.pre = self.nil
		self.nil.next.pre = x
		self.nil.next = x
		self.length += 1

	def list_delete(self, x):
		x.pre.next = x.next
		x.next.pre = x.pre


# l = linkedList()
# x1 = elements(key=5)
# x2 = elements(key=6)
# x3 = elements(key=7)
# x4 = elements(key=8)
# x5 = elements(key=9)
# l.list_insert(x1)
# l.list_insert(x2)
# l.list_insert(x3)
# l.list_insert(x4)
# l.list_insert(x5)
# s1 = l.list_search(k=7)
# print s1.key
# l.list_delete(s1)
# s1 = l.list_search(k=7)
# print s1.key




