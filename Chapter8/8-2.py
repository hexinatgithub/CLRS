# e:
def countingSort(A, k):
	C = [0]*(k+1)
	for x in A:
		C[x] += 1
	for x in range(1, len(C)):
		C[x] += C[x-1]
	position = list(C)

	i = 0
	while i < len(A):
		if isCorrectPlace(A, C, i):
			i += 1
		else:
			index = position[A[i]]-1
			position[A[i]] -= 1
			A[i], A[index] = A[index], A[i]


def isCorrectPlace(A, C, i):
	if C[A[i]-1] <= i < C[A[i]]:
		return True
	else:
		return False

# A = [9,1,6,8,10,5,5]
# countingSort(A, 10)
# print A