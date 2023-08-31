package main
import "fmt"

func main13() {
	
	var arr1 = [3]int{1, 2, 3}
	arr2 := [5] int{4,5,6,7,8}

	fmt.Println(arr1)
	fmt.Println(arr2)

}

func main14() {
	var cars = [4]string {"Volvo" , "BMW", "Ford", "Mazada"}
	fmt.Print(cars)
}

// Accessing element in the array
func main15() {
	prices := [3]int{10, 20, 30}

	fmt.Println(prices[0])
	fmt.Println(prices[2])
}

func main16() {
	prices := [3]int{10, 20, 30}

	prices[2] = 50
	fmt.Println(prices)
}

func main17() {

	arr1 := [5] int{} // not init
	arr2 := [5]int{1, 2} // partially init
	arr3 := [5] int{1, 2, 3, 4, 5} // fully init

	fmt.Println(arr1)
	fmt.Println(arr2)
	fmt.Println(arr3)
}

func main18() {
	arr1 := [5]int{1:10, 2:40}

	fmt.Println(arr1)
}

// len()
func main19() {
	arr1 := [4] string{"Volvo", "BMW", "Ford", "Mazda"}
	arr2 := [...]int{1, 2, 3, 4, 5, 6}
	
	fmt.Println(len(arr1))
	fmt.Println(len(arr2))
}

//  Slicing an array
func main20() {

	myslice1 := []int{}
	fmt.Println(len(myslice1))
	fmt.Println(cap(myslice1))
	fmt.Println(myslice1)

	myslice2 :=[]string{"Go", "Get", "a", "life", "!"}
	fmt.Println(len(myslice2))
	fmt.Println(cap(myslice2))
	fmt.Println(myslice2)
}