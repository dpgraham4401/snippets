/**
 * Objects in JavaScript are only shallow copied by default.
 * JS has an 'StructuredClone' method that can be used to deep clone objects.
 * But we may be asked to implement this in an interview.
 */

const nestedObject = {
  foo: "bar",
  count: 2,
  user: {
    name: "david",
    email: "david@gmail.com",
    profile: {
      theme: "dark",
      oauth: "google.com",
    },
    peers: [
      { name: "fasdf", email: "asdf@gmail.co" },
      { name: "lkj", email: "qwe@gmail.com" },
    ],
  },
};

// const shallowCopy = { ...nestedObject };

// showNestedUserName(nestedObject, shallowCopy)
// shallowCopy.user.name = "bob";
// showNestedUserName(nestedObject, shallowCopy)

function showNestedUserName(obj, copyObj) {
  console.log("Original: ", obj.user.name, "copy: ", copyObj.user.name);
}

// const deepCopyObj = structuredClone(nestedObject);
// showNestedUserName(nestedObject, deepCopyObj);
// deepCopyObj.user.name = "alice";
// showNestedUserName(nestedObject, deepCopyObj);

/***
 * This is relatively simple, we're just using a recursive technique to visit 
 * all children. if it doesn't have a type of "object", return it, else
 * handle arrays of sub-objects.
 */
function deepClone(obj) {
  if (typeof obj != "object") {
    return obj;
  }
  if (Array.isArray(obj)) {
    return obj.map((subObject) => deepClone(subObject));
  }
  let copy = {};
  for (let key in obj) {
    if (typeof obj[key] != "object") {
      copy[key] = obj[key];
    } else {
      copy[key] = deepClone(obj[key]);
    }
  }
  return copy;
}

const deepClone = deepClone(nestedObject);
console.log("deepClone", deepClone);

