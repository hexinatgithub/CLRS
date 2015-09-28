import sys

def cutRod(p, n):
	if n == 0:
		return 0
	q = -sys.maxint
	for i in xrange(1,n+1):
		q = max(q, q[x]+cutRod(n-i))
	return q