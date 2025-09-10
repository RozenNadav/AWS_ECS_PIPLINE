// Load the HTTP module
const http = require("http");

// Define the hostname and port
const hostname = "127.0.0.1";
const port = 3000;

// Create the server
const server = http.createServer((req, res) => {
  res.statusCode = 200; // OK
  res.setHeader("Content-Type", "text/plain");
  res.end("Hello, World!\n");
});

// Start listening
server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
