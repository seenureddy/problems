"""
Largest sub-array problem

You have an array containing positive and negative numbers (no zeros). How will you find the sub-array with the largest sum.

Example: If the array is: 1, 4, -6, 8, 1, -4, 5, -3, 1, -1, 6, -5
The largest sub-array is: 8, 1, -4, 5, -3, 1, -1, 6

NOTE: You've to print the largest sub-array (with all integers), NOT the largest numeric sum total.

Boundary condition: For an array with all negative numbers, the largest number is the answer. For an array with all positive numbers, the whole array is the answer.
Sample Input
(Plaintext Link)

1, 4, -6, 8, 1, -4, 5, -3, 1, -1, 6, -5

Sample Output
(Plaintext Link)

8, 1, -4, 5, -3, 1, -1, 6

"""

import operator

def larget_sub_arry():
    """
    We will take an array and print the largest sum of sub array.
    Input:

        1, 4, -6, 8, 1, -4, 5, -3, 1, -1, 6, -5

    Sample Output
        8, 1, -4, 5, -3, 1, -1, 6

    """
    largest_array = raw_input('Enter An Array?\n')
    largest_array = [int(i) for i in largest_array.strip().split(", ")]
    find_sub_array_dict, length_array = {}, len(largest_array) 
    for j in xrange(1, length_array + 1):
        for i in xrange(1, length_array + 1):
            sub_array = largest_array[i - 1 : length_array - 1]
            amount = sum(sub_array)
            if amount:
                find_sub_array_dict[amount] = sub_array
    return find_sub_array_dict

if __name__ == '__main__':
    sub_array_dict = larget_sub_arry()
    print max(sub_array_dict.iteritems(), key=operator.itemgetter(1))[1]



