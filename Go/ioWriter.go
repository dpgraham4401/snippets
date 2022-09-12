package main

import (
	"fmt"
	"io"
	"os"
	"reflect"
)

type byteWriter struct {
	data []byte
}

// byteWriter is the method that satisfies the io.Writer interface so things can be written to it.
// it abstracts away the fact that when someone writes an array of bytes to it, it appends those bytes to a byte array
func (b byteWriter) Write(p []byte) (n int, err error) {
	// The byte type in Golang is an alias for the unsigned integer 8 type ( uint8 ).
	// The byte type is only used to semantically distinguish between an unsigned integer 8 and a byte.
	// The range of a byte is 0 to 255 (same as uint8 ).
	fmt.Println(string(p), "that comes from the myWriter instance of byteWriter but also prints to StdOut")
	fmt.Println(reflect.TypeOf(p)) // -> unit8
	b.data = append(b.data, p...)
	return len(p), nil
}

func main() {
	var myWriter byteWriter
	// we can use io.Writer as a way to declare an interface that could be used to write to
	// anything that implements the write method
	// so instead of
	var i io.Writer
	i = os.Stdout
	_, _ = i.Write([]byte("some bytes written to stdout\n"))
	i = myWriter
	_, _ = i.Write([]byte("some additional bytes"))
}
