def insertion_sort(A):
	for x in xrange(1,len(A)):
		key = A[x]
		i = x - 1
		while i > 0 and A[i] < key:
			A[i+1] = A[i]
			i -= 1
		A[i+1] = key

A=[90,80,76,81,45,81]
insertion_sort(A)
print A