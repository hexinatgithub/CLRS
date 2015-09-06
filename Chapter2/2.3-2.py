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
	i = 0
	j = 0
	for x in range(n1 + n2):
		if i >= n1:
			for r in xrange(j, n2):
				A[begin+x] = R[r]
				x += 1
			return
		elif j >= n2:
			for l in xrange(i, n1):
				A[begin+x] = L[l]
				x += 1
			return
		else:
			# print 'else', begin, p, end, i, j, x
			if L[i] <= R[j]:
				A[begin+x] = L[i]
				i += 1
			else:
				A[begin+x] = R[j]
				j += 1


# A = [4,2,8,9,10,2,6,4,8,6,3,2,1,100,9,10]
# merge_sort(A, 0, len(A)-1)
# print A