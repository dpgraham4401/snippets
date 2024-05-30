// from the Mozilla Developer docs
// The `this` keyword refers to the context where a piece of code, such as a function's body, is supposed to run.
// Most typically, it is used in object methods, where this refers to the object that the method is attached to,
// thus allowing the same method to be reused on different objects.

function functionsHaveThis() {
  return this;
}

class AClass {
  getThis() {
    return this;
  }

  anotherMethod() {
    return "hello";
  }
}

if (require.main === module) {
  const anObject = new AClass();
  console.log("Method this: ", anObject.getThis());
  console.log("Function this: ", functionsHaveThis());
  console.log("Global this: ", this);
}
