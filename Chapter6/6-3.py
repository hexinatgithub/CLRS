import sys

class youngTableau(list):
	"""docstring for youngTableau"""
	def __init__(self, rows, columns):
		super(youngTableau, self).__init__()
		self.rows = rows
		self.columns = columns
		self.extend([([sys.maxint] * rows) for i in range(columns)])

	def isFull(self):
		row = self.rows-1
		column = self.columns-1
		if self[row][column] < sys.maxint:
			return True
		else:
			return False


def left(m, n):
	return (m, n-1)


def right(m, n):
	return (m, n+1)


def down(m, n):
	return (m+1, n)


def up(m, n):
	return (m-1, n)


def isWithin(table, row, column):
	if (0 <= row < table.rows) and (0 <= column < table.columns):
		return True
	else:
		return False


def maintain_table_property(table, row, column):
	if not isWithin(table, row, column):
		return
	smallest = table[row][column]
	new_row, new_column = row, column
	right_row, right_column = right(row, column)
	down_row, down_column = down(row, column)
	if isWithin(table, right_row, right_column) and table[right_row][right_column] < smallest:
		smallest = table[right_row][right_column]
		new_row, new_column = right_row, right_column
	if isWithin(table, down_row, down_column) and table[down_row][down_column] < smallest:
		new_row, new_column = down_row, down_column

	if (new_row, new_column) != (row, column):
		table[row][column], table[new_row][new_column] = table[new_row][new_column], table[row][column]
		maintain_table_property(table, new_row, new_column)


def extract_min(table):
	min = table[0][0]
	table[0][0] = sys.maxint
	maintain_table_property(table, 0, 0)
	return min


def insert(table, row, column):
	# exceed the matrix bound
	if not isWithin(table, row, column):
		return
	# print 'insert'
	# print table
	largest = table[row][column]
	new_row, new_column = row, column
	up_row, up_column = up(row, column)
	left_row, left_column = left(row, column)

	if isWithin(table, up_row, up_column) and table[up_row][up_column] > largest:
		largest = table[up_row][up_column]
		new_row, new_column = up_row, up_column
	if isWithin(table, left_row, left_column) and table[left_row][left_column] > largest:
		new_row, new_column = left_row, left_column

	# if insert element is not the largest, then recursive to find the place to insert
	if (row, column) != (new_row, new_column):
		table[row][column], table[new_row][new_column] = table[new_row][new_column], table[row][column]
		insert(table, new_row, new_column)


def insert_element(table, n):
	if table.isFull():
		print "table is full, cann't insert new element"
		return
	else:
		row = table.rows-1
		column = table.columns-1
		table[row][column] = n
		insert(table, row, column)


def sort_table(table):
	rows = table.rows
	columns = table.columns
	temp_table = youngTableau(rows, columns)

	# copy all elements into temp_table
	for r in range(rows):
		for c in range(columns):
			insert_element(temp_table, table[r][c])

	# sort the table
	for r in range(rows):
		for c in range(columns):
			table[r][c] = extract_min(temp_table)


# table = youngTableau(4, 4)
# table[0][0] = 2
# table[0][1] = 3
# table[0][2] = 4
# table[0][3] = 5
# table[1][0] = 8
# table[1][1] = 9
# table[1][2] = 12
# table[1][3] = 14
# table[2][0] = 16
# extract_min(table)
# insert_element(table, 1)
# sort_table(table)
# print table
