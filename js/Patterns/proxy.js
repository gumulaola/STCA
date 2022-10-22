function StockAPI() {
  this.getPrice = function (stock, callback) {
    console.log("Calling...");
    setTimeout(() => {
      if (stock === "MICROSOFT") {
        callback(300);
      } else if (stock === "APPLE") {
        callback(200);
      } else {
        callback("Not a stock.");
      }
    }, Math.random() * 2000);
  };
}

function StockAPIProxy() {
  this.cache = new Map();
  this.realStockAPI = new StockAPI();

  this.getPrice = function (stock, callback) {
    if (this.cache.has(stock)) {
      console.log("Get from cache");
      callback(this.cache.get(stock));
    } else {
      this.realStockAPI.getPrice(stock, (res) => {
        this.cache.set(stock, res);
        callback(res);
      });
    }
  };
}

let ins = new StockAPIProxy();

ins.getPrice("APPLE", (res) => {
  console.log(res);
});

ins.getPrice("MICROSOFT", (res) => {
  console.log(res);
});

setTimeout(() => {
  ins.getPrice("MICROSOFT", (res) => {
    console.log(res);
  });

  ins.getPrice("APPLE", (res) => {
    console.log(res);
  });

  ins.getPrice("AMAZON", (res) => {
    console.log(res);
  });
}, 3000);
