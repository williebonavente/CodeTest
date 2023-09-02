package main

import "fmt"

type Person struct {
	name   string
	age    int
	job    string
	salary int
}

func main43() {
	var person1 Person
	var person2 Person

	// Person1 specs
	person1.name = "Damian"
	person1.age = 32
	person1.job = "Guard"
	person1.salary = 5_000

	// Person2 specs
	person2.name = "Rad"
	person2.age = 35
	person2.job = "Forward"
	person2.salary = 3_000

	// struct calling 
	outPerson(person1)
	outPerson(person2)

}

func outPerson(per Person) {

	fmt.Println("Name: ", per.name)
	fmt.Println("Age: ", per.age)
	fmt.Println("Job: ", per.job)
	fmt.Println("Salary: ", per.salary)
}
