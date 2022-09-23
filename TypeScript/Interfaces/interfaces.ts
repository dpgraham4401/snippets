// I think I now Interfaces well but maybe I'll learn something from this snippet
// interfaces are a way to describe the shape of an object in the type system
// here's your basic enum, we've got primitive types, nested interfaces and enums, and functions

interface MyPerson {
    name: string
    age: number
    single?: boolean
    hairColor: HairColor
    sayHello: (name: string) => string
}

// an irrelevant enum
enum HairColor {
    blonde,
    brunette,
    black,
    bald
}

function getName(name: string) {
    return "Hi, my name is " + name
}

let jim: MyPerson = {
    name: "jim",
    age: 42,
    hairColor: HairColor.bald,
    // single is optional, hence the question mark
    sayHello: getName
}

console.log("jim's name: ", jim.name) // we can access object properties via dot notation
console.log("jim's age: ", jim.age)
console.log("jim, say hello: ", jim.sayHello(jim.name)) // you can abstract the function away, just leaving the interface
console.log(jim.single) // you can still access this object property, but it will be undefined

// readonly elements can't be changed once set... sort of. Like other things, it's in the type system, not javascript.
// jim.name = "steve"
// console.log(jim.name) // if you call a property read only, it will give you at compile time error, but may still run



