import sys
from heapsort import *

def heap_maximum(A):
	return A[0]

def heap_extract_max(A):
	if A.heap_size <= 0:
		print "heap underflow"
	max = A[0]
	A[0] = A[A.heap_size-1]
	A.__delitem__(A.heap_size-1)
	A.heap_size -= 1
	max_heapify(A, 0)
	return max

def heap_increase_key(A, i, key):
	if key < A[i]:
		print "new key is smaller than current key"
	A[i] = key
	while i > 0 and A[parent(i)] < A[i]:
		A[parent(i)], A[i] = A[i], A[parent(i)]
		i = parent(i)


def max_heap_insert(A, key):
	A.append(-sys.maxint)
	A.heap_size += 1
	heap_increase_key(A, A.heap_size-1, key)

# A = heap()
# max_heap_insert(A, 2)
# max_heap_insert(A, 1)
# max_heap_insert(A, 9)
# max_heap_insert(A, 10)
# max_heap_insert(A, 7)
# max_heap_insert(A, 3)
# heap_extract_max(A)
# heap_extract_max(A)
# heap_extract_max(A)
# print A
