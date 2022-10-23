let nums = [1, 2, 3, 4, 5];

let numsProxy = new Proxy(nums, {
  get: function (target, p) {
    if (p === "-1") {
      return target[target.length - 1];
    } else {
      return target[p];
    }
  },
});

console.log(numsProxy[-1]);
