class heap(list):
	"""docstring for heap"""
	def __init__(self):
		super(heap, self).__init__()
		self.heap_size = 0
		

def parent(i):
	return ((i+1) / 2) - 1

def left(i):
	return 2*i+1

def right(i):
	return 2*i+2

def min_heapify(A, i):
	l = left(i)
	r = left(i)
	minmum = i
	if l < A.heap_size and A[l] < A[i]:
		minmum = l
	if r < A.heap_size and A[r] < A[minmum]:
		minmum = r
	if minmum != i:
		A[i], A[minmum] = A[minmum], A[i]
		min_heapify(A, minmum)