import fetch from "node-fetch";

fetch("https://www.baidu.com")
  .then((res) => {
    return res.json();
  })
  .then((res) => console.log(res));
