class set(object):
	"""docstring for set"""
	def __init__(self):
		super(set, self).__init__()
		self.head = None
		self.tail = None
		self.len = 0


class node(object):
	"""docstring for node"""
	def __init__(self):
		super(node, self).__init__()
		self.set = None
		self.next = None


def make_set(x):
	s = set()
	s.head = x
	s.tail = x
	x.set = s
	s.len = 1
	return s
	

def find_set(x):
	return x.set.head


def union(x, y):
	s1 = x.set
	s2 = y.set
	if x.len < y.len:
		s1, s2 = s2, s1
	x = s2.head
	while x != None:
		x.set = s1
		x = x.next
	s1.tail = s2.tail