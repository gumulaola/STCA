import fetch from "node-fetch";

fetch("https://www.baidu.com")
  .then((res) => {
    return res.text();
  })
  .then((res) => {
    console.log(res.slice(0, 300));
  });

let fetchRes = await fetch("https://www.baidu.com");
let text = await fetchRes.text();
console.log(text.slice(0, 300));
