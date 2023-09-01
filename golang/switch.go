package main 
import "fmt"

func main30() {

	day := 4

	switch day {
	case 1:
		fmt.Println("Monday")	
	case 2:
		fmt.Println("Tuesday")
	case 3:
		fmt.Println("Wednesday")
	case 4:
		fmt.Println("Thursday")
	case 5:
		fmt.Println("Friday")
	case 6:
		fmt.Println("Saturday")
	case 7:
		fmt.Println("Sunday")
	}
}

func main31() {
	var day = 2
	switch day {
	case 1:
		fmt.Print("Saturday")
	case 2:
		fmt.Print("Sunday")
	}
}

func main32() {
	day := 5

	switch day {
	case 1, 3, 5:
		fmt.Println("Odd Weekday")
	case 2, 4:
		fmt.Println("Even Weekday")
	case 6, 7:
		fmt.Println("Weekend")
	default:
		fmt.Println("Invalid day of number.")
	}
}