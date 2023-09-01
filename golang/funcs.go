package main

import "fmt"

// No Params
func main35() {
	fmt.Println("Function 36 calling!")
}

// With
func main36(fname string) {
	fmt.Println("Hello", fname, "Bonavente")
}

func main37(fname string, age int) {
	fmt.Println("Hello", fname, "Bonavente\n", "You are", age, "years young.")
}