// what's funny is a wrote this for myself and looked up to verify the name of the interface ("stringer")
// and this was almost the exact example in a tutorial of go on go.dev
package main

import "fmt"

type Person struct {
	name string
	age  int
}

// give any custom type a String() string method and it will be called when anything needs it "ToString"
func (p Person) String() string {
	return fmt.Sprintf("Hey, I'm %s, I'm %d\n", p.name, p.age)
}

func main() {
	jim := Person{name: "jim", age: 43}
	fmt.Printf("%s", jim)

}
