/*

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

EX:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

*/

package main

import (
	"fmt"
)

func twoSum(nums []int, target int) []int {
	pervMap := make(map[int]int)
	result := []int{}
	for i, v := range nums {
		diffValue := target - v
		value, ok := pervMap[diffValue]

		if ok {
			result = append(result, value, i)
		}
		pervMap[v] = i


	}
	return result
}
func main() {
	fmt.Println("Hello, playground")
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
}
