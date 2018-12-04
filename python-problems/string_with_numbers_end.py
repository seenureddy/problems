"""
Input:  S = "geeks5"
Output:  1
Explanation : As geeks is of 5 length and at 
              last number is also 5.

Input:  S = "geeksforgeeks15"
Output:  0
Explanation: As geeksforgeeks is of 13 length and
             at last number is 15 i.e. not equal

"""

def string_with_numbers_end():

	# Number of tests
	t = int(raw_input())

	for i in range(0, t):
	    # input alpha numberic value
	    string = raw_input().strip()
	    # find string
	    str_value = string.rstrip("0123456789")
	    length_of_string = len(str_value)
	    if length_of_string:
	        # get number from string
	        int_value = int(string[length_of_string:])
	        # check the length of string and number matching or not
	        if length_of_string == int_value:
	            print 1
	        else:
	            print 0

if __name__ == "__main__":
    string_with_numbers_end()
