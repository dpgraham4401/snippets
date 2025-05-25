// In CommonJs, all files are modules by default.
// Node.js added stable support for ES modules since Node.js v14

const sayHello = (name) => {
  console.log(`Hello, ${name}!`);
};

module.exports = {
  sayHello
};
