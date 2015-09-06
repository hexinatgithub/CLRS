import sys

def find_maximum_subarray(A, low, high):
	max_sum = 0
	(low_i, high_i) = (-1, -1)	# allow empty subarray
	for x in xrange(low,high+1):
		sum = 0
		for i in xrange(x,high+1):
			sum += A[i]
			if sum > max_sum:
				max_sum = sum
				(low_i, high_i) = (x, i)
	return (low_i, high_i, max_sum)

# A = [1, 2, 3, -100, 8, 9, 10, -100000, 2, 4, 500]
# print find_maximum_subarray(A, 0, len(A)-1)
