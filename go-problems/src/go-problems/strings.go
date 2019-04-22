package main

import (
	"fmt"
	"strings"
)

// Reverse the string
func Reverse(str string) string {
	if str != "" {
		return Reverse(str[1:]) + str[:1]
	}
	return ""
}

// Reverse the words
func ReverseWords(s string) string {
	// SPLIT the string into slice
	// words := strings.Split(s, " ")
	words := strings.Fields(s)
	
	fmt.Println(words)
	for i, j := 0, len(words)-1; i < j; i, j = i+1, j-1 {
		words[i], words[j] = words[j], words[i]
	}
	return strings.Join(words, " ")
}

func main() {
    // Reverse the words
	fmt.Println(ReverseWords("Hello, playground"))
	fmt.Println(ReverseWords("How are you?"))
    // Reverse the string
	fmt.Println(Reverse("Hello,playground"))
}
