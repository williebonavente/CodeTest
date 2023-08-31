package main

import "fmt"

// Basics

func main23() {
	var a = 15 + 25
	fmt.Println(a)
}

func main24() {

	var(
		sum1 = 100 + 50 
		sum2 = sum1 + 250
		sum3 = sum2 + sum2
	)

	fmt.Println(sum3)
}