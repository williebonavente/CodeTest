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

// Returning
func main38(x int, y int) int {
	return x + y
}

func main39(x int, y int) (result int ) {
	result = x + y 
	return 
}