// Created by David Graham on 9/12/22.
//
#include <stdio.h>
#include <string.h>

struct Person {
  int age;
};

int main() {
    // just a regular variable (int)
    int myInt = 42;
    // a pointer is, conventionally, initialized with an '*' before the variable name
    // the '&' returns the address of an existing variable
    int *myIntPointer = &myInt;
    // printing a pointer displays the address in memory
    printf("myIntPointer: \t%p\n", myIntPointer);
    // to "dereference" a pointer, we use the same '*' operator
    printf("*myIntPointer: \t%d\n", *myIntPointer);
    // the '&' operator will return the address as well, but I think of it more of as a one way street
    // as opposed to the '*' operator
    printf("&myIntPointer: \t%p\n", &myIntPointer);
    printf("&myInt: \t\t%p\n", &myInt);
    // the struct definition is global, to initialize, use "struct <StructType> <variable name>"
    struct Person jim;
    // struct fields can be assigned values via dot notation
    jim.age = 42;
    printf("jim age: %d\n", jim.age);
    // however, pointers to struct use the '->' notation to access members
    struct Person *jimPointer = &jim;
    printf("jim age from pointer: %d\n", jimPointer->age);
}
