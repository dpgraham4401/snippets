package main

import "fmt"

func main() {
	// maps are Go's easy implementation of hash tables
	// a basic map looks like...
	//		map[KeyType]ValueType
	// where KeyType is any comparable type and ValueType may be any type at all

	// comparable types are boolean, numeric, string, pointer,
	// channel, and interface types, as well as structs or arrays that contain only those types

	// to initialize a map, we need to use Go's make function
	m := make(map[string]int)

	// after initialization, we can add our key/value pairs
	m["david"] = 99
	m["kelly"] = 17
	m["john"] = 24

	fmt.Printf("<%v, %T>\n", m["david"], m["david"])

	// we can do all sorts of stuff with maps like iterate over values and delete them.
	for key, value := range m {
		// the order of iteration is not guaranteed to be the same every time
		fmt.Printf("%v:\t%v\n", key, value)
	}

	// a reference to a non-existent key will return the default nil ValueType (e.g., boolean: false, int: 0)
	nonKey := "kevin"
	fmt.Printf("non existant key %s: %v\n", nonKey, m[nonKey])

}
