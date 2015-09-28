LEFT = 1
UP = 2
ID = 3

def lcsLength(X, Y):
	m = len(X)
	n = len(Y)
	b = {}
	c = {}
	for i in range(0, m+1):
		c[(i, -1)] = 0
	for j in range(0, n+1):
		c[(-1, j)] = 0
	for i in range(0, m):
		for j in range(0, n):
			if X[i] == Y[j]:
				c[(i, j)] = c[(i-1, j-1)]+1
				b[(i, j)] = ID
			elif c[(i-1, j)] >= c[(i, j-1)]:
				c[(i, j)] = c[(i-1, j)]
				b[(i, j)] = UP
			else:
				c[(i, j)] = c[(i, j-1)]
				b[(i, j)] = LEFT
	return (c, b)

def printLCS(b, X, i, j):
	if i ==-1 or j == -1:
		return
	if b[(i, j)] == ID:
		printLCS(b, X, i-1, j-1)
		print X[i],
	elif b[(i, j)] == UP:
		printLCS(b, X, i-1, j)
	else:
		printLCS(b, X, i, j-1)

# X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
# Y = ['B', 'D', 'C', 'A', 'B', 'A']
# (c, b) = lcsLength(X, Y)
# printLCS(b, X, len(X)-1, len(Y)-1)
# print c
# print b





