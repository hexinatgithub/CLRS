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

def quitckSort(A, p, r):
	if p < r:
		q = partition(A, p, r)
		quitckSort(A, p, q - 1)
		quitckSort(A, q + 1, r)

# A = [9,10,5,7,4,1,20]
# quitckSort(A, 0, len(A)-1)
# print A