import os from "os";

// info on current user
const user = os.userInfo();
console.log(user);

// System uptime (in seconds)
console.log(`The system ${os.uptime()} in seconds`);

const currentOs = {
  name: os.type(),
  release: os.release(),
  totalMem: os.totalmem(),
  freeMeme: os.freemem(),
};

console.log(currentOs);
