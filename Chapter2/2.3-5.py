def binary_search(A, v, begin, end):
	p = (begin + end) / 2
	if begin > end:
		# print begin, end
		return None
	elif A[p] == v:
		return p
	elif A[p] < v:
		return binary_search(A, v, p+1, end)
	elif A[p] > v:
		return binary_search(A, v, begin, p-1)

# A = [1, 10, 20, 40, 70, 85, 90]
# print binary_search(A, 1, 0, len(A)-1)