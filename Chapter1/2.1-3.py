def search(A, item):
	for x in xrange(0,len(A)):
		if A[x] == item:
			return x
	return None