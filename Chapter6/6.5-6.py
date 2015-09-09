def heap_increase_key(A, i, key):
	if key < A[i]:
		print "new key is smaller than current key"
	while i > 0 and A[parent(i)] < A[i]:
		A[i] = A[parent(i)]
		i = parent(i)
	A[i] = key
