import fetch from "node-fetch";

function Networking() {
  this.sendFetch = function (url, callback) {
    let response = fetch(url)
      .then((res) => {
        return res.text();
      })
      .then((res) => {
        callback(res);
      });
  };
}

function NetworkingProxy() {
  this.cache = new Map();
  this.realNetworking = new Networking();
  this.sendFetch = function (url, callback) {
    if (this.cache.has(url)) {
      console.log("Get from cache.");
      callback(this.cache.get(url));
    } else {
      console.log("Fetching...");
      this.realNetworking.sendFetch(url, (res) => {
        this.cache.set(url, res);
        callback(res);
      });
    }
  };
}

let ins = new NetworkingProxy();

ins.sendFetch("https://www.baidu.com", (res) => {
  console.log(res.slice(0, 100));
});

setTimeout(() => {
  ins.sendFetch("https://www.baidu.com", (res) => {
    console.log(res.slice(0, 100));
  });
}, 3000);
