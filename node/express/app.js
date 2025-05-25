import { readFile, writeFile } from "fs";

readFile("./content/first.txt", "utf-8", (err, result) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(result);
  const processedData = `Wll hello there, ${result}`;
  writeFile("./content/results.txt", processedData, (err, data) => {
    if (err) {
      console.log("write error", err);
      return;
    }
    console.log("Done writing to file");
  });
});
