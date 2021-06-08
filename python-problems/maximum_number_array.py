"""
Find the element which appears maximum number of times in the array.

arrA = [4, 1, 5, 2, 1, 5, 9, 8, 6, 5, 3, 2, 4, 7]
Output: Element repeating maximum no of times: 5, maximum count: 3

"""

from collections import Counter

def element_appears_maximum_number(A):
    # sort array
    A.sort()
    count_values = Counter(A)
    max_count = 0
    element_index = A[0]
    for k, v in count_values.items():
        if max_count < v:
            max_count = v
            element_index = i
            
            if max_count != element_index:
                max_count = 0
    return max_count


if __name__ == "__main__":
    arrA = [4, 1, 5, 2, 1, 5, 9, 8, 6, 5, 3, 2, 4, 7]

    print(element_appears_maximum_number(arrA))
    
        
  
  
