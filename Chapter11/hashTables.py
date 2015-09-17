import sys

class hashTable(object):
	"""docstring for hashTable"""

	def __init__(self, n):
		super(hashTable, self).__init__()
		self.n = n
		self.m = 11
		self.hashTable = [None]*self.m
		self.Delete = sys.maxint
		
	def hashInsert(self, k):
		i = 0
		while i < self.m:
			j = self.hash(k, i)-1
			if (j >= 0) and (self.hashTable[j] == None or self.hashTable[j] == self.Delete):
				self.hashTable[j] = k
				return j
			else:
				i += 1
		print "hash table overflow"

	def hashSearch(self, k):
		i = 0
		j = self.hash(k, i)-1
		while j >= 0 and i < self.m and self.hashTable[j] != None:
			j = self.hash(k, i)
			if self.hashTable[j] == k:
				return j
			else:
				i += 1
		return None

	def hashDelete(self, k):
		j = self.hashSearch(k)
		if j != None:
			self.hashTable[j] = self.Delete

	def hash(self, k, i):
		return ((self.hash1(k)+i*self.hash2(k))%self.m)

	def hash1(self, k):
		return k

	def hash2(self, k):
		return 1+k%(self.m-1)

	def __str__(self):
		return self.hashTable.__str__()


# h = hashTable(n=1000)
# h.hashInsert(k=10)
# h.hashInsert(k=22)
# h.hashInsert(k=31)
# h.hashInsert(k=4)
# h.hashInsert(k=15)
# h.hashInsert(k=28)
# h.hashInsert(k=17)
# h.hashInsert(k=88)
# h.hashInsert(k=59)
# print h

