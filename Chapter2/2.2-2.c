//selection sort

int *selection_sort(int *A, int len) {
	for (int i = 0; i < len-1; ++i)
	{
		int min_index = i;
		for (int j = i; j < len; ++j) {
			if (A[min_index] > A[j]) {
				min_index = j;
			}
		}
		int temp = A[i];
		A[i] = A[min_index];
		A[min_index] = temp;
	}
}