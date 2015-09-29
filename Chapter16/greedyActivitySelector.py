def greedyActivitySelector(s, f):
	n = len(s)
	a0 = (s[0], f[0])
	A = []
	A.append(a0)
	k = 0
	for m in range(1, n):
		if s[m] >= f[k]:
			A.append((s[m], f[m]))
			k = m
	return A


# s = [1,3,0,5,3,5,6,8,8,2,12]
# f = [4,5,6,7,9,9,10,11,12,14,16]
# A = greedyActivitySelector(s, f)
# print A