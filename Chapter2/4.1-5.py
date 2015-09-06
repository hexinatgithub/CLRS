def find_maximum_subarray(A, low, high):
	sum = 0
	max_sum = sum
	j = 0
	for x in xrange(low, high):
		sum += A[x]
		if sum > max_sum:
			max_sum = sum
			j = x

	sum = 0
	i = 0
	if j < high:
		for x in xrange(low, j+1):
			sum += A[x]
			if A[j+1] > sum:
				max_sum2 = 0
				i = x
	i += 1
	if i > 0:
		return (i, j+1)
	else:
		return (0, j)

A = [1, 2, 3, -100, 8, 9, 10, -100000, 2, 4, 500]
print find_maximum_subarray(A, 0, len(A)-1)
