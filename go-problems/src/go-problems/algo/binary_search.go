package main

import "fmt"

func binarySearch(element int, haystack []int) bool {
	low := 0
	high := len(haystack) - 1
	for low <= high {
		median := (low + high) / 2
		if haystack[median] < element {
			low = median + 1
		} else {
			high = median - 1
		}
	}
	if low == len(haystack) || haystack[low] != element {
		return false
	}
	return true
}

func main() {
	items := []int{1, 2, 9, 20, 31, 45, 63, 70, 100}
	fmt.Println(binarySearch(63, items))
}
