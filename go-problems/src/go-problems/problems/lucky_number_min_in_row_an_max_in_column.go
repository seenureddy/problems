/*

Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
 
Example 1:
Input: matrix = [[3,7,8], 
                 [9,11,13],
                 [15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
*/
package main

import (
	"fmt"
)

func minInRowAndMaxInColumn(mat [3][3]int) (result []int) {

	for i, _ := range mat {

		minIndex := 0
		minValue := mat[i][minIndex]
		//fmt.Println(minValue)

		for j, _ := range mat[minIndex] {
			// fmt.Println(mat[i][j], minValue)
			if mat[i][j] < minValue {
				minIndex = j
				// fmt.Println(minIndex)
			}

		}
		isFound := true

		for k, _ := range mat {
			if mat[k][minIndex] > minValue {
				isFound = false
				break
			}
		}

		if isFound {
			result = append(result, minValue)
		}

	}
			//fmt.Println(result)
	return result
}

func main() {

	mat := [3][3]int{{3, 7, 8}, {9, 11, 13}, {15, 16, 17}}
	fmt.Println(mat)
	fmt.Println(minInRowAndMaxInColumn(mat))
}
