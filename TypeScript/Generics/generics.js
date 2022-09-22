// TypeScript Generics
// Generics are a way to make TypeScript functions more reusable
// unlike JavaScript, when you declare a function in TS, we also tell it the type of object to expect.
// if we give it something other than that type, it will freak the math out!
// a function is made generic with the following syntax
function sayHello(myParam) {
    console.log("<".concat(typeof myParam, ", ").concat(myParam, ">"));
}
sayHello("blah");
sayHello(42);
// arrow functions are made generic like so (but best to avoid in .tsx files)
var myArrowFunc = function (myParam) { return console.log(myParam); };
myArrowFunc({ code: 'mI6' });
// note: <T> is not required, but idiomatic to use single capitol letters like so (especially 'T')
// we can use multiple generics values
function multiGeneric(first, second) {
    if (typeof first === typeof second) {
        console.log("First and Second params are of type <".concat(typeof first, ">"));
    }
    else {
        console.log("Not the same type (".concat(typeof first, " & ").concat(typeof second, ")"));
    }
}
multiGeneric(12, 24);
multiGeneric(12, "number");
var jim = {
    name: "jim"
};
var dave = {
    name: 42
};
console.log("Jim's name =", jim.name);
console.log("Dave's name =", dave.name);
