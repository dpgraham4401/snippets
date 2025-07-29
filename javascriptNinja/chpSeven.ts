/**
 * Even before the 'class' syntactic sugar, JavaScript had a object-oriented elements to it.
 *
 */

/**
 * In JavaScript, 'this' is a special parameter that is implicitly passed to functions.
 * (Along with the 'arguments' object which we pretty much never need to touch.)
 */
function Mammal(this: any, name: string, age: number) {
  this.name = name;
  this.age = age;
}

// We can create new instances of Person using the 'new' keyword (even though it is not a class).
// TypeScript generally does not like this old-school style of trying to use a function as a constructor.
// We can get around it with a type assertion, kinda hacky and hard to read.
const animal = new (Person as any)("Huey", 30);
console.log(animal.name); // Huey

/**
 * JavaScript doesn't have inheritance like some languages, but it does have prototypes.
 * Every object has a prototype, which points to another object, all the way down to
 * the base Object prototype, which prototype points to null.
 */

function Person(this: any, name: string, age: number) {
  Mammal.call(this, name, age);
  this.type = "Person";
}

// @ts-ignore
const alice = new Person("Alice", 25);

console.log(alice.name); // Alice
console.log(alice.age); // 25
console.log(alice.type); // Person

/**
 * ES6 introduced the 'class' syntax, which is just syntactic sugar over the existing prototype-based inheritance.
 * it makes it easier for people coming from traditional OOP languages to read JS, and just
 * makes the code cleaner and more readable.
 */

/**
 * This is a lot nicer to read, isn't it.
 */
class Animal {
  age: number;
  // It's common convention to use a leading underscore for private properties.
  private _name: string;

  constructor(name: string, age: number) {
    this._name = name;
    this.age = age;
  }

  // Getter for the name property (Note the 'get' keyword).
  get name(): string {
    return this._name;
  }

  // Setter for the name property (Note the 'set' keyword).
  set name(value: string) {
    this._name = value;
  }
}

class Dog extends Animal {

}

const lion = new Animal("Leo", 5);
console.log(lion.name); // Leo

const sparky = new Dog("Sparky", 3);
console.log(Object.getPrototypeOf(sparky)); // Animal {}


