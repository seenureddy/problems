"""
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
 
Example 1:
Input: matrix = [[3,7,8], 
                 [9,11,13],
                 [15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
"""

def smallest_colum(mat, n, m):
    lu_list = []
    for i in range(len(mat)):
        min_index = 0
        min_value = mat[i][min_index]
        for j in range(len(mat[min_index])):
            if(mat[i][j] < min_value):
                min_index = j
        is_found = True
        for k in range(len(mat)):
            if mat[k][min_index] > min_value:
                is_found = False
                break
        if is_found:
            lu_list.append(min_value)
    return max(lu_list)

def min_in_row_and_max_in_column(mat):
    element_list = []
    for i, ma in enumerate(mat):
        min_value = min(ma)
        min_index = ma.index(min_value)
        is_found = True
        for k in range(len(mat)):
            if mat[k][min_index] > min_value:
                is_found = False
                break
        if is_found:
            element_list.append(min_value)
    return element_list

if __name__ == '__main__':
    mat = [[3,7,8], 
           [9,11,13],
           [15,16,17]]

    print(min_in_row_and_max_in_column(mat))
    
    
    n = 3
    m = 3
    mat = [[3,7,8], 
           [9,11,13],
           [15,16,17]]

    print(smallest_colum(mat, n, m))
