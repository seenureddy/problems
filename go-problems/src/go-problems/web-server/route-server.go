package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/gorilla/mux"
)

func main() {

	router := mux.NewRouter().StrictSlash(true)
	router.HandleFunc("/", Index)
	fmt.Println("Starting the server ...")
	log.Fatal(http.ListenAndServe(":8080", router))

}

// Index - Request and Response
func Index(w http.ResponseWriter, r *http.Request) {
	// fmt.Fprintf(w, "Hello, %q", html.EscapeString(r.URL.Path))
	fmt.Fprintln(w, "Welcome!")
}
