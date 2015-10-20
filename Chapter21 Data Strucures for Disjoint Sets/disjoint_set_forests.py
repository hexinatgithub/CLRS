def make_set(x):
	x.p = x
	x.rank = 0

def unioin(x, y):
	link(find_set(x), find_set(y))

def link(x, y):
	if x.rank > y.rank:
		y.p = x
	else:
		x.p = y
		if x.rank == y.rank:
			y.rank = y.rank+1

def find_set(x):
	if x != x.p:
		x.p = find_set(x.p)
	return x.p