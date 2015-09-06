def selection_sort(A):
	# selection sort, input is a array A
	for x in xrange(0,len(A)-1):
		min_index = x;
		for j in xrange(x,len(A)):
			if A[min_index] > A[j]:
				min_index = j
		A[min_index], A[x] = A[x], A[min_index]

A=[2,6,8,10,6,14,3,0,100,9,8]
selection_sort(A)
print A

# 这里保持的loop invariant
# initialization: 在排序之前不存在最小的排在前面
# maintenance: 如果这次循环前j个元素保持从小到大排列，那么下次循环的时候，j+1个元素也保持从小到大排列
# termination: 循环n-1次循环结束，前0..n-2为数组最小元素，且保持从小到大排列，所以算法正确

# 算法的复杂度在best_case和worst_cast下面都是O(n^2)