import http from "http";
import fs from "fs";
const port = 3000;

http
  .createServer((request, response) => {
    console.log("request url: ", request.url);

    if (request.url === "/") {
      const html = fs.readFileSync("./cache-control.html", "utf-8");

      response.writeHead(200, {
        "Content-Type": "text/html",
      });

      response.end(html);
    } else if (request.url === "/script.js") {
      response.writeHead(200, {
        "Content-Type": "text/javascript",
        "Cache-Control": "max-age=200",
      });

      response.end("console.log('script load')");
    }
  })
  .listen(port);

console.log("server listening on port ", port);
