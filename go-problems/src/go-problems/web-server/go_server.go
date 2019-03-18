package main

import (
	"fmt"
	"net/http"
)

func indexHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Go is great!")
}

func aboutHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Check it out")
}

func main() {
	http.HandleFunc("/", indexHandler)
	http.HandleFunc("/about/", aboutHandler)
	fmt.Println("Starting the server ...")
	http.ListenAndServe(":8000", nil)
}
