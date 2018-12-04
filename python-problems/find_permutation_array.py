"""
Given two arrays of equal size n and an integer k. The task is to permute both arrays such that sum of their corresponding element is greater than or equal to k i.e A[i] + B[i] >= k.

Input : A[] = {2, 1, 3}, 
        B[] = { 7, 8, 9 }, 
        k = 10. 
Output : 1
Permutation  A[] = { 1, 2, 3 } and B[] = { 9, 8, 7 } 
satisfied the condition A[i] + B[i] >= K.

"""
def isPermute(array_sum, k):
    for value in array_sum:
	    if value < k :
		    return False
    return True

def find_permutation_array():
	# Input of the test case
	t = int(raw_input())

	# one by one run for all the input test cases
	for i in range(0, t):
		# array of  Input Size of array
		array_input = map(int, raw_input().split())
		# size of array
		n = array_input[0]
		# comparission value
		k = array_input[1]
		# Inputs of array a and b
		a = map(int, raw_input().split())
		b = map(int, raw_input().split())
		# sorting the array a in desending order
		a.sort(reverse=True)
		# sorting the array b in increasing order
		b.sort(key=int)
		array_sum = map(lambda x,y: x+y, a, b)
		bool_value = isPermute(array_sum, k)
		if bool_value:
		    print 1
		else:
		    print 0

if __name__ == "__main__":
    find_permutation_array()
