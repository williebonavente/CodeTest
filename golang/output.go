package main
import "fmt"

func main3() {
	var i, j string =  "Hello ", "World"
	fmt.Print(i)
	fmt.Print(j)
}

func main4() {
	var i  string = "Hello"
	var j  int = 15

	fmt.Printf("i has value: %v and type: %T\n", i, i)
	fmt.Printf("i has value: %v and type: %T\n", j, j)
}

/*
%v default format
%#v Go-syntax format
%T type of the value
%% % sign
*/

func main5() {

	var i = 15.5
	var txt = "Hello, World"

	fmt.Printf("%v\n", i)
	fmt.Printf("%#v\n", i)
	fmt.Printf("%v%%\n", i)
	fmt.Printf("%T\n", i)

	fmt.Printf("%v\n", txt)
	fmt.Printf("%#v\n", txt)
	fmt.Printf("%T\n", txt)
}

func main6() {
	
	var i = 15

	fmt.Printf("%b\n", i)
	fmt.Printf("%d\n", i)
	fmt.Printf("%+d\n", i)
	fmt.Printf("%o\n", i)
	fmt.Printf("%O\n", i)
	fmt.Printf("%x\n", i)
	fmt.Printf("%X\n", i)
	fmt.Printf("%#x\n", i)
	fmt.Printf("%4d\n", i)
	fmt.Printf("%4d\n", i)
	fmt.Printf("%-4d\n", i)
	fmt.Printf("%04d\n", i)
}