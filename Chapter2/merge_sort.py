# sum = 0

def merge_sort(A, begin, end):
	# print "merge_sort", begin, end
	if begin < end:
		p = (begin + end) / 2
		merge_sort(A, begin, p)
		merge_sort(A, p+1, end)
		# print begin, p, end
		merge(A, begin, p, end)

import sys

def merge(A, begin, p, end):
	n1 = p - begin + 1
	n2 = end - p
	L = list()
	R = list()
	for i in range(n1):
		L.append(A[begin+i])
	for j in range(n2):
		R.append(A[p+1+j])
	L.append(sys.maxint)
	R.append(sys.maxint)
	i = 0
	j = 0
	for x in range(n1 + n2):
		if L[i] <= R[j]:
			A[begin+x] = L[i]
			i += 1
		else:
			A[begin+x] = R[j]
			j += 1
			global sum
			# sum += n1 - i


A = [7,6,5,4,3,2,1]
merge_sort(A, 0, len(A)-1)
print A