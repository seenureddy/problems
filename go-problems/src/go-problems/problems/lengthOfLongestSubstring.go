/* Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

*/


package main

import (
	"fmt"
	//"math"
)

func Max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

func lengthOfLongestSubstring(s string) int {
	count := 0
	start := 0
	repeatData := make(map[string]int)
	for i, v := range s {
		//fmt.Println(i, string(v))
		_, ok := repeatData[string(v)]
		if ok && start <= repeatData[string(v)] {
			start = repeatData[string(v)] + 1
		} else {
			count = Max(count, i-start+1)
		}

		repeatData[string(v)] = i
	}
	return count
}

func main() {
	fmt.Println(lengthOfLongestSubstring("Hello, playground"))
	fmt.Println(lengthOfLongestSubstring("abcabcbb"))
}

