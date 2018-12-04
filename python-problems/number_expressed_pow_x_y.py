"""
Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow . Each test cases contains an integer N.

Output:
For each test case in a new line print 1 if the number can be expressed as  xy else print 0.

Example:
Input:
2
8
5
Output:
1
0

"""

import math

def is_pow(n):
    x = 2
    if (n == 1):
        return True
    # x is equal to square root of n
    while(x <= math.sqrt(n)):
        p = x
        while (p <= n):
            p *= x
            if (p == n):
                return True
        x += 1
    return False

def number_expressed_pow_x_y():
	t = int(raw_input())

	for i in range(0, t):
	    number = int(raw_input())
	    bool_val = is_pow(number)
	    if bool_val :
	        print 1
	    else:
	        print 0

if __name__ == "__main__":
     number_expressed_pow_x_y()
