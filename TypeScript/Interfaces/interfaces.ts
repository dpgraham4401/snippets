// I think I now Interfaces well but maybe I'll learn something from this snippet
// interfaces are a way to describe the shape of an object in the type system
// here's your basic enum, we've got primitive types, nested interfaces and enums, and functions

interface Person {
  name: string;
  age: number;
  single?: boolean;
  hairColor: HairColor;
  sayHello: (name: string) => string;
}

// an irrelevant enum
enum HairColor {
  blonde,
  brunette,
  black,
  bald,
}

function getName(name: string) {
  return "Hi, my name is " + name;
}

let jim: Person = {
  name: "jim",
  age: 42,
  hairColor: HairColor.bald,
  // single is optional, hence the question mark
  sayHello: getName,
};

console.log("jim's name: ", jim.name); // we can access object properties via dot notation
console.log("jim's age: ", jim.age);
console.log("jim, say hello: ", jim.sayHello(jim.name)); // you can abstract functions away
console.log(jim.single); // since 'single' is optional? it implicitly has union type "boolean | undefined"

// readonly elements can't be changed once set... sort of. Like other things, it's in the type system, not javascript.
// jim.name = "steve"
// console.log(jim.name) // if you call a property read only, it will give you at compile time error, but may still run

// interfaces can also extend other interfaces
interface Employee extends Person {
  salary: number;
  position: string;
}

const sally: Employee = {
  name: "Salli Mae",
  age: 24,
  single: false,
  hairColor: HairColor.bald,
  sayHello: getName,
  salary: 1000000000000,
  position: "Soul Sucker",
};

// the last thing is index object interfaces, since some problems create objects to store info with arbitrary keys
// it would be impossible to add all those keys to an interface, so we get index signatures, which are really type safe
interface IndexInterface {
  [i: string]: number; // objects with this type will accept and string/number (read key/value) pair and dish them back out
}

let inventory: IndexInterface = {
  apples: 5,
  bananas: 2,
};

inventory.grapes = 27; // there's no telling when someone will put in here
let i: keyof IndexInterface; // we can use the typescript 'keyof' operator to iterate through an object
console.log("Inventory...");
for (i in inventory) {
  console.log(i, ":\t", inventory[i]); // nice!
}
