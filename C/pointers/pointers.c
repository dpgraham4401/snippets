// Created by David Graham on 9/12/22.
//
#include <stdio.h>
#include <string.h>

struct Person {
  int age;
};

void agePlusOne(struct Person *p) {
    // p is a pointer to the Person struct argument
    printf("In function: \t\t%d\n", p->age);
    p->age = p->age + 1;
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

    // If we'd like to use fields in a struct pointer (wording) we use a separate notation
    struct Person jim;
    // dot notation for regular struct access
    jim.age = 42;
    // use the '->' notation to access members in a pointer to struct
    struct Person *jimPointer = &jim;
    printf("Person age: \t\t%d\n", jimPointer->age);

    // When passing struct to a function
    // if we pass a struct as an argument, an entire copy will be made (within the function scope)
    //      --> this is kind of wasteful, and may not be what we want if we need to modify fields
    agePlusOne(&jim);
    printf("Person age: \t\t%d\n", jimPointer->age);
}
