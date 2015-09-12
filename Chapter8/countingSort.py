def countingSort(A, B, k):
	C = [0]*(k+1)
	for j in A:
		C[j] += 1
	# now C[j] contain the number of elements equal to j
	for i in range(1,k+1):
		C[i] += C[i-1]
	# noew C[i] contain the number of elements less or equal to i
	i = len(A)-1
	while i >= 0:
		B[C[A[i]]-1] = A[i]
		C[A[i]] -= 1
		i -= 1

#A = [9,1,6,8,10,5,5]
#B = [0,0,0,0,0,0,0]
#countingSort(A, B, 10)
#print B