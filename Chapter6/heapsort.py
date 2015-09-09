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

def max_heapify(A, i):
	l = left(i)
	r = right(i)
	largest = i
	if l < A.heap_size and A[l] > A[i]:
		largest = l
	if r < A.heap_size and A[r] > A[largest]:
		largest = r
	if largest != i:
		A[i], A[largest] = A[largest], A[i]
		max_heapify(A, largest)

def build_max_heap(A):
	A.heap_size = len(A)
	i = (len(A) / 2) - 1
	while i >= 0:
		max_heapify(A, i)
		i -= 1

def heapsort(A):
	build_max_heap(A)
	i = len(A) - 1
	while i >= 1:
		A[0], A[i] = A[i], A[0]
		A.heap_size -= 1
		max_heapify(A, 0)
		i -= 1

# a = [27,17,3,16,13,10,1]
# A = heap()
# A.extend(a)
# heapsort(A)
# print A
