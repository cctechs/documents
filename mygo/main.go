package main

import (
	"fmt"
	"net/http"
)

func echo(req http.ResponseWriter, request *http.Request) {
	fmt.Println("here")
}

func main() {
	fmt.Println("starting...")
	http.HandleFunc("./", echo)
	http.ListenAndServe(":8081", nil)
}
