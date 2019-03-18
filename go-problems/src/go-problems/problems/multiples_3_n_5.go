package main

import (
	"fmt"
)

func sumOfMultiple(multiple, number int) int {

	target := number / multiple

	return (multiple * (target * (target + 1))) / 2

}

func main() {
	output := sumOfMultiple(3, 999) + sumOfMultiple(5, 999) - sumOfMultiple(15, 999)
	fmt.Println("Sum of 3 and 5 multiples", output)
}
