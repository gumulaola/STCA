function sendRequests(urls, max, callback) {
  let curNum = 0;
  let result = [];
  let total = urls.length;

  let sendOneRequest = (url) => {
    return new Promise((resolve, reject) => {
      let period = Math.random() * 3000;
      setTimeout(() => {
        console.log(url + " take " + period + ".");
        resolve(url);
      }, period);
    });
  };

  let send = (urlArr) => {
    while (curNum < max && urlArr.length > 0) {
      curNum++;
      let urlToSend = urlArr.shift();
      console.log(urlToSend + " is started.");
      sendOneRequest(urlToSend).then((res) => {
        console.log(res + " is finished.");
        result.push(res);
        curNum--;
        send(urlArr);
        result.length === total && callback();
      });
    }
  };

  send(urls);
}

sendRequests([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 3, () => {
  console.log("All are finished.");
});
