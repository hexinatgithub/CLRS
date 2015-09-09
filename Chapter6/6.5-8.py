def heap_delete(A, i):
	if A.heap_size > 1:
		A[i] = A[A.heap_size-1]
		A.__delitem__(A.heap_size-1)
		max_heapify(A, i)
	A.heap_size -= 1