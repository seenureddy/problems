
def bubble_sort(seq):
	"""
	Worst case time complexity: O(n2)
	"""
	for i in range(len(seq)):
		for k in range(len(seq) - 1, i, -1):
			if seq[k] < seq[k-1]:
				swap(seq, k, k - 1)


def swap(seq, x, y):
	temp = seq[x]
	seq[x] = seq[y]
	seq[y] = temp

alist=[30,40,90,50,20,60,70,80,100,110]
bubble_sort(alist)

print(alist)


def bubbleSort(alist):
	"""
	Best case time complexity: O(n)
	"""
	swapped = 1
	for i in range(len(alist)):
		if (swapped == 0):
			return 

		for k in range(len(alist) - 1, i, -1):
			if alist[k] < alist[k - 1]:
				alist[k], alist[k - 1] = alist[k - 1], alist[k]

	return alist


alist=[80,100,110,30,40,90,50,20,60,70]
bubbleSort(alist)

print(alist)
