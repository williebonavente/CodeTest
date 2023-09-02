package main

import "fmt"

func main44() {
	var a  = map[string]string{"brand": "Ford", "model": "Mustang", "year": "1964"}
	b := map[string]int{"Oslo": 1, "Bergen": 2, "Trondheim": 3, "Stavanger": 4}

	fmt.Printf("a\t%v\n", a)
	fmt.Printf("b\t%v\n", b)
}


func main45() {
	var a = make(map[string]string) // empty map
	a["brand"] = "Ford" // inserting value
	a["model"] = "Mustang" 
	a["year"] = "1964"

	b:= make(map[string]int)
	b["Oslo"] = 1
	b["Bergen"] = 2
	b["Trondheim"] = 3
	b["Stavanger"] = 4
}

// Creating an empty map with make function key
func main46() {
	var a = make(map[string]string)
	var b map[string]string

	fmt.Println(a == nil)
	fmt.Println(b == nil)
}
// Accessing the map elements
func main47() {
	var  a = make(map[string]string)
	a["brand"] = "Ford"
	a["model"] = "Mustang"
	a["year"] = "1964"

	fmt.Println(a["brand"])
}

// Updating

func main48() {
	var a = make(map[string]string)
	a["brand"] = "Ford"
	a["model"] = "Mustang"
	a["year"] = "1964"

	fmt.Println(a)

	a["year"] = "1970" // Updating an element
	a["color"] = "RED" // Adding element

	fmt.Println(a)
}

// Remove Element from Map

func main49() {
	var a = make(map[string]string) 
	a["brand"] = "Ford"
	a["model"] = "Mustang"
	a["year"] = "1964"

	fmt.Println(a)
	delete(a, "year")
	fmt.Println(a)
}