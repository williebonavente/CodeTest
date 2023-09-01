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

func main40(x int, y string) (result int, txt1 string) {
	result = x + x
	txt1 = "Hi" + y 
	return 
}

//..Recursive 
func main41_recur(x int ) int {
	if x == 11 {
		return 0
	}
	fmt.Println(x)
	return main41_recur(x + 1)
}

//..Factorial recursive 
func main42_factorialRecursive(x float64) (y float64) {
	if x > 0 {
		y = x * main42_factorialRecursive(x - 1)
	} else {
		y = 1
	}
	return 
}
