def hoare_partition(A, p, r):
	x = A[p]
	i = p-1
	j = r+1
	while True:
		while True:
			j -= 1
			if A[j] <= x:
				break

		while True:
			i += 1
			if A[i] >= x:
				break

		if i < j:
			A[i], A[j] = A[j], A[i]
		else:
			return j

def quickSort(A, p, r):
	if p < r:
		q = hoare_partition(A, p, r)
		quickSort(A, p, q)
		quickSort(A, q+1, r)


A = [9,10,7,5,12]
quickSort(A, 0, len(A)-1)
print A