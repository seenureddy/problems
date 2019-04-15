package main

import (
	"fmt"
)

// https://gobyexample.com/pointers
func zerovalue(prt int) {

	prt = 0
	fmt.Println("address 22:", &prt)
}

func zeroptr(ptr *int) {
	*ptr = 0
}

func main() {
	i := 1
	fmt.Println("Hello, playground", 1)
	fmt.Println("address:", &i)
	zerovalue(i)
	fmt.Println("pointer:", &i)
	fmt.Println("value", i)
	fmt.Println("value address", &i)
	zeroptr(&i)
	fmt.Println("pointer", &i)
	fmt.Println("value iiii:", i)

}
