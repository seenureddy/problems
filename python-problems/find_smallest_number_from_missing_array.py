"""Find the smallest positive number missing from an unsorted array"""

def solution(A):
    occurrence = [False] * (len(A) + 1)
    for item in A:
        if 1 <= item <= len(A) + 1:
            occurrence[item-1] = True
 
    # Find out the missing minimal positive integer.
    for index in range(len(A) + 1):
        if occurrence[index] == False:
            return index + 1
 
    raise Exception("Should never be here.")
    return -1

A = [1, 3, 6, 4, 1, 2]
print solution(A)
