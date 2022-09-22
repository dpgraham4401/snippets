// TypeScript Generics

// Generics are a way to make TypeScript functions more reusable
// unlike JavaScript, when you declare a function in TS, we also tell it the type of object to expect.
// if we give it something other than that type, it will freak the math out!


// a function is made generic with the following syntax
function sayHello<T> (myParam: T){
    console.log(`<${typeof myParam}, ${myParam}>`)
}
sayHello("blah")
sayHello(42)

// arrow functions are made generic like so (but best to avoid in .tsx files)
const myArrowFunc = <T>(myParam:T) => console.log(myParam)
myArrowFunc({code: 'mI6'})
// note: <T> is not required, but idiomatic to use single capitol letters like so (especially 'T')

// we can use multiple generics values
function multiGeneric<T, K> (first: T, second: K) {
   if (typeof first === typeof second) {
       console.log(`First and Second params are of type <${typeof first}>`)
   } else {
       console.log(`Not the same type (${typeof first} & ${typeof second})`)
   }
}

multiGeneric(12,24)
multiGeneric(12, "number")

// Interfaces can also use generics

interface Person<T> {
    name: T
}

let jim: Person<string> = {
    name: "jim"
}
let dave: Person<number> = {
    name: 42
}
console.log("Jim's name =", jim.name)
console.log("Dave's name =", dave.name)
