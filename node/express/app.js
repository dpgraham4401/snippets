import http from "http";

const server = http.createServer((req, res) => {
  if (req.url === "/") {
    res.end("Hello");
  }
});

server.listen(2000);
