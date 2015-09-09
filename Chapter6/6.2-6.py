class heap(list):
	"""docstring for heap"""
	def __init__(self, heap_size):
		super(heap, self).__init__()
		self.heap_size = heap_size

def parent(i):
	return ((i+1) / 2) - 1

def left(i):
	return 2*i+1

def right(i):
	return 2*i+2

def max_heapify(A, i):
	while i < A.heap_size:
		l = left(i)
		r = left(i)
		largest = i
		if l < A.heap_size and A[l] > A[i]:
			largest = l
		if r < A.heap_size and A[r] > A[largest]:
			largest = r
		if largest != i:
			A[i], A[largest] = A[largest], A[i]
			i = largest
		else:
			break

# a = [27,17,3,16,13,10,1]
# A = heap(len(a))
# A.extend(a)
# max_heapify(A, 2)
# print A
