package main
import "fmt"

func main7(){
	
	var a bool = true
	var b int = 5
	var c float32 = 3.14
	var d string = "Hi!"

	fmt.Println("Boolean: ", a)
	fmt.Println("Int: ", b)
	fmt.Println("Float: ", c)
	fmt.Println("String: ", d)
	
}

// Boolean
func main8() {

	var b1 bool= true
	var b2 bool = true
	var b3 bool
	b4 := true

	fmt.Println(b1)
	fmt.Println(b2)
	fmt.Println(b3)
	fmt.Println(b4)
}

// Integer
func main9() {

	var x int = 5000
	var y int = -4500
	fmt.Printf("Type: %T, value: %v\n", x, x)
	fmt.Printf("Type: %T, value: %v", y, y)
}

// Float32
func main10() {

	var x float32 = 123.78
	var y float32 = 3.4e+38
	fmt.Printf("Type: %T, value: %v\n", x, x)
	fmt.Printf("Type: %T, value: %v", y, y)
}

// Float64
func main11() {

	var x float64 = 1.7e+308
	fmt.Printf("Type: %T, value: %v", x, x)
}

// String 
func main12() {
	var txt1 string = "Hello"
	var txt2 string 

	txt3 := "World 1"

	fmt.Printf("Type: %T, value: %v\n", txt1, txt1)
	fmt.Printf("Type: %T, value: %v\n", txt2, txt2)
	fmt.Printf("Type: %T, value: %v\n", txt3, txt3)
}