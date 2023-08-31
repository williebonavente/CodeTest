package main

import "fmt"

func main27() {

	if 20 > 18 {

		fmt.Println("20 is greater than 18")
	}
}

func main28() {
	x := 20
	y := 18

	if x > y {
		fmt.Println("x is greater than y")
	}
}

// Nested else-if
func main29() {
	num := 20
	if num >= 10 {
		fmt.Println("Num is more than 10.")
		if num > 15 {
			fmt.Println("Num is also more than 15.")
		}
	} else {
		fmt.Println("Num is less than 10.")
	}
}
