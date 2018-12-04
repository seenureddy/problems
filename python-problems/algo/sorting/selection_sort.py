# selection sort
# [2, 4, 5, 8, 7]


"""
Performance:

Worst case complexity:       O(n^2)
Best case complexity:        O(n)
Average case complexity:     O(n^2)
Worst case space complexity: O(1) auxiliary

"""


def selection_sort(seq):
    for i in reversed(range(len(seq))):
        max_no_index = 0
        for index in range(1, i + 1):
            if seq[index] > seq[max_no_index]:
                max_no_index = index
        seq[i], seq[max_no_index] = seq[max_no_index], seq[i]
    return seq



alist = [54,26,93,17,77,31,44,55,20]
selection_sort(alist)
print(alist)


def selectionSort(alist):
	for i in range(len(alist)):
		least = i
		for k in range(i + 1, len(alist)):
			if alist[k] < alist[least]:
				least = k
		alist[i], alist[least] = alist[least], alist[i]
	return alist


alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)
