import path from "path";
import { fileURLToPath } from "url";

console.log(path.sep); // '/'

const filePath = path.join("/content/", "subfolder", "test.txt");
console.log(filePath); // '/content/subfolder/test.txt'

const base = path.basename(filePath);
console.log(base); // 'test.txt'

// note, we need to import dirname instead of relying on __dirname global when using ES modules
const __filename = fileURLToPath(import.meta.url); // get the resolved path to the file
const __dirname = path.dirname(__filename); // get the name of the directory

// We could also just remove __dirname here and it would be the same result
const absolute = path.resolve(__dirname, "content", "subfolder", "test.txt");
console.log(absolute);
