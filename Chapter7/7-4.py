def partition(A, p, r):
	x = A[r]
	i = p-1
	for j in range(p,r):
		if A[j] <= x:
			i += 1
			A[i], A[j] = A[j], A[i]
	new_pivot = i + 1
	if new_pivot != r:
		A[new_pivot], A[r] = A[r], A[new_pivot]
	else:
		new_pivot = (p+r)/2
	return new_pivot


def tail_recursive_quicksort(A, p, r):
	while p < r:
		q = partition(A, p, r)

		# use if else clause to direct the recuisive call to good partition.
		if q <= (p+r)/2:
			tail_recursive_quicksort(A, p, q-1)
			p = q+1
		else:
			tail_recursive_quicksort(A, p+1, r)
			r = q-1

# A = [9,0,1,2]
# tail_recursive_quicksort(A, 0, len(A)-1)
# print A
