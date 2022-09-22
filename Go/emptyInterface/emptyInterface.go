package main

import (
	"fmt"
	"os"
	"reflect"
)

func main() {
	test := os.Getenv("HELLO")
	fmt.Println(test)
	// I think of the empty interface as a way of have dynamic typing (which is wrong but whatever)
	var i interface{}
	i = "hello"
	describe(i)

	// Something important to keep in mind is everything "satisfies" the empty interface,
	// so anything can be assigned to it
	i = 42
	describe(i)

	// we can use type assertions to inspect the dynamic type of an interface
	iType, ok := i.(int)
	fmt.Println(iType, ok)

	// we can also use the 'reflect' package to inspect types
	iRefType := reflect.TypeOf(i)
	fmt.Println(iRefType)

	// reflection returns a 'Type' which has methods we can use to inspect further
	iKind := iRefType.Kind() // -> returns a Kind type which is easy to compare
	if iKind == reflect.String {
		fmt.Println("i has a dynamic type (kind) of string")
	} else if iKind == reflect.Int {
		fmt.Println("i has a dynamic type (kind) of int")
	} else {
		fmt.Printf("i is not int or string, dynamic type (kind) of %T\n", iKind)
	}

}

func describe(i interface{}) {
	fmt.Printf("<%v, %T>\n", i, i)
}
