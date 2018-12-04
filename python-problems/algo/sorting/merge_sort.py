def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    # print "left", left
    right = merge_sort(lst[mid:])
    return merge(left, right)


def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])


alist = [54,26,93,17,77,31,44,55,20]
mst = merge_sort(alist)
print(mst)


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        left_half = alist[ :mid]
        right_half = alist[mid: ]
        mergeSort(left_half)
        mergeSort(right_half)
        
        i, j, k = (0, 0, 0)
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]
                i = i + 1
            else:
                alist[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            alist[k] = left_half[i]
            i = i + 1
            j = j + 1

        while j < len(right_half):
            alist[k] = right_half[j]
            j = j + 1
            k = k + 1
        
        print("merger_sort..", alist)
        return alist


alist = [54,26,93,17,77,31,44,55,20]
mst = mergeSort(alist)
print(mst)
