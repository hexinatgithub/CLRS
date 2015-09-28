import sys

def matrixChainOrder(p):
	n = len(p)-1
	m = {}
	s = {}
	for i in xrange(1, n+1):
		m[(i, i)] = 0
	for l in range(2, n+1):
		for i in range(1, n-l+2):
			j = i+l-1
			m[(i, j)] = sys.maxint
			for k in range(i, j):
				q = m[i, k] + m[k+1, j] + p[i-1]*p[k]*p[j]
				if q < m[(i, j)]:
					m[(i, j)] = q
					s[(i, j)] = k
	return (m, s)

def printOptimalParens(s, i, j):
	if i == j:
		print ("A[%d"%i)+']',
	else:
		print "(",
		printOptimalParens(s, i, s[i, j])
		printOptimalParens(s, s[i, j]+1, j)
		print ")",

def matrixMultiply(A, B):
	if A.columns != B.rows:
		print "incompatible dimensions"
		return
	else:
		C = [[0 for col in range(A.rows)] for row in range(B.columns)]
		for i in range(0, A.rows):
			for j in xrange(0, B.columns):
				C[i][j] = 0
				for k in xrange(0,A.columns):
					C[i][j] = C[i][j]+A[i][k]*B[k][j]
		return C

def matrixChainMultiply(A, s, i, j):
	if i == j:
		return A[i]
	else:
		return matrixMultiply(matrixChainMultiply(A, s, i, s[i][j]), matrixChainMultiply(A, s, s[i][j]+1, j))

# p = [30,35,15,5,10,20,25]
# (m, s) = matrixChainOrder(p)
# printOptimalParens(s, 1, len(p)-1)
# mul = [[0]*5]*3
# print mul



