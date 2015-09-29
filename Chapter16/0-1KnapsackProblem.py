def dynamic_0_1_Knapsack(v, w, n, W):
	c = {}
	for w in xrange(0, W+1):
		c[(-1, w)] = 0
	for i in range(0, n):
		c[(i, -1)] = 0
		for w in range(1, W+1):
			if w[i] <= W:
				if v[i]+c[i-1, w-w[i]] > c[i-1,w]:
					c[i, w] = v[i]+c[i-1, w-w[i]]
				else:
					c[i, w] = c[i-1, w]
			else:
				c[i, w] = c[i-1, w]