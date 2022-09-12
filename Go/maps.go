package main

import "fmt"

func main() {
	// maps are Go's easy implementation of hash tables
	// a basic map looks like...
	//		map[KeyType]ValueType
	// where KeyType is any comparable type and ValueType may be any type at all

	// to initialize a map, we need to use Go's make function
	m := make(map[string]int)

	// after initialization, we can add our key/value pairs
	m["david"] = 1
	m["kelly"] = 2
	m["john"] = 3

	fmt.Printf("<%v, %T>\n", m["david"], m["david"])

}
