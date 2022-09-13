#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct dynamicPerson {
  int age;
  char *name;
};

struct staticPerson {
  int age;
  char name[50];
};

int main() {
    // C does not have direct support for strings, so things may feel clunky sometimes, but string 101 is there are no
    // strings, only array's of character. To initialize a string
    // 1. Provide a size at compile time
    int myStringLen = 10;
    char myString[myStringLen];
    // 2. Provide a string during initialization
    char myPersonString[] = "jim";
    // There's other ways via assigning each array element, not touching that.

    // Character arrays cannot be assigned a string literal with the '=' operator once they have been declared.
    // to assign a value, we need to use functions from the <string.h> library
    strcpy(myString, "hello!");
    printf("%s\n", myString);
    // We either need to allocate enough space while initializing or dynamically allocate
    struct dynamicPerson jim;
    jim.age = 21; // with a int field, it's no problem to assign after initialization
    printf("%d\n", jim.age);
    // jim.name = "jim"; but THIS WILL FAIL!!!

    // with something like a string field in a struct, we have basically 3 options
    // 1. Our strength length is constant (we only allow using constant length strings)
    // 2. We make it overly large to ensure the field doesn't overflow
    //      --> there's wasted space/memory, but it's easy (a trade-off)
    //      --> Like the staticPerson struct above
    // 3. We use a pointer to a string, malloc for the string pointer, then copy the value
    //      --> like the dynamicPerson struct above (code below)

    jim.name = malloc(sizeof(char) * strlen(myPersonString)+1);
    // remember to allocate +1 for the null-terminating character '\0'
    strcpy(jim.name, myPersonString);
    printf("%s\n", jim.name);

    return 0;
}
