import sys

def find_max_crossing_subarray(A, low, mid, high):
	left_sum = -sys.maxint
	sum = 0
	i = mid
	max_left = mid
	while i >= low:
		sum += A[i]
		if sum > left_sum:
			max_left = i
			left_sum = sum
		i -= 1

	right_sum = -sys.maxint
	sum = 0
	i = mid + 1
	max_right = mid + 1
	while i <= high:
		sum += A[i]
		if sum >= right_sum:
		 	max_right = i
		 	right_sum = sum
		i += 1
	return (max_left, max_right, left_sum+right_sum)

def find_maximum_subarray(A, low, high):
	if low == high:
		return (low, high, A[low])
	else:
		mid = (low + high) / 2
		(left_low, left_high, left_sum) = find_maximum_subarray(A, low, mid)
		(right_low, right_high, right_sum) = find_maximum_subarray(A, mid+1, high)
		(cross_low, cross_high, cross_sum) = find_max_crossing_subarray(A, low, mid, high)
		if left_sum >= right_sum  and left_sum >= cross_sum:
			return (left_low, left_high, left_sum)
		elif right_sum >= left_sum and right_sum >= cross_sum:
			return (right_low, right_high, right_sum)
		else:
			return (cross_low, cross_high, cross_sum)


A = [1, 2, 3, -100, 8, 9, 10, -100000, 2, 4, 500]
print find_maximum_subarray(A, 0, len(A)-1)

# A = [-8, -2, -4]
# print find_maximum_subarray(A, 0, len(A)-1)



